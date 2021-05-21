class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        curr_question = self.question_list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Q{self.question_num}: {curr_question.question} (True/False)?: ")
        self.check_answer(user_ans,curr_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            print("\tYou got that right!")
            self.score += 1
        else:
            print("\tOops! Wrong answer")
        print(f"\tThe Correct answer is {correct_ans}")
        print(f"\tYou score is: {self.score}/{self.question_num}")

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def final_score(self):
        print(f"You've Completed you quiz")
        print(f"Your final score is: {self.score}/{self.question_num}")