
index=1
cat arguments.txt | while read line 
do
	n=1 #executa cada entrada 10x
	while [ $n -le 2 ]
	do
		echo "$(python3 main.py $line)"
		n=$(( n+1 )) #incrementa n
	done
	index=$(( index+1 )) #incrementa index da instancia
done
