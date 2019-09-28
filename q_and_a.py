# import pprint
import pymagnitude


class QandAHandler:


    def __init__(self):
        self.q_and_as = [
            {'question': '''Following a C3-C7 laminoplasty in a myelopathic
             patient with cervical stenosis, the most common neurologic
             complication would manifest with which of the following new
             postoperative exam findings?''',
             'keywords': [['bicep'], ['weakness']],
             'answer': 'Bicep weakness'},
            
            {'question': '''Which variables has the strongest
            association with poor clinical outcomes in patients who undergo
            expansive laminoplasty for cervical spondylotic myelopathy?''',
             'keywords': [['angle'], ['small', 'few', '13', 'degrees'],
                          ['kyphosis']],
             'answer': 'Local kyphosis angle > 13 degrees'},

            {'question': '''Which classification system for cervical myelopathy
            focuses exclusively on lower extremity function?''',
             'keywords': [['nurick']],
             'answer': 'Nurick'},

            {'question': '''Motor-dominant radiculopathy with weakness of the
            deltoid''',
             'keywords': [['motor'], ['radiculopathy'], ['weak'], ['deltoid']]}
        ]

        self.q_index = 0
        self.wv = pymagnitude.Magnitude('../wiki-news-300d-1M-subword.magnitude')


    def supply_question(self):
        return self.q_and_as[self.q_index]['question']


    def evaluate_response(self, response):
        keywords = self.q_and_as[self.q_index]['keywords']
        answer = self.q_and_as[self.q_index]['answer']

        scores = []
        for kw_group in keywords:
            top_score = -1

            for kw in kw_group:
                response_words = response.lower().split()
                top_score = max(self.wv.similarity(kw, response_words))

            scores.append(top_score)

        score = sum(scores) / len(scores)
        low_score_kw = [keywords[i][0] for i in range(len(scores))
                        if scores[i] < 0.6]

        self.q_index = 0 if self.q_index == len(self.q_and_as) else self.q_index + 1

        if score > 0.75:
            return 'You got it, good job!'

        if score > 0.5:
            return f"""You're getting there, but you forgot to mention these
keywords: {low_score_kw}.
The correct answer is: {answer}"""

        return f'Sorry, the correct answer is: {answer}'


def main():
    handler = QandAHandler()
    print(handler.supply_question())
    response = input('Answer: ')
    print(handler.evaluate_response(response))


if __name__ == '__main__':
    main()
