#!/usr/bin/env bash
current_year=$(date +"%Y")
year=${1:-${current_year}}

for ((index = 1 ; index < 25 ; index++ ))
do 
    day=$(printf "%02d" ${index})
    mkdir -p "${year}/${day}"
done
