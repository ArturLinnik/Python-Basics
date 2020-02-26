
from tkinter import *   # Imports all the files from the package tkinter
import shelve

# Function that creates a 1 hour timer.
def start_timer():
    global hours, minutes, seconds, run_timer # Global is to be able to use those
    global hours_programming                  # initialized variables in the function.

    seconds -= 1
    label["text"] = "{}:{}:{}".format(hours, # Changes the text of the label
        minutes, seconds)                    # dinamically.

    label3["text"] = hours_programming  # Shows the hours you have programmed

    # How timer works
    if seconds == 0:
        seconds = 60
        minutes -= 1
    elif hours == 0 and minutes == 0 and seconds == 0:  # When timer ends...
        run_timer = False

    # If run_timer is True it calls this function every 1000 milliseconds
    # until the timer ends.
    if run_timer == True:
        root.after(1000, start_timer)

    # If run_timer is False the timer stops at "00:00:00", your programmed
    # hours increases by 1 and saves it in the "programming_timer" file.
    elif run_timer == False:
        label["text"] = "00:00:00"
        saved_hours = shelve.open('programming_timer.txt')
        hours_programming = saved_hours['programming_timer']
        hours_programming += 1
        saved_hours = shelve.open('programming_timer.txt')
        saved_hours['programming_timer'] = hours_programming
        saved_hours.close()
        label3["text"] = hours_programming

# Root of the graphical interface.
root = Tk()

# Initializing time variables.
hours = 0
minutes = 59
seconds = 60
run_timer = True
hours_programming = 0

# Creates a label which default text is "01:00:00"
label = Label(root, text="01:00:00")
label.grid(row = 0, column = 0)

label2 = Label(root, text="Hours programming:")
label2.grid(row = 2, column = 0)

label3 = Label(root, text="nothing")
label3.grid(row = 2, column = 1)

# Creates a button which text is "Start timer" and that execute the code
# of the "start_timer()" function.
button = Button(root, text="Start timer", command=start_timer)
button.grid(row = 1, column = 0)

# Loops the graphical interface that we can constantly see it.
root.mainloop()
