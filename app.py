from flask import Flask, request, make_response, jsonify
import pprint
import sys


app = Flask(__name__)
pp = pprint.PrettyPrinter()


def dflow_response():
    req = request.get_json(force=True)

    pp.pprint(req)
    #print(req['queryResult'])

    action = req['queryResult']['intent']['displayName']
    
    if action == 'Ask Question Intent':
    	pass
    if action == 'Evaluate Response':
    	pass
   	if action == 'test intent':
   		pass


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
