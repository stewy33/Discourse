import random
import pprint
import requests
import json
import numpy as np

class QandAHandler:


    def __init__(self):
        self.q_and_as = [
            {'question': 'What kind of fluid is normal saline?',
             'answer': 'Normal saline is a crystalloid fluid'}
        ]

        self.last_q_and_a = None


    def supply_question(self):
        self.last_q_and_a = random.choice(self.q_and_as)
        return self.last_q_and_a['question']


    def evaluate_response(self, response):
        answer = self.last_q_and_a['answer']

        url = 'https://api.msturing.org/gen/encode'
        headers = {'Ocp-Apim-Subscription-Key':
                   '04414dcfaf7c43a4b918e5c14a8bfd0c'}
        payload = json.dumps({'queries': [response, answer]})

        req = requests.post(url, headers=headers, data=payload)
        vecs = [np.array(q['vector']) for q in req.json()]
        norm_vecs = [v / np.linalg.norm(v) for v in vecs]
        score = np.dot(norm_vecs[0], norm_vecs[1])

        if score > 0.7:
            return f'You got it - score: {score}'

        return f'Sorry, the correct answer is: {answer} - score: {score}'


def main():
    handler = QandAHandler()
    print(handler.supply_question())
    response = input('Answer: ')
    print(handler.evaluate_response(response))


if __name__ == '__main__':
    main()
