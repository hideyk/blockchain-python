#!/bin/bash

NC='\033[0m'
RED='\033[0;31m'
GREY='\033[0;37m'
GREEN='\033[0;32m'
LBLUE='\033[1;34m'
YELLOW='\033[1;33m'
LCYAN='\033[1;36m'

DIFFICULTY=$1
SEED=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13 ; echo '')

get_hash () {
        word=$1
        hash_result=$(echo -n "$1" | sha256sum)
        echo $hash_result
}

verify_difficulty () {
        hash_result=$1
        if [[ $hash_result =~ ^[0]{$DIFFICULTY,}.*$ ]]; then
                return 0
        else
                return 1
        fi
}

start=$(date +%s.%N)
clear
printf "${GREY}\n\n=== [Single block simulator] ===\n${NC}"
printf "${GREY}Block data: $SEED\n\n${NC}"

i=0
while true;
do
        i=$((i+1))
        nonced_value="$SEED$i"
        hashed_value=$(get_hash $nonced_value)

        if verify_difficulty $hashed_value; then
                printf "${GREEN}\nFound an accepted hash value${NC}"
                printf "${GREEN}\n($i) [Success] $nonced_value : $hashed_value\n\n${NC}"
                end=$(date +%s.%N)
                printf "${LBLUE}Runtime: $( echo "$end - $start" | bc -l )s\n${NC}"
                printf "${LBLUE}Iterations: $i\n${NC}"
                break
        else
                printf "${RED}($i) [Failed] $nonced_value : $hashed_value\n${NC}"
        fi

done
