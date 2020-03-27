
from tkinter import *   # Imports all the files from the package tkinter
import shelve

# Function that creates a 1 hour timer.
def start_timer():
    global hours, minutes, seconds, run_timer # Global is to be able to use those
    global hours_programming                  # initialized variables in the function.

    seconds -= 1
    label["text"] = "{}:{}:{}".format(hours, # Changes the text of the label
        minutes, seconds)                    # dinamically.
    if seconds == 0:
        if hours == 0 and minutes == 0 and seconds == 0:  # When timer ends...
            run_timer = False
        seconds = 60
        minutes -= 1

    if run_timer == True:
        root.after(1000, start_timer)   # Calls this function every 1000
    elif run_timer == False:            # miliseconds until the timer ends.
        label["text"] = "00:00:00"
        print("hours_programming", hours_programming)
        saved_hours = shelve.open('programming_timer.txt')
        hours_programming = saved_hours['programming_timer']
        hours_programming += 1
        print("hours_programming", hours_programming)
        saved_hours = shelve.open('programming_timer.txt')
        saved_hours['programming_timer'] = hours_programming
        saved_hours.close()

        saved_hours = shelve.open('programming_timer.txt')
        hours_programming = saved_hours['programming_timer']
        print("hours_programming", hours_programming)

# Root of the graphical interface.
root = Tk()

# Initializing time variables.
hours = 0
minutes = 0
seconds = 60
run_timer = True
hours_programming = 0

# Creates a label which default text is "01:00:00"
label = Label(root, text="01:00:00")
label.pack()

# Creates a button which text is "Start timer" and that execute the code
# of the "start_timer()" function.
button = Button(root, text="Start timer", command=start_timer)
button.pack()

# Loops the graphical interface that we can constantly see it.
root.mainloop()
