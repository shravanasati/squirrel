from dataclasses import dataclass
from io import StringIO
from typing import Any
import mysql.connector
from .database import DBConnectionParams, InvalidDBCredentials


@dataclass(frozen=True)
class TableRowDescription:
    field: str
    field_type: str
    null: bool
    key: str
    default: Any
    extra: str

    KEY_TABLE = {"PRI": "PRIMARY KEY", "UNI": "UNIQUE", "": ""}

    @classmethod
    def from_tuple(cls, t: tuple):
        return cls(*t)

    def generate_create_stmt_part(self):
        return f"{self.field} {self.field_type} {'NOT NULL' if not self.null else ''} {self.KEY_TABLE[self.key]} {f'DEFAULT {self.default}' if self.default else ''} {self.extra}".strip()


def construct_create_stmt(table_name: str, row_descs: list[TableRowDescription]):
    stmt = f"CREATE TABLE {table_name}(\n"
    stmt += ",\n".join((r.generate_create_stmt_part() for r in row_descs))
    stmt += "\n);\n"
    return stmt


class DDLGenerator:
    def __init__(self, connection_params: DBConnectionParams | str) -> None:
        try:
            if isinstance(connection_params, str):
                self.conn = mysql.connector.connect(dsn=connection_params)
            else:
                self.conn = mysql.connector.connect(**connection_params.asdict())
            self.cursor = self.conn.cursor()
            self.STMT_SHOW_TABLES = "show tables;"

        except Exception:
            raise InvalidDBCredentials(
                "invalid db credentials passed, unable to connect to the database"
            )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.conn:
            self.conn.close()

    def generate(self):
        self.cursor.execute(self.STMT_SHOW_TABLES)
        tables = [str(t[0]) for t in self.cursor.fetchall()]
        ddl = StringIO()
        for table in tables:
            self.cursor.execute(f"desc {table}")
            tds: list[TableRowDescription] = []
            for entry in self.cursor.fetchall():
                td = TableRowDescription.from_tuple(entry)
                tds.append(td)

            ddl.write(construct_create_stmt(table, tds) + "\n")

        ddl.seek(0)
        return ddl.read()


if __name__ == "__main__":
    with DDLGenerator(
        DBConnectionParams(
            user="root",
            password="oursql1234",
            host="localhost",
            port=3306,
            database="animeviz",
        )
    ) as gen:
        print(gen.generate())
