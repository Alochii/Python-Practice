from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
labeltext = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def stop_timer():
    global reps
    window.after_cancel(timer)
    label_title.config(text="Timer")
    label_checkmark.config(text="")
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global labeltext
    reps += 1
    work_time = WORK_MIN * 60
    rest_time = SHORT_BREAK_MIN * 60
    break_time = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        label_title.config(text="WORK!")
        countdown(work_time)
    elif reps % 8 == 0:
        label_title.config(text="short break")
        labeltext += "✓"
        label_checkmark.config(text=labeltext)
        countdown(break_time)
    else :
        label_title.config(text="long break")
        labeltext += "✓"
        label_checkmark.config(text=labeltext)
        countdown(rest_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    minutes = floor((count/60))
    if minutes < 10 :
        minutes = f"0{minutes}"
    seconds = count % 60
    if seconds < 10 :
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1, countdown, count-1)
    else :
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=2)

label_title = Label(text="Timer",fg=GREEN, font=(FONT_NAME, 40, "bold"))
label_title.grid(column=1, row=1)


button_start = Button(text="start",command=start_timer, highlightthickness=4)
button_start.config(width=10)
button_start.grid(column=0,row=3)

button_reset = Button(text="reset",command=stop_timer, highlightthickness=4)
button_reset.config(width=10)
button_reset.grid(column=2,row=3)

label_checkmark = Label(text="", fg=GREEN, font=(FONT_NAME, 20, "bold"))
label_checkmark.grid(column=1,row=4)

window.mainloop()
