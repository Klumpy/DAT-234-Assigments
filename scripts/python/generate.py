"""
Wordlist generator.
To be used with the password cracker.

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
    print("    -t    Med tegn (ascii.txt)")
    print("    -n    Med nummer")
    print("    -l    Med Leet")
    print("    -m    Mix upper og lower")
    print("    -r    Med reverse")
    print("    -c    Cipher")
    print("    -d    remove Duplicates")
    print("    -p    Print output")
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
    if remove_duplicates:
        passwordlist = sorted(set(passwordlist), key=lambda x:passwordlist.index(x))

    f = open(output_fp, "a")
    for word in passwordlist:
        f.write("{}\n".format(word))
    f.close()

    if print_output:
        for password in passwordlist:        
            print password
    
    end_time = time.time()
    delay = int((end_time - start_time))
    length = length + len(passwordlist)
    print length, "passwords created in", delay, "Seconds"



def mangle(word):
    new_list = word.split(" ")
    new_word = ""
    new_word = new_word+(new_list[1])
    new_word = new_word+(new_list[0])
    return new_word



def each_word_to_upper(word):
    new_list = word.split(" ")
    new_word = ""
    for i in new_list:
        new_word = new_word+i.capitalize()
    return new_word



def each_word_to_upper2(word):
    new_list = word.split(" ")
    new_word = ""
    for i, j in enumerate(new_list):
        if i == 0:
            new_word = ""+j.capitalize()
        else:
            new_word = new_word+" "+j.capitalize()
    return new_word



def each_word_to_upper3(word):
    new_list = word.split(" ")
    new_word = ""
    for i, j in enumerate(new_list):
        new_word = new_word+j.upper()
    return new_word



def get_tegnlist(ascii_fp):
    try:
        with open(ascii_fp, "r") as f:
            wordlist = f.read()
    except OSError as e:
        if e.errno == ENOENT:
            print "Error: File not found"
        if e.errno == EPERM:
            print "Eroor: Permission denied"

    return wordlist


def legg_til_tegn(passwordlist):
    data = get_tegnlist(ascii_fp)
    tegnlist = data.split('\n')
    del tegnlist[-1]

    newpasswordlist = []
    for word in passwordlist:
        for tegn in tegnlist:
            newpasswordlist.append(word+tegn)

    return newpasswordlist



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



def legg_til_leet(passwordlist):
    newpasswordlist = []
    password = ""

    en = ["s", "S", "$", "5"]
    to = ["i", "I", "!", "|", "1"]
    tre = ["g", "G", "6", "9"]
    fire = ["u", "U"]
    fem = ["r", "R"]
    seks = ["d", "D"]
    sju = ["k", "K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    atte = ["b", "B", "8", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for a in en:
        for b in to:
            for c in tre:
                for d in fire:
                    for e in fem:
                        for f in seks:
                            for g in sju:
                                for h in atte:
                                    password = a + b + c + d + e + f + g + h
                                    newpasswordlist.append(password)
    return newpasswordlist



def legg_til_leet2(passwordlist):
    newpasswordlist = []

    for password in passwordlist:
        newpassword = ""
        print password
        for letter in password:
                if letter is "i" or letter is "I":
                    newpassword = newpassword + "".join("1")
                elif letter is "z" or letter is "Z":
                    newpassword = newpassword + "".join("2")
                elif letter is "e" or letter is "E":
                    newpassword = newpassword + "".join("3")
                elif letter is "a" or letter is "A":
                    newpassword = newpassword + "".join("4")
                elif letter is "s" or letter is "S":
                    newpassword = newpassword + "".join("5")
                elif letter is "t" or letter is "T":
                    newpassword = newpassword + "".join("7")
                elif letter is "b" or letter is "B": 
                    newpassword = newpassword + "".join("8")
                elif letter is "g" or letter is "G":
                    newpassword = newpassword + "".join("9")
                elif letter is "o" or letter is "O":
                    newpassword = newpassword + "".join("0")
                else:
                    newpassword = newpassword + letter
        newpasswordlist.append(newpassword)

    return newpasswordlist



def legg_til_reverse(passwordlist):
    newpasswordlist = []
    for password in passwordlist:
        reverse = password[::-1]
        newpasswordlist.append(reverse)
    return newpasswordlist



def legg_til_mix(passwordlist):
    binarylist = []
    for i in range(0, 256):
        binarylist.append(str(bin(i))[2:].zfill(8))

    newlist = []
    for word in passwordlist:
        if len(word) < 9:
            for line in binarylist:
                newword = ""
                for i, bit in enumerate(line):
                    if word[i]:
                        if bit is "1":
                            newword = newword + word[i].upper()
                        if bit is "0":
                            newword = newword + word[i].lower()
                        else:
                            break
                    else:
                        break
                newlist.append(newword)
    return newlist
        



def legg_til_cipher(passwordlist, n):
    newpasswordlist = []
    for word in passwordlist:
        newword = ""
        for letter in word:
            if letter.isalpha():
                if letter.isupper():
                    newletter = chr((ord(letter) + n))
                    if ord(newletter) > 90:
                        newletter = chr(ord(newletter) - 26)
                    newword = newword + newletter
                if letter.islower():
                    newletter = chr((ord(letter) + n))
                    if ord(newletter) > 122:
                        newletter = chr(ord(newletter) - 26)
                    newword = newword + newletter
            else:
                newword = newword + letter
        newpasswordlist.append(newword)

    return newpasswordlist



def generate_passwords(input_fp, output_fp, length):
    data = get_wordlist(input_fp)
    wordlist = data.split('\n')
    del wordlist[-1]

    passwordlist = []
    for word in wordlist:
        passwordlist.append(word)
        passwordlist.append(word.capitalize())
        passwordlist.append(word.upper())
        if not word.isalpha():
            passwordlist.append(word.replace(" ", ""))
            passwordlist.append(word.replace(" ", "-"))
            passwordlist.append(word.replace(" ", "_"))
            passwordlist.append(mangle(word))
            passwordlist.append(each_word_to_upper(word))
            passwordlist.append(each_word_to_upper2(word))
            passwordlist.append(each_word_to_upper3(word))
            split_word = word.split(" ")
            for i in split_word:
                passwordlist.append(i)
                passwordlist.append(i.capitalize())
                passwordlist.append(i.upper())

    output_passwordlist(passwordlist, output_fp, length)

    if med_nummer:
        passwordlist_nummer = legg_til_nummer(passwordlist)
        output_passwordlist(passwordlist_nummer, output_fp, length)
    if med_mix:
        passwordlist_mix = legg_til_mix(passwordlist)
        output_passwordlist(passwordlist_mix, output_fp, length)
    if med_tegn:
        passwordlist_tegn = legg_til_tegn(passwordlist)
        output_passwordlist(passwordlist_tegn, output_fp, length)
    if med_leet:
        passwordlist_leet = legg_til_leet2(passwordlist)
        output_passwordlist(passwordlist_leet, output_fp, length)
    if med_reverse:
        passwordlist_reverse = legg_til_reverse(passwordlist)
        output_passwordlist(passwordlist_reverse, output_fp, length)
    if med_cipher:
        for n in range(0, 26):
            passwordlist_cipher = legg_til_cipher(passwordlist, n)
            output_passwordlist(passwordlist_cipher, output_fp, length)



if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:o:t:hcnpldrm')
    except getopt.GetoptError:
        print "Getopt error."
        usage()
        sys.exit(1)

    # timer
    start_time = time.time()

    # default
    input_fp = "wordlist.txt"
    output_fp = "passwordlist.txt"
    ascii_fp = "wordlist_ascii.txt"
    med_nummer = False
    med_tegn = False
    med_leet = False
    med_cipher = False
    med_mix = False
    med_reverse = False
    print_output = False
    remove_duplicates = False
    length = 0

    for opt, arg in opts:
        if opt in ("-h"):
            usage()
            sys.exit(1)
        elif opt in ("-i"):
            input_fp = arg
        elif opt in ("-o"):
            output_fp = arg
        elif opt in ("-t"):
            med_tegn = True
        elif opt in ("-c"):
            med_cipher = True
        elif opt in ("-n"):
            med_nummer = True
        elif opt in ("-l"):
            med_leet = True
        elif opt in ("-r"):
            med_reverse = True
        elif opt in ("-p"):
            print_output = True
        elif opt in ("-d"):
            remove_duplicates = True
        elif opt in ("-m"):
            med_mix = True
        else:
            print("Invalid argument {}".format(opt))

    try:
        generate_passwords(input_fp, output_fp, length)
        count_passwords(output_fp)
    except Exception as e:
        print "Oh no, something went wrong."
        print(e)
        usage()
        sys.exit(1)




