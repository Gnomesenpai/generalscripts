#!/bin/bash
version="Version 0.1"
#lets define some things
home="/home/game"
includes="/includes"
#LA details
user1="game"
host1="la.moevsmachine.tf"
#other server details
user2="game"
host2="uk.moevsmachine.tf"
#start servers
if [ "$1" == "start" ]; then
    if [ "$2" == "uk" ]; then
        printf "Starting UK servers."

    elif [ "$2" == "la" ]; then
        printf "Starting LA servers."

    elif [ "$2" == "all" ]; then
        printf "Starting ALL servers."

    else
        printf "meep"
    fi

#stop servers
elif [ "$1" == "stop" ]; then
    if [ "$2" == "uk" ]; then
        printf "Stopping UK servers."

    elif [ "$2" == "la" ]; then
        printf "Stopping LA servers."

    elif [ "$2" == "all" ]; then
        printf "Stopping ALL servers."

    else
        printf "meep"
    fi

#update servers
elif [ "$1" == "update" ]; then
    if [ "$2" == "uk" ]
        printf "Updating UK servers."

    elif [ "$2" == "la" ]; then
        printf "Updating LA servers."

    elif [ "$2" == "all" ]; then
        printf "Updating ALL servers."

    else
        printf "meep"
    fi

#restart servers
elif [ "$1" == "restart" ]; then
    if [ "$2" == "uk"]; then
        printf "Restarting UK servers."

    elif [ "$2" == "la" ]; then
        printf "Restarting LA servers."

    elif [ "$2" == "all" ]; then
        printf "Restarting ALL servers."

    else
        printf "meep"
    fi

#pull system information
elif [ "$1" == "info" ]; then
    if [ "$2" == "uk" ]; then
        printf "Gathering UK information."

    elif [ "$2" == "la" ]; then
        printf "Gathering LA information."

    else
        printf "meep"
    fi

else
echo ""
echo "Available Options:"
echo ""
echo -e "\tStart     -   start all LOCAL TF2 servers"
echo -e "\tStop      -   stop all LOCAL TF2 servers"
echo -e "\tUpdate    -   update all LOCAL TF2 servers"
echo -e "\tRestart   -   restart all LOCAL TF2 servers"
echo -e "\tInfo      -   Pull Local & Remote Uptime, Disk usage, memory usage & load average"
echo ""
echo "$version"
echo ""

fi

