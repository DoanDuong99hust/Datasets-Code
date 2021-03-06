#!/bin/bash

# tshark [ -i <capture interface>|- ] [ -f <capture filter> ] [ -2 ] [ -r <infile> ] [ -w <outfile>|- ] [ options ] [ <filter> ]

# tshark -G [ <report type> ] [ --elastic-mapping-filter <protocols> ]
# /home/mpec/DoanDuong/CodeScript/RunningCode/TestScript.sh
echo "Capturing pcap file! Please choose an option below! "

echo "1.Capturing by time"
echo "2.Capturing by size"
echo "3.Capturing by packets"

read -p "Enter your option: " option
# Capture by time
case "$option" in
	1 )
		read -p "Number of file wanting to capture: " numFiles1
		read -p "Period of time: " _time
		read -p "Interface: " interface1
		echo "Started capture $numFiles1 files by $_time seconds in $interface1"

		for (( i=1; i <= $numFiles1; i++))
		do
			tshark -i $interface1 -a duration:$_time -w /home/admin123/DoanDuong/TestData/by_time/timeTest"$i".pcap
			#tcpdump -i $interface1  -G $_time tcp -w /home/mpec/DoanDuong/DataCaptured/CapByTime/time"$i".pcap

			echo "Done $i"
		done
	;;
# Capture by size
	2 )
		read -p "Number of file wanting to capture: " numFiles2
		read -p "Size of file: " _size
		read -p "Interface: " interface2
		echo "Started capture $numFiles2 files by $_size kB in $interface2"

		tshark -i $interface2 -b filesize:$_size -a files:$numFiles2 -w /home/admin123/DoanDuong/TestData/by_size/size.pcap
	;;
#Capture by packet
	3 )
		read -p "Number of file wanting to capture: " numFiles3
		read -p "Numbedr of packets: " _packets
		read -p "Interface: " interface3
		echo "Started capture $numFiles3 files by $_packets packets in $interface3"
		for (( i=1; i <= $numFiles3; i++ )) 
		do
			 tshark -i $interface3 -c $_packets -w /home/mpec/DoanDuong/DataCaptured/CapByPacket/packets"$i".pcap
#			tcpdump -i $interface3 -c $_packets tcp -w /home/mpec/DoanDuong/DataCaptured/CapByPacket/packets"$i".pcap
			echo "Done $i"
		done
	;;
	*)
		echo "Choose the valid option!"
esac

echo "Completed !"


