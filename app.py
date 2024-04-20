import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask import request

load_dotenv()
# init_db()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000  # 16MB


@app.route("/")
def home():
    return render_template("index.html")



#added route of the chat panel
@app.route("/chat")
def chat():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run()
