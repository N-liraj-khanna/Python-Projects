import html


class QuizManager:
    def __init__(self, questions_list):
        self.all_questions = questions_list
        self.score = 0
        self.curr_question_num = 0

    def next_question(self):
        question_data = self.all_questions[self.curr_question_num].question
        question_data = html.unescape(question_data)

        return f"Q{self.curr_question_num + 1}. {question_data} (True/False)\n"

    def check_answer(self, ans):
        answer_data = self.all_questions[self.curr_question_num].answer
        self.curr_question_num += 1

        if ans == answer_data:
            self.score += 1
            return True
        else:
            return False

    def still_has_questions(self):
        return self.curr_question_num < len(self.all_questions)
