import random
import pprint

class QandAHandler:


    def __init__(self):
        self.q_and_as = [
            {'question':
             'How are photosystems involved in photosynthesis?',

             'answer': 'Photons excite chlorophyll which produces energy.'}
        ]

        self.last_q_and_a = None


    def supply_question(self):
        self.last_q_and_a = random.choice(self.q_and_as)
        return self.last_q_and_a['question']


    def evaluate_response(self, response):
        answer = self.last_q_and_a['answer']

        score = 1

        if score > 0.9:
            return 'You got it - score: {score}'

        return f'Sorry, the correct answer is: {answer} - score: {score}'


def main():
    handler = QandAHandler()
    print(handler.supply_question())
    response = input('Answer: ')
    print(handler.evaluate_response(response))


if __name__ == '__main__':
    main()
