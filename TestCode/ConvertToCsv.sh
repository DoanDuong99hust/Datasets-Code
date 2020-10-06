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

# editcap -i 150 inComing368.pcap inCom/inCom368 
function countNumfiles {
PYTHON_ARG="$1" python3 - <<END
import os, sys
import numpy as np
path = os.environ['PYTHON_ARG']
lists = os.listdir(path)
for file in lists:
	print(file)
END
}
countNumfiles /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/HUST_DATA/inCom_outGo_368/inCom
test1=$(countNumfiles /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/HUST_DATA/inCom_outGo_368/inCom)

echo "------------"
# echo $test1

for is in $test1; do
	echo $is
done
# for ((i=1 ; i <= $test1; i++))
# do 
# 	echo $i
# done
# 	function current_datetime {
# python - <<END
# import datetime
# print datetime.datetime.now()
# END
# }

# # Call it
# current_datetime

# # Call it and capture the output
# DT=$(current_datetime)
# echo Current date and time: $DT

# function line {
# PYTHON_ARG="$1" python - <<END
# import os
# line_len = int(os.environ['PYTHON_ARG'])
# print '-' * line_len
# END
# }

# # Do it one way
# line 80

# # Do it another way
# echo $(line 80)

 #tshark -r /media/mpec/eb38a860-81a7-43f8-9205-6df6e098435f/HUST_DATA/inCom_outGo_368/outGo/outGo368_1.pcap -T fields -e frame.time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.len -e ip.proto -e tcp.flags.syn -E header=y -E separator=, -E occurrence=f > /home/mpec/DoanDuong/CsvData/file_368/outGoingTest.csv
