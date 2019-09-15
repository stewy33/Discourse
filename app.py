import pprint
from flask import Flask, request, make_response, jsonify
from q_and_a import QandAHandler


app = Flask(__name__)
handler = QandAHandler()
pp = pprint.PrettyPrinter()


def dflow_response():
    req = request.get_json(force=True)

    pp.pprint(req)

    action = req['queryResult']['intent']['displayName']
    
    if action == 'Ask Question Intent':
        fulfill_text = handler.supply_question()

    elif action == 'Evaluate Response':
        user_input = req['queryResult']['queryText']
        fulfill_text = handler.evaluate_response(user_input)

    elif action == 'test intent':
        fulfill_text = 'hi'

    print(fulfill_text)

    return {
        "fulfillmentText": fulfill_text,
        "payload": {
            "google": {
                "expectUserResponse": 'true',
                "richResponse": {
                    "items": [{
                        "simpleResponse": {
                            "textToSpeech": fulfill_text
                            }
                        }]
                }
            }
        }
    }


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
