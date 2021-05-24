import json
import string
import random
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import pyperclip

# --------------- Functionalities  -----------------#
# Checks if you've entered every field, it prompts a dialogue box if you didn't
# Confirms if you want to save in the file on Add Button
# On generating passwords or on Typing passwords(after it got added in the file)
# it will save the password to your clipboard, using pyperclip module
# Adds each website name, email & passwords with three pipe symbols in b/w
# (just incase to avoid confusion of getting pip symbol on the password itself)
# confirms if there already exits a file names passwords if not create it with FileNotFoundError
# also if exists a file with no data in it, it handles the exception with JSONDecodeError
# Others are easily understandable
# --------------- Constants & Global Variables -----------------#
FONT = "Helvetica"
FONT_SIZE = 13
BACKGROUND_COLOUR = "#393e46"

# --------------- Screen Config -----------------#

window = Tk()
# window.minsize(500, 500)
window.config(padx=100, pady=50, bg=BACKGROUND_COLOUR)
window.title("Password Manager")

photo = PhotoImage(file="logo.png")
window.iconphoto(False, photo)


# --------------- Search Function -----------------#
def search_data():
    title = ""  # Initializing
    message = ""

    try:  # make the whole data in file as a json object ( is exist a file or data in it)
        with open("passwords.json") as data_file:
            data_json = json.load(data_file)
    except FileNotFoundError:  # if there's no file found
        message = "No data File Found"
    except JSONDecodeError:  # if there's no data in the file(like nothing literally)
        message = "There's is no Data in the file"
    else:
        website = website_entry.get().title()
        if website in data_json:  # saves the title and message if the given data is present in the file

            email = data_json[website]['email']
            password = data_json[website]['password']

            title = website
            message = f"Your Details:\nEmail: {email}\nPassword: {password}"
    finally:
        if title == "":  # if the data given is not present in the file
            title = "Error"
        if message == "":
            message = "No such Data exist!"

        messagebox.showinfo(title=title, message=message)


# --------------- Save Function -----------------#

def print_message(entry):
    messagebox.showinfo(title="Oops", message=f"Please don't leave {entry} field Empty!")


def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    if website == "":
        print_message("website")
    elif email == "":
        print_message("email")
    elif password == "":
        print_message("password")
    else:
        message = f"Details entered: \nEmail:    {email}\nPassword:    {password}\n" \
                  f"Do you wish to save?"
        is_ok = messagebox.askyesnocancel(title=website, message=message)

        if is_ok:
            pyperclip.copy(password)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

            save_password = {
                website: {
                    "email": email,
                    "password": password
                }
            }
            try:  # Checking if there's any JSONDecodeError(if there's data to be loaded or updated)
                with open("passwords.json", "r") as data_file:
                    # Loading previous data
                    data = json.load(data_file)
            except FileNotFoundError:
                # if there's no data/file then have to create using the current data
                # Making the file on write mode
                with open("passwords.json", "w") as data_file:
                    # Writing the whole data
                    json.dump(save_password, data_file, indent=4)
            except JSONDecodeError:
                # this is to ensure that there's some data in the file, if not then create the damn file
                with open("passwords.json", "w") as data_file:
                    # Writing the whole data
                    json.dump(save_password, data_file, indent=4)
            else:  # if no error go ahead and execute
                with open("passwords.json", "w") as data_file:
                    # Updating new data
                    data.update(save_password)
                    # dumping the old data with the new data to the file
                    json.dump(data, data_file, indent=4)
            finally:  # executes this no matter what
                email_entry.delete(0, END)
                email_entry.insert(0, "yourDefaultEmail@mail.com")


# --------------- Password & Clipboard Functions -----------------#
def password_generator():
    # Random sample(returns list of random values from given list of given size)
    # String printable(returns all letters, numbers & symbols, with whitespaces)
    # Strip() removes all whitespaces and lines from the given list
    # "".join(random.sample(list(string.printable.strip()), 16))

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "~`!@#$%^&*()-+={[}]|:\;\"'<,>.?/"
    password = list(letters + numbers + symbols)

    return "".join(random.sample(password, 16))


# Get the password and set in entry
def generate():
    password = password_generator()
    pyperclip.copy(password)  # Copies to clipboard
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# --------------- UI Config -----------------#

# Logo
canvas = Canvas(window, width=300, height=300, bg=BACKGROUND_COLOUR, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website: ", font=(FONT, FONT_SIZE))
website_label.config(fg="white", bg=BACKGROUND_COLOUR)
website_label.grid(row=1, column=0)

email_label = Label(text="Username/Email: ", font=(FONT, FONT_SIZE))
email_label.config(fg="white", bg=BACKGROUND_COLOUR)
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=(FONT, FONT_SIZE))
password_label.config(fg="white", bg=BACKGROUND_COLOUR)
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="N", ipady=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2, sticky="N")
# default mail
email_entry.insert(0, "yourDefaultEmail@mail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="N", ipady=1)

# Buttons
search_button = Button(text="Search", borderwidth=0.3, width=15, pady=1, command=search_data)
search_button.grid(row=1, column=2, sticky="NE")

generate_button = Button(text="Generate Password", borderwidth=0.5, width=15, command=generate)
generate_button.grid(row=3, column=2, sticky="NE")

add_button = Button(text="Add", width=34, borderwidth=0.5, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="S")

# Continue listening
window.mainloop()
