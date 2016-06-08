#!/bin/bash

file="1.txt"
count=0
field=4
criteria=6

while read line
do
    s=`echo $line | cut -d: -f"$field"`
    [[ $s == $criteria ]] && let "count+=1"
done<$file

echo "There are strings matching to criteria in defined file: " $count
echo ""
