"""
Wordlist shaver. Removes duplicates, and only includes passwords up to 8 characters.

Made by Leander Thorkildsen and Theodor Fossum
"""


import sys
import getopt
import os
import time
import string



def usage():
    print("\nCommand Line Arguments:")
    print("    -i    Input file (wordlist)")
    print("    -o    Output file (passwordlist)")
    print("    -h    Display this message")
    print("\n")


def get_wordlist(wordlist_fp):
    try:
        with open(wordlist_fp, "r") as f:
            wordlist = f.read()
    except OSError as e:
        if e.errno == ENOENT:
            print "Error: File not found"
        if e.errno == EPERM:
            print "Eroor: Permission denied"

    return wordlist



def count_passwords(output_fp):
    try:
        with open(output_fp, "r") as f:
            wordlist = f.read()
    except OSError as e:
        if e.errno == ENOENT:
            print "Error: File not found"
        if e.errno == EPERM:
            print "Eroor: Permission denied"

    
    passwordlist = wordlist.split('\n')
    print "Total passwords:", len(passwordlist)



def output_passwordlist(passwordlist, output_fp, length):
    passwordlist = sorted(set(passwordlist), key=lambda x:passwordlist.index(x))

    f = open(output_fp, "a")
    for word in passwordlist:
        f.write("{}\n".format(word))
    f.close()

    
    end_time = time.time()
    delay = int((end_time - start_time))
    length = length + len(passwordlist)
    print length, "passwords created in", delay, "Seconds"



def shave_passwords(input_fp, output_fp, length):
    data = get_wordlist(input_fp)
    wordlist = data.split('\n')
    del wordlist[-1]

    passwordlist = []
    for word in wordlist:
        if len(word) < 9:
            passwordlist.append(word)

    output_passwordlist(passwordlist, output_fp, length)



if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:i:o:')
    except getopt.GetoptError:
        print "Getopt error."
        usage()
        sys.exit(1)

    start_time = time.time()


    # default
    input_fp = "wordlist.txt"
    output_fp = "passwordlist.txt"
    length = 0


    for opt, arg in opts:
        if opt in ("-h"):
            usage()
            sys.exit(1)
        elif opt in ("-i"):
            input_fp = arg
        elif opt in ("-o"):
            output_fp = arg
        else:
            print("Invalid argument {}".format(opt))

    try:
        shave_passwords(input_fp, output_fp, length)
        count_passwords(output_fp)
    except Exception as e:
        print "Oh no, something went wrong."
        print(e)
        usage()
        sys.exit(1)




