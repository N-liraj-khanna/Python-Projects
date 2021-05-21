from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(QuestionModel(question['question'], question['correct_answer']))

# print(question_bank)
brain = QuizBrain(question_bank)
while brain.still_has_questions():
    brain.next_question()

brain.final_score()