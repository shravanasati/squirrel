import os
from flask import Flask, render_template,jsonify
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

@app.route('/process-form', methods=['POST'])
def process_form():
    # Extract form data from the request
    form_data = request.json

    # Process the form data (you can perform database operations here)
    # Example: Print the form data
    print("Received form data:", form_data)

    # Return a response (optional)
    return jsonify({'message': 'Form data received successfully'}), 200


if __name__ == "__main__":
    app.run()
