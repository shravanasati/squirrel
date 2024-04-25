import logging
from .database import DBConnectionParams

import mysql.connector


class QueryExecutionFailed(Exception):
    pass


def get_execution_result(query: str, db_params: DBConnectionParams | str):
    """
    Executes the given query and returns result and an additional bool
    indicating if the column names are also returned.
    """
    try:
        if isinstance(db_params, str):
            conn = mysql.connector.connect(dsn=db_params)
        else:
            conn = mysql.connector.connect(**db_params.asdict())

        cursor = conn.cursor()
        cursor.execute(query)
        if cursor.description:
            return [c[0] for c in cursor.description] + cursor.fetchall(), True
        return cursor.fetchall(), False

    except Exception as e:
        logging.exception(e)
        # todo handle connection error differently
        raise QueryExecutionFailed(e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.commit()
            conn.close()
