import random


class QandAHandler:


    def __init__(self):
        self.q_and_as = [
            {'question':
            '''What is the name of:
The number of protons of each atom in the element?''',

            'answers': ['atomic number']},

            {'question':
             '6.02 times 10 to the 23rd particles is equal to:',

             'answers': ['mole']},

            {'question':
             '''What is the name for the transition from a solid to a gas?''',

             'answers': ['sublimation']}
        ]

        self.last_q_and_a = None


    def supply_question(self):
        self.last_q_and_a = random.choice(self.q_and_as)
        return self.last_q_and_a['question']


    def evaluate_response(self, response):
        if response in self.last_q_and_a['answers']:
            return 'You got it'

        return f'Sorry, the correct answer is: {self.last_q_and_a["answers"][0]}'


def main():
    handler = QandAHandler()
    print(handler.supply_question())
    response = input('Answer: ')
    print(handler.evaluate_response(response))


if __name__ == '__main__':
    main()
