#!/bin/bash

read -p "Enter the number of begin file: " beginFile
read -p "Enter the number of end file: " endFile
read -p "Enter location: " location

for ((i=$beginFile ; i <= $endFile ; i++))
do
    sudo chmod 777 $location
    echo "Creating folder $i"
    mkdir -p $location/file_$i/outGoing$i
    cd /$location/file_$i
    mkdir -p inComing$i
    echo "Create folder successfully!"
done