#!/bin/bash

DELAY=2
NC='\033[0m'
RED='\033[0;31m'
GREY='\033[0;37m'
GREEN='\033[0;32m'
LBLUE='\033[1;34m'
YELLOW='\033[1;33m'
LCYAN='\033[1;36m'


clear

while true; do
        printf "

        ${GREEN}=== [Mining Simulator] ===${NC}

        Please select an option:

                A. Single block
                B. Multiple blocks
                Q. Quit\n\n
        "
        read -p "Enter selection > "

        case "$REPLY" in

        Q|q)    clear
                        printf "${GREY}---------------------"
                        printf "\nProgram terminated"
                        printf "\n---------------------${NC}\n\n\n"
                        exit
                        ;;

        A|a)    printf "

        ${LCYAN}Please enter Proof-Of-Work difficulty.${NC}\n\n
        "
                        read -p "Enter selection > "
                        ./single_block.sh "$REPLY"
                        sleep "$DELAY"
                        printf "${YELLOW}\n--------------------------${NC}"
                        printf "${YELLOW}Press ENTER to continue${NC}"
                        printf "${YELLOW}--------------------------${NC}\n"
                        read -p ""
                        clear
                        ;;

        B|b)
                        sleep "$DELAY"
                        ;;


        *)              clear
                printf "${RED}Invalid entry!\n--------------${NC}
                        " >&2
                        ;;
        esac
done
