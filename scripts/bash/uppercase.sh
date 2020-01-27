characters=("bob" "reidar" "per")

for i in "${characters[@]}"
do
	echo $i | awk "{print toupper($0)}"
done

