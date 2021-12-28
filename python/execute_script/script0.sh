#!/bin/bash
echo "This is the start of the script 0 - bash script"
>&2 echo [START] This message goes to stderr 
for i in {1..5}
do
   echo "$i times"
   sleep 1
done
>&2 echo [END] This message goes to stderr >&2