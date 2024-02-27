from flask import Flask, render_template, request, jsonify
from chat import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get_response", methods=["POST"])
def chat():
    if request.method == "POST":
        input_stmt = ""

        if request.headers["Content-Type"] == "application/json":
            input_stmt = request.json["chat_msg"]
        elif request.headers["Content-Type"] == "application/x-www-form-urlencoded":
            input_stmt = request.form["chat_msg"]

        response = {
            "chat_msg": input_stmt,
            "chat_response": get_chat_response(input_stmt)
        }
        return jsonify(response)


if __name__ == '__main__':
    app.run()
