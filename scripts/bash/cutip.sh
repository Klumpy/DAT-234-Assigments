#! /bin/bash



function getiprange {
	a=$(echo $1 | cut -f1 -d ".")
	echo $a
}
echo $(getiprange 192.158.1.1)
