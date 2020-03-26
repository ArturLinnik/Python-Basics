
# List all files in a directory in Python

from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('/home/artur/Downloads') if isfile(join('/home/artur/Downloads', f))]

print(files_list)












