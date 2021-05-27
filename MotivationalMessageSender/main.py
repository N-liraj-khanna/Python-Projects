# A simple way to send a random quote as mail to an account on the specified time
import datetime as dt
import random
import smtplib

# --------------------- WHAT IT DOES!? ----------------------#
# On running this program like forever in the background
# using the infinite for loop it keeps on check today's date
# with the time, exactly on every monday (if the program keep's running
# in the background it sends some random motivational message at 10.A.M
# You can change the time and day to send, and fill your mail and the
# mail to send with you login details, it works with the mail with less
# secure turned on and should not have any two step authentication and for
# yahoo only the password generated for apps will work and not the normal login password
# Note: this program follows the 24-Hour Format

# Constants & Variables

my_email = "yourEmail@gmail.com"   # Fill em'
to_email = "senderEmail@yahoo.com"
mail_password = "yourMailPassword"

PORT = 587  # PORT is Very important (not working without it)

DAY = 0  # sends a random quote on every monday (0 is Monday in datetime module)
TIME = "10:00:00"  # sends a random quote exactly at 10:00:00 A.M. Monday
# you can set any time you wish for

with open("quotes.txt", encoding="utf8") as quotes_file:
    quotes_list = quotes_file.readlines()

# Function to send random quote as mail on given date
while True:
    now = dt.datetime.now()
    if DAY == now.weekday() and TIME == str(now.time().replace(microsecond=0)):
        with smtplib.SMTP(host="smtp.gmail.com", port=PORT) as smtp_connection:
            smtp_connection.starttls()
            smtp_connection.login(user=my_email, password=mail_password)

            message = f"Subject: Monday Motivation\n\n{random.choice(quotes_list)}"
            smtp_connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
