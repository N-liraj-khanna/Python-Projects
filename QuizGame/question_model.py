class QuestionModel:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def print_val(self):
        print(self.question, self.answer)
