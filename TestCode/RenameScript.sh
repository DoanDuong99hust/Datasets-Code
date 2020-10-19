#!/bin/bash
sudo chmod 777 /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f

read -p "Enter the number of begin file: " beginFile
read -p "Enter the number of end file: " endFile
 
function countNumfiles {
PYTHON_ARG="$1" python3 - <<END
import os, sys
path = os.environ['PYTHON_ARG']
lists = os.listdir(path)
for file in lists:
	print(file)
END
}
index = 0
for (( i = $beginFile; i <= $endFile; i++)) 
do
    echo "Processing file $i"

    numFiles=$(countNumfiles /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/HUST_DATA/inCom_outGo_$i/inCom)
    for file in $numFiles;
    do
        mv "/media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/HUST_DATA/inCom_outGo_$i/inCom/$file" "/media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/HUST_DATA/inCom_outGo_$i/inCom/$index"
        index=$((index+1))
    done
    echo "Done file $i"
done