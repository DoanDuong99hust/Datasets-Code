#!/bin/bash

# pcapDataFolder = "/home/mpec/DoanDuong/DataCaptured"
# csvSavedFolder = "/home/mpec/DoanDuong/CsvData" 

# tcpdump -r /home/mpec/DoanDuong/DataCaptured/CapByTime/time1.pcap -w /home/mpec/DoanDuong/CsvData/test1.pcap "tcp"

read -p "Enter the number of begin file: " beginFile
read -p "Enter the number of end file: " endFile
read -p "Enter location: " location

sudo chmod 777 $location
 
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
    tcpdump -r /home/admin123/Downloads/file_cap_$i -w $location/file_$i/pcap_data/outGoing$i.pcap -n '( (src net 10.133 or 10.134 or 192.168) and not (dst 10.133 or 10.134 or 192.168))'
    echo "Done filtering file $i"
    editcap -i 150 $location/file_$i/pcap_data/outGoing$i.pcap $location/file_$i/pcap_data/OutGoing$i/outGo$i

    numFiles=$(countNumfiles $location/file_$i/pcap_data/OutGoing$i)
    for file in $numFiles;
    do
        echo "Read $file"
        tshark -r $location/file_$i/pcap_data/OutGoing$i/$file -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.len -e ip.proto -e tcp.flags.syn -E header=y -E separator=, -E occurrence=f > $location/file_$i/csv_data/OutGoing$i/$file.csv
        echo "Done $file"
    done
    echo "Done file $i"
done
