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
if [ "$1" == "start"]; then
    if [ "$2" == "uk"]
        printf "Starting UK servers."

    elif [ "$2" == "la"]
        printf "Starting LA servers."

    elif [ "$2" == "all"]
        printf "Starting ALL servers."

    else
    
    fi

#stop servers
elif [ "$1" == "stop"]; then
    if [ "$2" == "uk"]
        printf "Stopping UK servers."

    elif [ "$2" == "la"]
        printf "Stopping LA servers."

    elif [ "$2" == "all"]
        printf "Stopping ALL servers."

    else

    fi

#update servers
elif [ "$1" == "update"]; then
    if [ "$2" == "uk"]
        printf "Updating UK servers."

    elif [ "$2" == "la"]
        printf "Updating LA servers."

    elif [ "$2" == "all"]
        printf "Updating ALL servers."

    else

    fi

#restart servers
elif [ "$1" == "restart"]; then
    if [ "$2" == "uk"]
        printf "Restarting UK servers."

    elif [ "$2" == "la"]
        printf "Restarting LA servers."

    elif [ "$2" == "all"]
        printf "Restarting ALL servers."

    else
    
    fi

#pull system information
elif [ "$1" == "info"]; then
    if [ "$2" == "uk"]
        printf "Gathering UK information."

    elif [ "$2" == "la"]
        printf "Gathering LA information."

    else

    fi

else





