import time
from tkinter import *

from quiz_manager import QuizManager

BACKGROUND_COLOR = "#98ddca"


class GUI:
    def __init__(self, quiz_manager: QuizManager):
        # getting the manager object
        self.quiz_brain = quiz_manager

        # Window Config
        self.window = Tk()

        self.window.minsize(height=500, width=350)
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        # Score Label
        self.score_label = Label(text="Score: 0", font=("Verdana", 10, "normal"), bg=BACKGROUND_COLOR)
        self.score_label.grid(row=0, column=0, sticky="")

        # Canvas Config
        self.canvas = Canvas(self.window, height=250, width=250)
        self.question_text_in_canvas = self.canvas.create_text(
            125, 125, font=("Verdana", 13, "bold"), width=200)
        self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2)

        # Buttons Config

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(self.window, image=self.true_image, command=self.true)
        self.false_button = Button(self.window, image=self.false_image, command=self.false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.window.grid_rowconfigure(1, pad=50)

        # Continue Listening
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self.canvas.itemconfig(self.question_text_in_canvas, text=self.quiz_brain.next_question())
        else:
            self.canvas.itemconfig(self.question_text_in_canvas, text="You've Reached the end of the Quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false(self):
        ans = self.quiz_brain.check_answer("False")
        self.animation(ans)

    def true(self):
        ans = self.quiz_brain.check_answer("True")
        self.animation(ans)

    def animation(self, ans):
        if ans:
            color = "green"
        else:
            color = "red"
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)
