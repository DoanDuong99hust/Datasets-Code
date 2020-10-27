#!/bin/bash

# pcapDataFolder = "/home/mpec/DoanDuong/DataCaptured"
# csvSavedFolder = "/home/mpec/DoanDuong/CsvData"

# tcpdump -r /home/mpec/DoanDuong/DataCaptured/CapByTime/time1.pcap -w /home/mpec/DoanDuong/CsvData/test1.pcap "tcp"
#tcpdump -r timeTest1.pcap -n '(not (dst net 192.168))' -w filterPivateIp.pcap

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
    tcpdump -r $location/file_$i/pcap_data/inComing$i.pcap -n '(not (src net 192.168 or 10.134 or 10.133))' -w $location/file_$i/pcap_data/filterLocalTraffic$i/inComingFiltered$i.pcap

    echo "Done filtering file $i"
    editcap -i 150 $location/file_$i/pcap_data/filterLocalTraffic$i/inComingFiltered$i.pcap $location/file_$i/pcap_data/filterLocalTraffic$i/inComing$i/inComFiltered$i

    numFiles=$(countNumfiles $location/file_$i/pcap_data/filterLocalTraffic$i/inComing$i)
    for file in $numFiles;
    do
        echo "Read $file"
        tshark -r $location/file_$i/pcap_data/filterLocalTraffic$i/inComing$i/$file -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.len -e ip.proto -e tcp.flags.syn -E header=y -E separator=, -E occurrence=f > $location/file_$i/csv_data/filterLocalTraffic$i/inComing$i/$file.csv
        echo "Done $file"
    done
    echo "Done file $i"
done

for (( i = $beginFile; i <= $endFile; i++))
do
    echo "Processing file $i"
    tcpdump -r $location/file_$i/pcap_data/outGoing$i.pcap -n '(not (dst net 192.168 or 10.134 or 10.133))' -w $location/file_$i/pcap_data/filterLocalTraffic$i/outGoingFiltered$i.pcap

    echo "Done filtering file $i"
    editcap -i 150 $location/file_$i/pcap_data/filterLocalTraffic$i/outGoingFiltered$i.pcap $location/file_$i/pcap_data/filterLocalTraffic$i/outGoing$i/outGoFiltered$i


    numFiles=$(countNumfiles $location/file_$i/pcap_data/filterLocalTraffic$i/outGoing$i)
    for file in $numFiles;
    do
        echo "Read $file"
        tshark -r $location/file_$i/pcap_data/filterLocalTraffic$i/outGoing$i/$file -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.len -e ip.proto -e tcp.flags.syn -E header=y -E separator=, -E occurrence=f > $location/file_$i/csv_data/filterLocalTraffic$i/outGoing$i/$file.csv
        echo "Done $file"
    done
    echo "Done file $i"
done