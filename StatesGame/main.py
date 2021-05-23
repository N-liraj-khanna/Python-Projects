import turtle
import pandas

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("States Game")
screen.bgcolor("light blue")
screen.addshape(image)
turtle.shape(image)

turtle = turtle.Turtle()
turtle.ht()
turtle.pu()

file = pandas.read_csv("50_states.csv")
all_states = file.state.to_list()

states_finished = 0
guessed_states = []

while states_finished != 50:
    your_state = screen.textinput(f"{states_finished}/50 Guess the state", "What's the next state!?").title()

    if your_state == "Exit":
        break

    if your_state in all_states:
        data = file[file.state == your_state]
        turtle.goto(int(data.x), int(data.y))
        turtle.write(your_state, False, "center", ("Consolas", 10, "italic"))
        states_finished += 1
        guessed_states.append(your_state)

yet_to_guess = {"states": [state for state in all_states if state not in guessed_states]}
print(yet_to_guess)
states_to_learn = pandas.DataFrame(yet_to_guess)

print(states_to_learn)
states_to_learn.to_csv("states_to_learn.csv")
