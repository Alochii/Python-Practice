from tkinter import *
from tkinter import messagebox
import random
import pyperclip

GRAY = "gray75"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    I_password.delete(0, END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    print(nr_letters, nr_symbols, nr_numbers)

    while len(password_list) < nr_letters + nr_symbols + nr_numbers:
        password_list += (char for char in random.choice(letters) if len(password_list) <= nr_letters)
        password_list += (char for char in random.choice(symbols) if len(password_list) <= nr_symbols + nr_letters)
        password_list += (char for char in random.choice(numbers) if
                          len(password_list) <= nr_numbers + nr_symbols + nr_letters)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    I_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_output():
    if len(I_website.get()) == 0 or len(I_password.get()) == 0:
        messagebox.showwarning(title="Missing information error", message="you cannot save an entry with missing data")
    else:
        is_okay = messagebox.askokcancel(title=I_website.get(), message=f"These are the info you added.\n"
                                                                        f"Email : {I_email}\n"
                                                                        f"Password : {I_password}")
        if is_okay:
            with open("data.txt", "a") as file:
                output_text = f"{I_website.get()} | {I_email.get()} | {I_password.get()}\n"
                file.write(output_text)
                I_website.delete(0, END)
                I_password.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=GRAY)

# logo
canvas = Canvas(width=200, height=200, bg=GRAY, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels :

L_website = Label(text="Website:", bg=GRAY)
L_website.grid(column=0, row=1)

L_email = Label(text="Email/Username:", bg=GRAY)
L_email.grid(column=0, row=2)

L_password = Label(text="Password:", bg=GRAY)
L_password.grid(column=0, row=3)

# input boxes

I_website = Entry(width=52)
I_website.grid(column=1, row=1, columnspan=2, sticky=W)
I_website.focus()

I_email = Entry(width=52)
I_email.grid(column=1, row=2, columnspan=2, sticky=W)
I_email.insert(0, "alochii@gmail.com")
I_password = Entry(width=32)
I_password.grid(column=1, row=3, sticky=W)
#
# #button
#
B_generate = Button(text="Generate Password", width=15, command=generate_password)
B_generate.grid(column=2, row=3, sticky=W)

B_add = Button(text="Add", width=44, command=save_output)
B_add.grid(column=1, row=4, columnspan=3, sticky=W)

window.mainloop()
