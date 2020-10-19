#!/bin/bash

# pcapDataFolder = "/home/mpec/DoanDuong/DataCaptured"
# csvSavedFolder = "/home/mpec/DoanDuong/CsvData" 

# tcpdump -r /home/mpec/DoanDuong/DataCaptured/CapByTime/time1.pcap -w /home/mpec/DoanDuong/CsvData/test1.pcap "tcp"

sudo chmod 777 /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f

read -p "Enter the number of begin file: " beginFile
read -p "Enter the number of end file: " endFile
read -p "Enter location: " location
 
function countNumfiles {
PYTHON_ARG="$1" python3 - <<END
import os, sys
path = os.environ['PYTHON_ARG']
lists = os.listdir(path)
for file in lists:
	print(file)
END
}

for (( i = $beginFile; i <= $endFile; i++)) 
do
    echo "Processing file $i"
    tcpdump -r /$location/file_cap_$i.pcap -w /$location/HUST_DATA/inCom_outGo_$i/outGoing$i.pcap src net 10.133 or 10.134 or 192.168
    echo "Done filtering file $i"
    editcap -i 130 $location/HUST_DATA/inCom_outGo_$i/outGoing$i.pcap $location/HUST_DATA/inCom_outGo_$i/outGo/outGo$i


    numFiles=$(countNumfiles /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/HUST_DATA/inCom_outGo_$i/outGo)
    for file in $numFiles;
    do
        echo "Read $file"
        tshark -r $location/HUST_DATA/inCom_outGo_$i/outGo/$file -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.len -e ip.proto -e tcp.flags.syn -E header=y -E separator=, -E occurrence=f > $location/file_$i/outGoing$i/$file.csv
        echo "Done $file"
    done
    echo "Done file $i"
done
