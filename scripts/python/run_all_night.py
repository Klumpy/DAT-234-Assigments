"""
Script to run brute-force all night,
by restarting the script if it crashes (which it actually does alot)
"""

import os

print "Running all night"


progress = 0 
length = 12000 #length of passwordlist


def get_progress():
    with open("progress.txt", "r") as f:
        progresslist = f.read()
    progress = progresslist.split("\n")
    del progress[-1]
    progress_as_int = [int(i) for i in progress]
    last = progress_as_int[-1]
    return last    


while progress < length:
    progress = get_progress()
    try:
        os.system("python brute_from_save.py -i passwordlist.txt")
    except:
        pass

