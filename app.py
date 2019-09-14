from flask import Flask, request, make_response, jsonify
import sys


app = Flask(__name__)
handler = QandAHandler()


def dflow_response():
    req = request.get_json(force=True)

    # handler.supply_question()
    # handler.evaluate_response(response)

    return {'fulfillmentText': 'This is a response from webhook.'}


# Called when dialogflow tries to access our server
@app.route('/dialogflow', methods=['GET', 'POST'])
def dialogflow():
    return make_response(jsonify(dflow_response()))


# Just for testing server is up in browser
@app.route('/')
def index():
    return 'Hi'


if __name__ == '__main__':
    app.run(debug=True)
