#!/bin/bash
version="Version 1.0"

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
        echo "Starting UK servers."
        ssh $user2@$host2 'parallel -k < "/home/game/includes/starttf2.sh"'
        printf "Servers started!"
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"

    elif [ "$2" == "la" ]; then
        echo "Starting LA servers."
        ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
        printf "Servers started!"
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"

    else
        echo "Available Options:"
        echo ""
        echo -e "\tUK   -   Start UK Servers"
        echo -e "\tLA   -   Start LA Servers"
    fi

#stop servers
elif [ "$1" == "stop" ]; then
    if [ "$2" == "uk" ]; then
        echo "Stopping UK servers."
        ssh $user2@$host2 'parallel -k < "/home/game/includes/stoptf2.sh"'
        printf "Servers stopped!"
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"

    elif [ "$2" == "la" ]; then
        echo "Stopping LA servers."
        ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
        printf "Servers stopped!"
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"

    else
        echo "Available Options:"
        echo ""
        echo -e "\tUK   -   Stop UK Servers"
        echo -e "\tLA   -   Stop LA Servers"
    fi

#update servers
elif [ "$1" == "update" ]; then
    if [ "$2" == "uk" ]; then
        echo "Inb4 localisation files, updating servers!"
        printf "Stopping the servers"       #stop them
        ssh $user2@$host2 'parallel -k < "/home/game/includes/stoptf2.sh"'
        printf "Running update script"      #run the update script
        ssh $user2@$host2 'parallel -k < "/home/game/includes/updatetf2.sh"'
        printf  "Starting the servers"      #start them again
        ssh $user2@$host2 'parallel -k < "/home/game/includes/starttf2.sh"'
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"

    elif [ "$2" == "la" ]; then
        echo "Inb4 localisation files, updating servers!"
        printf "Stopping the servers"       #stop them
        ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
        printf "Running update script"      #run the update script
        ssh $user1@$host1 'parallel -k < "/home/game/includes/updatetf2.sh"'
        printf  "Starting the servers"      #start them again
        ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"
    else
        echo "Available Options:"
        echo ""
        echo -e "\tUK   -   Update UK Servers"
        echo -e "\tLA   -   Update LA Servers"
    fi

#reboot servers
elif [ "$1" == "restart" ]; then
    if [ "$2" == "uk" ]; then
        echo "Inb4 localisation files, updating servers!"
        printf "Stopping the servers"       #stop them
        ssh $user2@$host2 'parallel -k < "/home/game/includes/stoptf2.sh"'
        printf  "Starting the servers"      #start them again
        ssh $user2@$host2 'parallel -k < "/home/game/includes/starttf2.sh"'
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"

    elif [ "$2" == "la" ]; then
        echo "Inb4 localisation files, updating servers!"
        printf "Stopping the servers"       #stop them
        ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
        printf  "Starting the servers"      #start them again
        ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"
    else
        echo "Available Options:"
        echo ""
        echo -e "\tUK   -   Restart UK Servers"
        echo -e "\tLA   -   Restart LA Servers"
    fi

#pull system information
elif [ "$1" == "info" ]; then
    if [ "$2" == "uk" ]; then
        echo "Pulling UK stats"
        echo ""
        echo "Uptime"
        ssh $user2@$host2 'uptime'
        echo ""
        echo "File System Usage"
        ssh $user2@$host2 'df -h'
        echo ""
        echo "RAM Usage"
        ssh $user2@$host2 'free -h'  

    elif [ "$2" == "la" ]; then    
        echo "Pulling LA stats"
        echo ""
        echo "Uptime"
        ssh $user1@$host1 'uptime'
        echo ""
        echo "File System Usage"
        ssh $user1@$host1 'df -h'
        echo ""
        echo "RAM Usage"
        ssh $user1@$host1 'free -h'

    elif [ "$2" == "all" ]; then    
        echo "Pulling UK stats"
        echo ""
        echo "Uptime"
        ssh $user2@$host2 'uptime'
        echo ""
        echo "File System Usage"
        ssh $user2@$host2 'df -h'
        echo ""
        echo "RAM Usage"
        ssh $user2@$host2 'free -h' 
        echo "Pulling LA stats"
        echo ""
        echo "Uptime"
        ssh $user1@$host1 'uptime'
        echo ""
        echo "File System Usage"
        ssh $user1@$host1 'df -h'
        echo ""
        echo "RAM Usage"
        ssh $user1@$host1 'free -h'  

    else
        echo "Available Options:"
        echo ""
        echo -e "\tUK     -   UK Resource Usages & Uptime"
        echo -e "\tLA     -   LA Resource Usages & Uptime"
        echo -e "\tall    -   All Resource Usages & Uptime"
    fi

#print options
else
echo ""
echo "Available Options:"
echo ""
echo -e "\tStart     -   start TF2 servers"
echo -e "\tStop      -   stop TF2 servers"
echo -e "\tUpdate    -   update TF2 servers"
echo -e "\tRestart   -   restart TF2 servers"
echo -e "\tInfo      -   Pull Local & Remote Uptime, Disk usage, memory usage & load average"
echo ""
echo "$version"
echo ""
fi
#echo ""
#echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
#echo "-----"