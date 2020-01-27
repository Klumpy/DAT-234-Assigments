""" Dictionary with usernames and passwords
arg1 - 6 characters long
arg2 - One Capital letter
arg3 - Begins with number

Print out the belonging username and password"""



myDict = {"chris":"helloworld", "john":"passw1", "nelly":"2hell1", "wendy":"1Passw"}

for user, password in myDict.items():
    if len(password) == 6:
        if password[0].isdigit():
            count = 0
            for character in password:
                if character.isupper():
                    count += 1
            if count == 1:
                print user, password

        
        
