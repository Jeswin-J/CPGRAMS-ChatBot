from flask import Flask, render_template, request, jsonify
from chat import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get_response", methods=["POST"])
def chat():
    #print("$$$$$$")
    if request.method == "POST":
        input_stmt = ""

        if request.headers["Content-Type"] == "application/json":
            input_stmt = request.json["msg"]
        elif request.headers["Content-Type"] == "application/x-www-form-urlencoded; charset=UTF-8":
            input_stmt = request.form["msg"]
            print(input_stmt)

        response = {
            "chat_msg": input_stmt,
            "chat_response": get_chat_response(input_stmt)
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run()
