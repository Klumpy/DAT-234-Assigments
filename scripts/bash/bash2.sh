#REPETITION

#! /bin/bash
echo "hello world"

a="hello owlrd"
echo @a

declare -i a
a=12
echo $a
a="hei"
echo $a
# gives nothing.

a=10
let "a=$a+10"

kernel=$(uname -sr)
location=$(pwd)
echo "you are running $kernel in $location

t1="foo"
t2="bar"
if [ "$t1" 0 "$t2" ; then
	echo "true"
else
	echo "false"
fi

OPTIONS="Hack Leave Backup"
select option in $OPTIONS
do
	if [ "$option" = "Hack" ] ; then
		echo "Lets Hack"
	else
		echo "Quitting..."
		exit
	fi
done


for i in {1..10}
do
	echo "Welcome $i times"
done

for i in $(seq 10)
do
	echo $i
done

for filename in $( ls )
do
	echo "Filename is $filename"
done


#ARRAYS

os=("linux" "mac" "windows")
echo "${os[0]}"		#first value
echo "${os[@]}"		#all values
echo "${!os[@]}"	#index value
echo "${#os[@]}"	#length of an array

for i in "${os[@]}"
do
	echo $i
done


#ASSOCIATIVE ARRAYS
declare -A user
user=([mortengo]="Morten Goodwin" [sgurda]="Sigurd Assev")

for i in "${!user[$i]}"
do
	echo "key:	$i"
	echo "Value:	${user[$i]}"
done

function printtwo {
	let "a=$1+$2"
	echo $a
}
printtwo 12 5


#PIPE

ls -a | grep "\.sh"
ls | grep 2012 | sort | uniq

#redirect stdout to a file
ls -alh > examplefile
ls -alh 1> examplefile

#Append to file
ls -alh >> examplefile

