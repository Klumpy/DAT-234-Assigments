import collections

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


myList = data.split(';')
del myList[-1]

dictionary = collections.defaultdict(list)
usernames = []
passwords = []
count = 0

for word in myList:
    temp = word.split(":")
    a = temp[0]
    b = temp[1]
    dictionary[a].append(b)
    usernames.append(a)
    passwords.append(b)
    count += 1

# Print all unique usernames
unique_usernames = set(usernames)
for username in unique_usernames:
    print username


# Print all unique passwords
unique_passwords = set(passwords)
for password in unique_passwords:
    print password


# How many passwords for each user
for user in unique_usernames:
    print user, " : ", len(dictionary[user])


# Number of total passwords
print "There is ", count, " total passwords"





