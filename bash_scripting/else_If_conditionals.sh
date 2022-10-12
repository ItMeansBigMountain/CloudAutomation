#!/bin/bash



echo please enter first word
read first


echo please enter second word
read second


if [[ $first == $second ]]
then
    echo match
else
    echo no match
fi


