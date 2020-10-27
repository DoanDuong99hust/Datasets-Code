#!/bin/bash

read -p "Enter the number of begin file: " beginFile
read -p "Enter the number of end file: " endFile
read -p "Enter location: " location

for ((i=$beginFile ; i <= $endFile ; i++))
do
    sudo chmod 777 $location
    echo "Creating folder $i"
    mkdir -p $location/file_$i/pcap_data
    cd /$location/file_$i/pcap_data
    mkdir -p inComing$i
    mkdir -p OutGoing$i
    mkdir -p filterLocalTraffic$i
    cd /$location/file_$i/pcap_data/filterLocalTraffic$i
    mkdir -p inComing$i
    mkdir -p outGoing$i

    mkdir -p $location/file_$i/csv_data
    cd /$location/file_$i/csv_data
    mkdir -p inComing$i
    mkdir -p OutGoing$i
    mkdir -p filterLocalTraffic$i
    cd /$location/file_$i/csv_data/filterLocalTraffic$i
    mkdir -p inComing$i
    mkdir -p outGoing$i


    echo "Create folder successfully!"
done