from question_model import Question
from quiz_manager import QuizManager
from tkinter import *
from gui import GUI
import requests

# ---------------- Constants & Global Variables ----------------#
all_questions = []

# ---------------- Data From API ----------------#
# Get Data from API
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()  # check for any error

# Convert the data as Question object and push it to a list
for data in response.json()['results']:
    new_question = Question(data['question'], data['correct_answer'])
    all_questions.append(new_question)

quiz_manager = QuizManager(all_questions)

# ---------------- UI Config ----------------#
gui = GUI(quiz_manager)

