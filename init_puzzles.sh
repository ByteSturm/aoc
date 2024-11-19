#!/usr/bin/env bash
current_year=$(date +"%Y")
current_day=$(date +"%d")
year=${1:-${current_year}}
day=$(printf "%02d" ${2:-${current_day}})

touch "${year}/${day}/puzzle_1.py"
touch "${year}/${day}/puzzle_1_test.py"
touch "${year}/${day}/puzzle_2.py"
touch "${year}/${day}/puzzle_2_test.py"
