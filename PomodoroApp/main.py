from tkinter import *
import math

# ----------------- Constants ---------------------#
BACKGROUND_COLOUR = "#f9c6b9"
BUTTON_COLOUR = "#9ddfd3"
TEXT_COLOUR = "#de2e44"

FONT = "Courier"

BACKGROUND_IMAGE = "tomato.png"

CODE_DURATION = 1  # * 60
BREAK_DURATION = 1  # * 60
LONG_BREAK_DURATION = 1  # * 60

# Check total reps
reps = 1
# Current Timer Variable
curr_timer = None  # Keep track of the after running, to cancel on reset
timer_running = False  # This is to check if there already is a timer running

# ------------------- Screen Config ----------------------#
# Configure screen
window = Tk()
window.config(padx=50, pady=50)
window.title("Pomodoro App")
window.config(bg=BACKGROUND_COLOUR)
window.geometry("600x500")
window.resizable(False, True)


# ------------------- Timer Config & Functions ----------------------#

# Produce Tick
def add_tick():
    tick = tick_mark_label["text"] + "✓"
    tick_mark_label["text"] = tick


# Resets the whole thing!
def reset():
    global timer_running
    timer_running = False
    canvas.after_cancel(curr_timer)
    to_do["text"] = "Timer!"
    tick_mark_label["text"] = ""
    canvas.itemconfig(timer_label, text="00:00")
    global reps
    reps = 1


# Start The timer by button
def start_timer():
    global timer_running, reps
    if timer_running:
        return
    timer_running = True

    if reps == 8:
        add_tick()
        countdown(LONG_BREAK_DURATION)
        to_do["text"] = "Long Break!"
    elif reps % 2 == 1:
        countdown(CODE_DURATION)
        to_do["text"] = "Code!"
    elif reps % 2 == 0:
        countdown(BREAK_DURATION)
        to_do["text"] = "Break!"
        add_tick()

    reps += 1


# Start Count Down
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    time_format = "{}:{}".format(minutes, seconds)

    canvas.itemconfig(timer_label, text=time_format)

    if count >= 0:
        global curr_timer
        curr_timer = canvas.after(1000, countdown, count - 1)
    elif reps == 9:
        reset()
    else:
        global timer_running
        timer_running = False
        start_timer()
    # This after method in canvas is time delay method
    # it calls the specified function with it's arguments next to it, with a delay of specified
    # millisecond  on parallel listening to other events or without interrupting the program


# ------------------- UI Config ----------------------#

# Set To Do Text
to_do = Label(text="Timer", bg=BACKGROUND_COLOUR, font=(FONT, 40, "bold"))
to_do.config(foreground=TEXT_COLOUR)
to_do.grid(row=1, column=2)

# Set Start Button
start_button = Button(text="Start", padx=5, pady=3, width=10, command=start_timer)
start_button.config(bg=BUTTON_COLOUR, foreground=TEXT_COLOUR, borderwidth=0)
start_button.grid(row=3, column=1, sticky="S")

# Set Reset Button
reset_button = Button(text="Reset", padx=5, pady=3, command=reset)
reset_button.config(width=10, borderwidth=0, bg=BUTTON_COLOUR, foreground=TEXT_COLOUR)
reset_button.grid(row=3, column=3, sticky="S")

# Set Tick mark
tick_mark_label = Label(fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR, font=(FONT, 13, "bold"))
tick_mark_label.grid(row=3, column=2, sticky="S")

# Create Canvas
tomato_img = PhotoImage(file=BACKGROUND_IMAGE)
canvas = Canvas(width=264, height=256, highlightthickness=0, bg=BACKGROUND_COLOUR)
# Set Image Canvas
canvas.create_image(132, 128, image=tomato_img)
# Set Timer Canvas
timer_label = canvas.create_text(137, 145, text="00:00", fill="white", font=(FONT, 30, "bold"))
canvas.grid(row=2, column=2)

# Configure the grid, to position it in the center
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(3, weight=1)

window.mainloop()
