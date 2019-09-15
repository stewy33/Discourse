import random
import pprint
import requests
import json
import numpy as np

class QandAHandler:


    def __init__(self):
        self.q_and_as = [
            {'question': 'What kind of fluid is normal saline?',
             'keywords': ['crystalloid fluid']},

            {'question': 'What is the function of chlorophyll?',
             'keywords': ['photosynthesis', 'energy', 'glucose']}
        ]

        self.last_q_and_a = None


    def supply_question(self):
        #self.last_q_and_a = random.choice(self.q_and_as)
        self.last_q_and_a = self.q_and_as[1]
        return self.last_q_and_a['question']


    def evaluate_response(self, response):
        question = self.last_q_and_a['question']
        keywords = self.last_q_and_a['keywords']

        return 'response not evaluated yet'

        url = 'https://api.msturing.org/gen/encode'
        headers = {'Ocp-Apim-Subscription-Key':
                   '04414dcfaf7c43a4b918e5c14a8bfd0c'}

        payload = json.dumps({'queries': keywords})

        req_k = requests.post(url, headers=headers, data=payload).json()
        print(req_k)
        for i in range(len(req_k)):
            q = req_k[i]
            v = np.array(q['vector'])
            req_k[i]['vector'] = v / np.linalg.norm(v)


        response_grams = []
        qsplit = question.split(' ')
        for i in range(0, len(qsplit) - 4, 2):
            response_grams.append(' '.join(qsplit[i:i+4]))
        payload = json.dumps({'queries': response_grams})

        req_r = requests.post(url, headers=headers, data=payload).json()
        for i in range(len(req_r)):
            q = req_r[i]
            v = np.array(q['vector'])
            req_r[i]['vector'] = v / np.linalg.norm(v)

        scores = []
        for q_k in req_k:
            top_score = -1
            for q_r in req_r:
                top_score = max(top_score, np.dot(q_k['vector'], q_r['vector']))
            scores.append(top_score)


        print(scores)
        score = sum(scores) / len(scores)

        if score > 0.7:
            return f'You got it - score: {score}'

        return f'Sorry, the correct answer is: {keywords} - score: {score}'


def main():
    handler = QandAHandler()
    print(handler.supply_question())
    response = input('Answer: ')
    print(handler.evaluate_response(response))


if __name__ == '__main__':
    main()
