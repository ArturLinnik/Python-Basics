
from tkinter import *

def print_entry():
    label3["text"] = entry2.get()

root = Tk()

label = Label(root, text="Name")
label.grid(row=0, column=0, sticky=W)

entry = Entry(root)
entry.grid(row=0, column=1)

label2 = Label(root, text="Surname")
label2.grid(row=1, column=0, sticky=W)

entry2 = Entry(root)
entry2.grid(row=1, column=1)

label3 = Label(root, text="Result")
label3.grid(row=2, column=0)

button = Button(root, text="Press me", command=print_entry)
button.grid(row=3, column=0)

root.mainloop()
