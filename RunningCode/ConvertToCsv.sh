#!/bin/bash

# pcapDataFolder = "/home/mpec/DoanDuong/DataCaptured"
# csvSavedFolder = "/home/mpec/DoanDuong/CsvData" 

# tcpdump -r /home/mpec/DoanDuong/DataCaptured/CapByTime/time1.pcap -w /home/mpec/DoanDuong/CsvData/test1.pcap "tcp"
# array = [371,370,369,368,367]

# sudo chmod 777 /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f

# for i in array do
#     tcpdump -r /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/file_cap_$i.pcap -w /home/mpec/DoanDuong/CsvData/file_$i/outGoing$i.pcap src net 10.133 or 10.134 or 192.168
#     tshark -r /home/mpec/DoanDuong/CsvData/file_371/InGoing371_.pcap -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.len -e ip.proto -e frame.time -e tcp.flags.syn -E header=y -E separator=; -E occurrence=f > /home/mpec/DoanDuong/CsvData/InGoing371/InGoing371_0.csv
#     echo "Done $i"
# done

/home/mpec/DoanDuong/CodeScript/TestCode/inComingScript.sh
/home/mpec/DoanDuong/CodeScript/TestCode/outGoingScript.sh