#!/bin/bash

# pcapDataFolder = "/home/mpec/DoanDuong/DataCaptured"
# csvSavedFolder = "/home/mpec/DoanDuong/CsvData" 

tshark -r /home/mpec/DoanDuong/CsvData/outGoing371.pcap -T fields -e ip.src -e ip.dst -e frame.time -e frame.len -e ip.proto -E header=y -E separator=, -E occurrence=f > /home/mpec/DoanDuong/CsvData/outGoing371.csv
# tcpdump -r /home/mpec/DoanDuong/DataCaptured/CapByTime/time1.pcap -w /home/mpec/DoanDuong/CsvData/test1.pcap "tcp"
# sudo chmod 777 /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/By_time
#tcpdump -r /home/mpec/file_cap_371 -w /home/mpec/DoanDuong/CsvData/outGoing371.pcap src net 10.133 or 10.134 or 192.168
