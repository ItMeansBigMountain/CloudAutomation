#!/bin/bash

# Creates 25 empty (0 KB) files.

# creates the next batch of 25 files with increasing numbers starting with the latest iteration
# saves iteration in /tmp/SAVED_NUMBER




userFile_number="/tmp/userFile_number.dat"


# NO FILE --> CREATE
if [ ! -f "$userFile_number" ]; 
then
    value="0"
    echo 0 > "/tmp/userFile_number.dat"
    echo created file

# EXISTING FILE --> RETRIEVE
else
    value=$(cat "$userFile_number")
    echo "retrieved file:   $(cat "$userFile_number")"
fi







# CREATE FILES USING TMP VAR EXTRACTED FROM FILE
for (( i=1;i<=25;i++ ))
do
    ((value=value+1))
    touch "$USER$value"
    echo $value
done







# SAVE INTO TMP FILE FOR PERSISTANT DATA
echo $value > "/tmp/userFile_number.dat"
