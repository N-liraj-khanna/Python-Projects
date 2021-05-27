import datetime as dt
import smtplib
import pandas
import random

# ------------------ WHAT IT DOES!? ------------------ #
# on running this program on the background like forever, it keeps on check
# today's date and time when it matches a date of some person fro the "birthdays.csv"
# it checks for the time at sharp 12:00 A.M. it sends a random letter as mail from
# the "letter_templates" folder, you can customize your letter, and for the name
# use [NAME], it replaces this with the name specified in .csv file and sends it to
# that person, enter all the details in the .csv file properly, fill our
# login credentials and the network service provider, you can also change the time
# Note: this program follows the 24-Hour Format

# ------------------ Constants & Variables ------------------ #

my_email = "yourEmail@gmail.com"
password = "yourPassword"

birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_data = birthdays_data.to_dict(orient="records")

# ------------------ Functions ------------------ #
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    while True:
        for data in birthdays_data:
            today = dt.datetime.now()
            if data['year'] == today.year and data['month'] == today.month and data['day'] == today.day\
                    and today.time().replace(microsecond=0) == "00:00:00":  # 24-hour format

                # open a random file and make it as a string, to send
                with open(f"letter_templates/letter_{random.choice([1, 2, 3])}.txt") as letter_file:
                    the_letter = letter_file.readlines()
                    the_letter[0] = the_letter[0].replace("[NAME]", data['name'])
                    final_letter = "".join(the_letter)

                    # convert that string into a message of email format
                    final_letter = "Subject: Hey " + data['name'] + "\n\n" + final_letter

                # open connection and provide the necessary details to establish connection
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=data['email'],
                        msg=final_letter
                    )
                print("Messages Sent to -> ", data["email"])
