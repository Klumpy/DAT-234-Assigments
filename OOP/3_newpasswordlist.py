"""
This new format will put usernames and passwords in coloums with whitespace between,
separated with newline. Readability is now higher.

olarhn coffee
arolhn whatever
arjoro phoenix

Since passwords can have special characters like ",:;" and such, we find it better to
separate with whitespace. This could be replaced if you must have whitespace in the username or password, 
but it is usually enough to have these 88 characters and symbols out of the ASCII:
!"#$%&'()*+,-./23456789:;<=>?@ABCDEFGHJKLMNOPRSTUVWXYZ[\]^_abcdefghijkmnopqrstuvwxyz{|}~

Since we are making a "passwordlist", we could also just have a list of passwords separated with newline, 
which would eliminate the "whitespace in password"-problem.
In a list where the length of usernames vary, there should be padding with whitespaces based on the longest username.
"""



"""Try to open file. There will be an exception if the file doesnt exist, 
or the user doesnt have permission to open the file."""
try:
    with open("passwordlist.txt", "r") as myfile:
        data = myfile.read().replace("\n", "")
except OSError as e:
    if e.errno == ENOENT:
        print "Error: File not found"
    if e.errno == EPERM:
        print "Error: Permission denied"
    else:
        print "Opening file.."



# LBYL
if not data:
    print "List is empty. No need to continue.."
    quit()

myList = data.split(';')
del myList[-1]

usernames = []
passwords = []

for word in myList:
    temp = word.split(":")
    a = temp[0]
    b = temp[1]
    usernames.append(a)
    passwords.append(b)
   


f = open("newpasswordlist.txt", "w")
for i, user in enumerate(usernames):
    f.write("{} {}\n".format(user, passwords[i]))

f.close()




