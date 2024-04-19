import os
from flask import Flask, render_template
from dotenv import load_dotenv
from database import db_session, init_db, DB_CONNECTION_URI

load_dotenv()
# init_db()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = DB_CONNECTION_URI
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000  # 16MB


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
