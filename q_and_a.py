import random
import gensim.downloader
import pprint

class QandAHandler:


    def __init__(self, model=None):
        self.q_and_ks = [
            {'question':
             '6.02 times 10 to the 23rd particles is equal to:',

             'keywords': ['mole']},

            {'question':
             '''What is the name for the transition from a solid to a gas?''',

             'keywords': ['sublimation']},

            {'question':
             'How are photosystems involved in photosynthesis?',

             'keywords': ['chlorophyll', 'absorption', 'photon', 'excite']}
        ]

        self.last_q_and_ks = None

        self.model = model
        if self.model is None:
            pass
            #self.model = gensim.downloader.load('glove-twitter-25')


    def supply_question(self):
        self.last_q_and_ks = random.choice(self.q_and_ks)
        return self.last_q_and_ks['question']


    def evaluate_response(self, response):
        keywords = self.last_q_and_ks['keywords']

        score = 0
        for kw in keywords:
            #if kw not in self.model.wv.vocab:
            #    break

            kw_match = 0
            for rw in response.split(' '):
                #if rw not in self.model.wv.vocab:
                #    break

                kw_match = max(kw_match, kw == rw)#self.model.wv.similarity(kw, rw))

            print(f'keyword: {kw}, response: {response}, score: {kw_match}')
            score += kw_match

        if score / len(keywords) > 0.9:
            return 'You got it - score: {score}'

        return f'Sorry, the correct answer is: {self.last_q_and_ks["keywords"][0]} - score: {score}'


def main():
    handler = QandAHandler()
    print(handler.supply_question())
    response = input('Answer: ')
    print(handler.evaluate_response(response))


if __name__ == '__main__':
    main()
