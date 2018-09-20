""" Dictionary with usernames and passwords
arg1 - 6 characters long
arg2 - One Capital letter
arg3 - Begins with number

Print out the belonging username and password"""



dict = {"chris":"helloworld", "john":"passw1", "nelly":"2hell1", "wendy":"1Passw"}

for user, password in dict.items():
    if len(password) == 6:
        if password[0].isdigit():
            for j in password:
                if j.isupper():
                    print user, password
    
        
        