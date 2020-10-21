
from tkinter import *
import time

my_hours = 0
my_minutes = 59
my_seconds = 60

print("1 00 00")

while True:
    my_seconds -= 1
    time.sleep(1)
    print("{}:{}:{}".format(my_hours, my_minutes, my_seconds))
    if my_seconds == 0:
        my_seconds = 60
        my_minutes -= 1
    elif my_hours == 0 and my_minutes == 0 and my_seconds == 0:
        break
