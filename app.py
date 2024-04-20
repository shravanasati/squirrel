import os
from flask import Flask, render_template
from dotenv import load_dotenv
from database import db_session, init_db, DB_CONNECTION_URI
from flask import request

load_dotenv()
# init_db()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = DB_CONNECTION_URI
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000  # 16MB


@app.route("/")
def home():
    return render_template("index.html")


<<<<<<< HEAD

#added route of the chat panel
=======
# added route of the chat panel
>>>>>>> 6df2eab48e92991121eacf0ada2bc8998ae94e33
@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route(" ", methods=["POST"])
def convert():
    data = request.json
    print(data)
    return data


if __name__ == "__main__":
    app.run()
