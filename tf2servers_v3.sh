#!/bin/bash
version="Version 3.0"
#requires SSH keys
#requres GNU parallel
#server details
user1="game"
host1="uk.moevsmachine.tf"
#start servers
#fixes formatting/line ending issues between platforms.
dos2unix "tf2servers_v3.sh"
if [ "$1" == "start" ]; then
    echo "Starting UK servers."
    ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
    echo "Servers started!"
    echo ""
    echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
    echo "-----"

#stop servers
elif [ "$1" == "stop" ]; then
    echo "Stopping UK servers."
    ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
    echo "Servers stopped!"
    echo ""
    echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
    echo "-----"

#update servers
elif [ "$1" == "update" ]; then

    echo "Inb4 localisation files, updating servers!"
    echo "Stopping the servers"       #stop them
    ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
    echo "Running update script"      #run the update script
    #ssh $user1@$host1 'parallel -k < "/home/game/includes/updatetf2.sh"'
    ssh $user1@$host1 '/home/game/mvmx10_7_machine_attacks update; /home/game/mvmx10_1 update; /home/game/mvmx10_3 update; /home/game/cactuscanyon_1 update'
    echo  "Starting the servers"      #start them again
    ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
    echo ""
    echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
    echo "-----"

#reboot servers
elif [ "$1" == "restart" ]; then

    echo "Restarting all servers!"
    echo "Stopping the servers"       #stop them
    ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
    echo  "Starting the servers"      #start them again
    ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
    echo ""
    echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
    echo "-----"

#pull system information
elif [ "$1" == "info" ]; then

    echo "Pulling UK stats"
    echo ""
    echo "Uptime"
    ssh $user1@$host1 'uptime'
    echo ""
    echo "File System Usage"
    ssh $user1@$host1 'df -h'
    echo ""
    echo "RAM Usage"
    ssh $user1@$host1 'free -h'  

#start ALL core servers/services
elif [ "$1" == "startup" ]; then
    echo "Starting Hlstatsx"
    echo ""
    ssh $user1@$host1 '/home/game/statsscripts/run_hlstats start'
    echo "Starting Discord bot"
    echo ""
    ssh $user1@$host1 '/home/game/start_discord.sh'
    #echo "Starting Minecraft Server"
    echo ""
    #ssh $user1@$host1 '/home/game/mc_perfectlycomplex.sh'
    echo "Starting TF2 Servers."
    ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
    echo "Servers started!"
    echo ""
    echo "Starting Insurgency servers"
    ssh $user1@$host1 '/home/game/insserver start; /home/game/insserver_1 start'
    echo ""
    echo "Starting L4D2 servers"
    ssh $user1@$host1 '/home/game/l4d2_1.sh; /home/game/l4d2_2.sh; /home/game/l4d2_3.sh;'
    echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
    echo "-----"

#stop ALL core servers/services
elif [ "$1" == "shutdown" ]; then
    echo "Stopping Discord bot"
    echo ""
    echo "REQUIRES MANUAL SHUTDOWN"
    #ssh $user1@$host1 '/home/game/start_discord.sh'
    echo "Stopping Minecraft Server"
    echo ""
    echo "REQUIRES MANUAL SHUTDOWN"
    #ssh $user1@$host1 '/home/game/mc_perfectlycomplex.sh'
    echo "Stopping TF2 Servers."
    ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
    echo "Servers down!"
    echo ""
    echo "Stopping Insurgency servers"
    ssh $user1@$host1 '/home/game/insserver stop; /home/game/insserver_1 stop'

    echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
    echo "-----"

#print options
else
    echo ""
    echo "Available Options:"
    echo ""
    echo -e "\tStart     -   start TF2 servers"
    echo -e "\tStop      -   stop TF2 servers"
    echo -e "\tUpdate    -   update TF2 servers"
    echo -e "\tRestart   -   restart TF2 servers"
    echo -e "\tInfo      -   Pull local disk usage, memory usage & load average"
    echo -e "\tStartup   -   Start all core servers/services"
    echo -e "\tShutdown   -   Start all core servers/services"
    echo ""
    echo "$version"
    echo ""
fi
#echo ""
#echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
#echo "-----"
