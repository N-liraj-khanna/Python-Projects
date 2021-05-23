from tkinter import *

window = Tk()
# window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

equal_to_label = Label(text="is equal to", padx=10, pady=10, font=("Arial", 11, "bold"))
equal_to_label.grid(column=0, row=1)

input_mile = Entry(width=10)
input_mile.grid(column=1, row=0)

mile_label = Label(text="Miles", padx=10, pady=10, font=("Arial", 12, "bold"))
mile_label.grid(column=2, row=0)

km_value_label = Label(text="0", padx=10, pady=10, font=("Arial", 12, "bold"))
km_value_label.grid(column=1, row=1)

km_label = Label(text="Km", padx=10, pady=10, font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)


def calculate_km():
    mile = input_mile.get()
    km = float(mile) * 1.609
    km_value_label["text"] = round(km)


calculate_button = Button(text="Calculate", padx=3, pady=3, font=("Arial", 11, "bold"))
calculate_button.grid(column=1, row=2)
calculate_button.config(command=calculate_km)

window.mainloop()
