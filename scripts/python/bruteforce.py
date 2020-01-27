import random

# Create a random 3 pin password
password = []

for i in range(3):
   password.append(random.randint(0,9))

print password

# Brute force the 3 pin password
for i in range(10):
    for j in range(10):
        for k in range(10):
            if password[0] == i and password[1] == j and password[2] == k:
                print "Pin is: ", i, j, k
