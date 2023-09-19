from tkinter import *
import pandas
from random import randint

LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# --------------- get french and display english one -----------------
try:
    word_learning_file = pandas.read_csv("data/new_words_to_learn.csv")
except FileNotFoundError:
    word_learning_file = pandas.read_csv("data/french_words.csv")

word_data = word_learning_file.to_dict(orient="records")
random_index = 0


def delete_word():
    global random_index, word_data
    if len(word_data) == 1:
        return
    word_data.remove(word_data[random_index])
    save_data = pandas.DataFrame(word_data)
    save_data.to_csv("data/new_words_to_learn.csv", index=False)
    get_french()


def get_french():
    global random_index, flip_timer, word_data
    if len(word_data) == 1:
        return
    window.after_cancel(flip_timer)
    random_index = randint(0, len(word_data)-1)
    french_word = word_data[random_index]["French"]
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language_text, text="Francais", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    flip_timer = window.after(3000, func=get_english)


def get_english():
    global random_index
    english_word = word_data[random_index]["English"]
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(word_text, text=english_word, fill="Gray75")
    canvas.itemconfig(language_text, text="English", fill="Gray75")


# -------------------------- G I U ---------------------------
window = Tk()
window.config(padx=50, pady=50, bg="#b1ddc6")
flip_timer = window.after(3000, func=get_english)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg="#b1ddc6")
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_back)
canvas.grid(column=0, row=0, columnspan=2)

language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)

right_image = PhotoImage(file="images/right.png")
button_check = Button(text="reset", highlightthickness=0, command=delete_word, image=right_image)
button_check.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(text="reset", highlightthickness=0, command=get_french, image=wrong_image)
button_wrong.grid(column=0, row=1)

get_french()
window.mainloop()
