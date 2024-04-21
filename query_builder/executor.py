import logging
from .database import DBConnectionParams

import mysql.connector


class QueryExecutionFailed(Exception):
    pass


def get_execution_result(query: str, db_params: DBConnectionParams | str):
    try:
        if isinstance(db_params, str):
            conn = mysql.connector.connect(dsn=db_params)
        else:
            conn = mysql.connector.connect(**db_params.asdict())

        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

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
