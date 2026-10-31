# This program is an example
import time
import os

numfiles = len(os.listdir("data"))

file = open("res/time.txt", "w")
file.write(f"The program was last run at {time.ctime()}\n")
file.write(f"There are {numfiles} file(s) in the data folder")
file.close()
