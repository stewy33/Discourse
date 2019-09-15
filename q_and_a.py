import random
import pprint
import requests
import json
import numpy as np

def read_word_vecs():
    with open('../wiki-news-300d-1M-subword.vec', 'r', encoding='utf-8',
              newline='\n', errors='ignore') as fin:
        _, _ = map(int, fin.readline().split())

        word_vecs = {}
        for line in fin:
            tokens = line.rstrip().split(' ')
            vec = np.array(list(map(float, tokens[1:])))
            word_vecs[tokens[0]] = vec / np.linalg.norm(vec)

    return word_vecs


class QandAHandler:


    def __init__(self, word_vecs=None):
        self.q_and_as = [
            {'question': 'What does it mean for a problem to be in class p?',
             'keywords': [['polynomial']],
             'answer': '''If a problem is in class p, there exists a polynomial
time algorithm to solve it.'''},

            {'question': 'What is a classifier?',
             'keywords': [['class', 'category']],
             'answer': '''A classifier classifies inputs into distinct
categories.'''},

            {'question': 'What is a hash table?',
             'keywords': [['hash', 'map'], ['key', 'index']],
             'answer': '''A hash table is a data structure that hashes keys to
integers which are used to efficiently index an internal array.'''},

            {'question': 'What is a binary tree?',
             'keywords': [['two'], ['children', 'subtree']],
             'answer': '''A binary tree is a tree where every node has at most
two children.'''}
        ]

        self.last_q_and_a = None

        if word_vecs:
            self.word_vecs = word_vecs
        else:
            self.word_vecs = read_word_vecs()


    def similarity(self, w1, w2):
        if w1 not in self.word_vecs or w2 not in self.word_vecs:
            return 0

        return np.dot(self.word_vecs[w1], self.word_vecs[w2])


    def supply_question(self):
        #self.last_q_and_a = random.choice(self.q_and_as)
        self.last_q_and_a = self.q_and_as[1]
        return self.last_q_and_a['question']


    def evaluate_response(self, response):
        keywords = self.last_q_and_a['keywords']

        scores = []
        for kw_group in keywords:
            top_score = -1

            for kw in kw_group:
                for rw in response.lower().split():
                    top_score = max(top_score, self.similarity(kw, rw))

            scores.append(top_score)

        score = sum(scores) / len(scores)

        if score > 0.75:
            return f'You got it - score: {score}'

        return f'Sorry, the correct answer is: {keywords} - score: {score}'


def main():
    handler = QandAHandler()
    print(handler.supply_question())
    response = input('Answer: ')
    print(handler.evaluate_response(response))


if __name__ == '__main__':
    main()
