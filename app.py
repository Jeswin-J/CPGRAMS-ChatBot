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
    print("$$$$$$$$$$$", get_chat_response(input_stmt))
    response = {
        "chat_response": get_chat_response(input_stmt)
    }
    return get_chat_response(input_stmt)


#
# @app.route("/get_response", methods=["GET", "POST"])
# def get_chat_response():
#     msg = request.form["msg"]
#     input_stmt = msg
#     response = {
#         "chat_response" : get_chat_response(input_stmt)
#     }
#     return response


if __name__ == '__main__':
    app.run()
