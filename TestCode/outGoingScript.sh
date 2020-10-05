#!/bin/bash

# pcapDataFolder = "/home/mpec/DoanDuong/DataCaptured"
# csvSavedFolder = "/home/mpec/DoanDuong/CsvData" 

# tcpdump -r /home/mpec/DoanDuong/DataCaptured/CapByTime/time1.pcap -w /home/mpec/DoanDuong/CsvData/test1.pcap "tcp"

sudo chmod 777 /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f

for (( i = 368; i <= 371; i++)) 
do
    tcpdump -r /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/file_cap_$i.pcap -w /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/HUST_DATA/inCom_outGo_$i/outGoing$i.pcap src net 10.133 or 10.134 or 192.168
    tshark -r /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/HUST_DATA/inCom_outGo_$i/outGoing$i.pcap -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.len -e ip.proto -e tcp.flags.syn -e frame.time -E header=y -E separator=, -E occurrence=f > /home/mpec/DoanDuong/CsvData/file_$i/outGoing$i.csv
    echo "Done $i"
done