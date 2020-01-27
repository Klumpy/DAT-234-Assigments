#! /bin/bash

declare -A users
users="[user1]=pass1 [user2]=pass2"

for i in "${users@]}"
do
	echo "key	:	$i"
	echo "value	: 	${users[$i]}"

	ssh $i@localhost -password=${users[$i]}
done