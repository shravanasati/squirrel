import logging
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

from query_builder.database import DBConnectionParams, InvalidDBCredentials
from query_builder.llm_interaction import get_response
from query_builder.executor import get_execution_result, QueryExecutionFailed

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000  # 16MB


@app.get("/")
def home():
    return render_template("index.html")


# added route of the chat panel
@app.get("/chat")
def chat():
    return render_template("chat.html")


@app.post("/query/build")
def build_query():
    data = request.json
    if data is None:
        return {"ok": False, "message": "Missing JSON object."}, 400

    connection_uri: str | None = data.get("connection_uri")
    db_params: DBConnectionParams | str | None = connection_uri
    if not connection_uri:
        user = data.get("username")
        password = data.get("password")
        host = data.get("host")
        port = data.get("port")
        database = data.get("dbname")

        conditions = (user, password, host, port, database)
        conditions = map(lambda x: not x, conditions)
        if any(conditions):
            return {
                "ok": False,
                "message": "Missing fields to construct the database URI.",
            }, 400

        db_params = DBConnectionParams(user, password, host, port, database)

    else:
        db_params = connection_uri

    question = data.get("question")
    if not question:
        return {"ok": False, "message": "Missing the question field."}, 400

    try:
        llm_resp = get_response(question, db_params)
        print(llm_resp)
        return {"ok": True, "message": llm_resp}
    except InvalidDBCredentials:
        return {"ok": False, "message": "Invalid database credentials!"}, 400
    except Exception as e:
        logging.exception(e)
        return {
            "ok": False,
            "message": "Unable to process the request at the moment, please try again later.",
        }, 500


@app.post("/query/execute")
def execute_query():
    data = request.json
    if data is None:
        return {"ok": False, "message": "Missing JSON object."}, 400

    connection_uri: str | None = data.get("connection_uri")
    db_params: DBConnectionParams | str | None = connection_uri
    if not connection_uri:
        user = data.get("username")
        password = data.get("password")
        host = data.get("host")
        port = data.get("port")
        database = data.get("dbname")

        conditions = (user, password, host, port, database)
        conditions = map(lambda x: not x, conditions)
        if any(conditions):
            return {
                "ok": False,
                "message": "Missing fields to construct the database URI.",
            }, 400

        db_params = DBConnectionParams(user, password, host, port, database)

    else:
        db_params = connection_uri

    query = data.get("query")
    if not query:
        return {"ok": False, "message": "Missing the query field."}, 400

    try:
        result, headings_added = get_execution_result(query, db_params)
        print(result, headings_added)
        headings = result[0] if headings_added else None
        rows = result[1:] if headings_added else result
        return {"ok": True, "rows": rows, "headings": headings}
    except QueryExecutionFailed:
        return {"ok": False, "message": "Unable to execute query."}, 501
    except Exception:
        return {
            "ok": False,
            "message": "Unable to process the request at the moment, please try again later.",
        }, 500


if __name__ == "__main__":
    app.run()
