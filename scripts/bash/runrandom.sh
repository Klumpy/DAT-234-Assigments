#! /bin/bash

echo "how many times?"
read counter

#remove tempfile here

for i in $(seq $counter)
do
	./random.sh >> tempfile
done

#print out filecontent (temp) here
echo ""
