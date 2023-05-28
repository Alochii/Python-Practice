from tkinter import *

window =Tk()

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0,row=0)
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=1,row=1)

button2 = Button(text="Don't Click Me", command=action)
button2.grid(column=2,row=0)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(column=3,row=3)

window.mainloop()
