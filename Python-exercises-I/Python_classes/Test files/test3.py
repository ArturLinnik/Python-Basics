
from tkinter import *
import time

######################
import shelve

score = 150

d = shelve.open('score.txt')
d['score'] = score
d.close()
######################

def set_time(hours, minutes, seconds):
    my_hours = hours
    my_minutes = minutes
    my_seconds = seconds
    return "{}:{}:{}".format(my_hours, my_minutes, my_seconds)

print(set_time("01", "00", "00"))
