#!/bin/bash


# (()) is used for arithmetic 
# If i put a string in (), it gives me arithmetic error,


# [[]] is true/false. 
# [] equates to false





echo Please input a number
read number

if [[ $number == "45" || $number == "55"  ]]
then
echo win
else
echo loss
fi



