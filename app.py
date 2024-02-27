from flask import Flask, render_template, request, jsonify
from chat import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input_stmt = msg
    return get_chat_response(input_stmt)


if __name__ == '__main__':
    app.run()
