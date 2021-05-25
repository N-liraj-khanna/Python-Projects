import random

import pandas
from tkinter import *

# ---------------------- Constants & Global Variables ---------------------- #
FONT = "Helvetica"
TITLE_SIZE = 30
WORD_SIZE = 60
BACKGROUND_COLOR = "#b1ddc6"
data = ""  # Variable being parsed as a DataFrame from csv (Initializing)

# ---------------------- Read Words from CSV ---------------------- #
# Read from CSV
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/words.csv")
finally:
    jap_words = pandas.DataFrame.to_dict(data, 'records')
# Convert everything to dictionary in 'records' orientation

# ---------------------- Screen Config ---------------------- #
window = Tk()
window.title(130 * " " + "Flashy")
window.config(bg=BACKGROUND_COLOR, padx=40, pady=40)
logo = PhotoImage(file="images/logo.png")
window.iconphoto(False, logo)


# ---------------------- Words Config on Card ---------------------- #
def correct_func():
    global jap_words, curr_timer

    window.after_cancel(curr_timer)  # cancels the the current timer
    # if clicked on next question, the previous timer(after) should be shutdown

    curr_word = set_jap_words()
    # delete the current word if correct
    jap_words.remove(curr_word)

    words_data = pandas.DataFrame(jap_words)
    words_data.to_csv("data/words_to_learn.csv", index=False)

    curr_timer = window.after(3000, set_eng_words, curr_word)


def wrong_func():
    global curr_timer
    window.after_cancel(curr_timer)

    # don't delete the current word on correct
    curr_word = set_jap_words()
    curr_timer = window.after(3000, set_eng_words, curr_word)


def set_jap_words():  # used to set a japanese word on the current card
    random_word = random.choice(jap_words)
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(canvas_title, text="Japanese")
    canvas.itemconfig(canvas_word, text=random_word['japanese'])
    return random_word


def set_eng_words(curr_word):  # used to set a english word on the current card
    canvas.itemconfig(canvas_title, text="English")
    canvas.itemconfig(canvas_word, text=curr_word['english'])
    canvas.itemconfig(canvas_image, image=back_card)


# ---------------------- UI Config ---------------------- #

# Open Images
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")

# About Cards and Words Config
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas_image = canvas.create_image(400, 263, anchor="center", image=front_card)
canvas_title = canvas.create_text(400, 150, text="Japanese", font=(FONT, TITLE_SIZE, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=(FONT, WORD_SIZE, "bold"))

# setting a random japanese word at start of program
start_word = set_jap_words()
curr_timer = window.after(3000, set_eng_words, start_word)

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

correct = Button(image=correct_img, bg=BACKGROUND_COLOR, borderwidth=0, command=correct_func)
correct.grid(row=1, column=0, sticky="N")
wrong = Button(image=wrong_img, bg=BACKGROUND_COLOR, borderwidth=0, command=wrong_func)
wrong.grid(row=1, column=1, sticky="N")

# Continue Listening
window.mainloop()
