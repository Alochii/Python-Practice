from tkinter import *
window = Tk()
window.title("Unit converter")
window.minsize(width=250, height=200)
window.config(padx=50,pady=50)
label_mile = Label(text="miles")
label_mile.grid(column=3,row=2)

label_km = Label(text="km")
label_km.grid(column=3,row=1)

label_miles = Label(text="0")
label_miles.grid(column=2,row=2)

label_equal_to = Label(text="is equal to")
label_equal_to.grid(column=1,row=2)

input = Entry(width = 10)
input.grid(column=2,row=1)
def clickbutton():
    kilos = int(input.get())
    miles = round((kilos / 1.56),2)
    label_miles.config(text=miles)
button = Button(text="convert",command=clickbutton)
button.grid(column=2,row=3)

window.mainloop()