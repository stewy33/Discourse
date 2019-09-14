from flask import Flask, request, make_response, jsonify
import sys


app = Flask(__name__)


def q_and_a():
    q_and_a = [
        {'question':
         '''What is the name of:
         The number of protons of each atom in the element?''',

         'answers': ['atomic number']},

        {'question':
         '''6.02 times 10 to the 23rd particles is equal to:''',

         'answers': ['mole']},

        {'question':
         '''What is the name for the transition from a solid to a gas?''',

         'answers': ['sublimation']}
    ]

    return 'Hi'


def dflow_response():
    req = request.get_json(force=True)

    print(req['queryResult'])

    action = req['queryResult']['action']


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
