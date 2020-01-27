"""
Wordlist generator.
To be used with the password cracker.

Made by Leander Thorkildsen and Theodor Fossum
"""


import sys
import getopt
import os
import time
import itertools



def usage():
    print("\nCommand Line Arguments:")
    print("    -o    Output file (passwordlist)")
    print("    -n    Med nummer")
    print("    -p    Print output")
    print("    -h    Display this message")
    print("\n")



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
    f = open(output_fp, "a")
    for word in passwordlist:
        f.write("{}\n".format(word))
    f.close()

    if print_output:
        for password in passwordlist:        
            print password
    
    end_time = time.time()
    delay = round((end_time - start_time))
    length = length + len(passwordlist)
    print length, "passwords created in", delay, "Seconds"




def legg_til_nummer(passwordlist):
    newpasswordlist = []
    for word in passwordlist:
        newpasswordlist.append(word+str(123))
        newpasswordlist.append(word+str(1234))
        newpasswordlist.append(word+str(1337))
        newpasswordlist.append(word+str(321))
        newpasswordlist.append(word+str(4321))
        newpasswordlist.append(word+str(123456789))
        newpasswordlist.append(word+str(1990))
        newpasswordlist.append(word+str(1991))
        newpasswordlist.append(word+str(1992))
        newpasswordlist.append(word+str(1993))
        newpasswordlist.append(word+str(1994))
        newpasswordlist.append(word+str(1995))
        newpasswordlist.append(word+str(1996))
        for tall in range(0, 100):
            newpasswordlist.append(word+str(tall))

    return newpasswordlist



def generate_passwords(output_fp, length):
    passwordlist = []
    charset = "abcdefghijklmnopqrstuvwxyz"
    charset_reverse = "zyxwvutsrqponmlkjihgfedcba"
    for i in range(1, 4):
        for attempt in itertools.product(charset, repeat=i):
            password = "".join(attempt)
            passwordlist.append(password)

    #output_passwordlist(passwordlist, output_fp, length)

    if med_nummer:
        passwordlist_nummer = legg_til_nummer(passwordlist)
        output_passwordlist(passwordlist_nummer, output_fp, length)



if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:i:o:t:np')
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    start_time = time.time()


    # default
    output_fp = "passwordlist.txt"
    med_nummer = False
    print_output = False
    length = 0


    for opt, arg in opts:
        if opt in ("-h"):
            usage()
            sys.exit(1)
        elif opt in ("-o"):
            output_fp = arg
        elif opt in ("-n"):
            med_nummer = True
        elif opt in ("-p"):
            print_output = True
        else:
            print("Invalid argument {}".format(opt))

    try:
        generate_passwords(output_fp, length)
        count_passwords(output_fp)
    except Exception as e:
        print "Oh no, something went wrong."
        print(e)
        usage()
        sys.exit(1)




