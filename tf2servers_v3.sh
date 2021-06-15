#!/bin/bash
version="Version 3.1.2"
#requires SSH keys
#requres GNU parallel
#optinal - dos2unix
#server details
user1="game"
host1="uk.moevsmachine.tf"
host2="vps.moevsmachine.tf"
host3="miku.gnome.moe"
echo "Current Filename: $(basename $BASH_SOURCE)"
echo ""
dos2unix $(basename $BASH_SOURCE) #fixes formatting/line ending issues between platforms.
echo ""
#start main funtions
if [ "$1" == "start" ]; then
    if [ "$2" == "tf2" ]; then
        echo "Starting UK servers."
        ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
        echo "Servers started!"
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"
    elif [ "$2" == "l4d2" ]; then
        echo "Starting the servers"       #start them
        ssh $user1@$host1 '/home/game/l4d2_1.sh && sleep 10s && /home/game/l4d2_2.sh && sleep 10s && /home/game/l4d2_3.sh && sleep 10s && /home/game/l4d2_4.sh;'
        echo ""
        ssh $user1@$host1 'screen -list | grep "l4d2"'
    else
        echo "No option selected"
        echo -e "\tstart tf2      -   Start TF2 servers"
        echo -e "\tstart l4d2     -   Start L4D2 servers"
    fi
#stop servers
elif [ "$1" == "stop" ]; then
    if [ "$2" == "tf2" ]; then
        echo "Stopping UK servers."
        ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
        echo "Servers stopped!"
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"
    elif [ "$2" == "l4d2" ]; then
        echo "Stopping the servers"       #stop them
        ssh $user1@$host1 'screen -S l4d2_1 -X quit; screen -S l4d2_2 -X quit; screen -S l4d2_3 -X quit; screen -S l4d2_4 -X quit'
    else
        echo "No option selected"
        echo -e "\tstop tf2      -   Stop TF2 servers"
        echo -e "\tstop l4d2     -   Stop L4D2 servers"
    fi

#update servers
elif [ "$1" == "update" ]; then
    if [ "$2" == "tf2" ]; then
        echo "Inb4 localisation files, updating servers!"
        sleep 5s
        echo "Stopping the servers"       #stop them
        ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
        echo "Running update script"      #run the update script
        ssh $user1@$host1 '/home/game/mvmx10_7_machine_attacks update; /home/game/mvmx10_1 update; /home/game/mvmx10_3 update; /home/game/cactuscanyon_1 update'
        echo  "Starting the servers"      #start them again
        ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"
    elif [ "$2" == "l4d2" ]; then
        echo "updating L4D2"
        sleep 5s
        echo "Stopping the servers"       #stop them
        ssh $user1@$host1 'screen -S l4d2_1 -X quit; screen -S l4d2_2 -X quit; screen -S l4d2_3 -X quit; screen -S l4d2_4 -X quit'
        echo "Running update script, this will freeze on waiting for user info..."      #run the update script
        ssh $user1@$host1 '/home/game/includes/update_l4d2.sh'
        echo  "Starting the servers"      #start them again
        ssh $user1@$host1 '/home/game/l4d2_1.sh && sleep 10s && /home/game/l4d2_2.sh && sleep 10s && /home/game/l4d2_3.sh && sleep 10s && /home/game/l4d2_4.sh;'
        echo "Checking status"
        ssh $user1@$host1 'screen -list | grep "l4d2"'
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"
    else
        echo "no option selected"
        echo -e "\tupdate tf2      -   Update TF2 servers"
        echo -e "\tupdate l4d2     -   Update L4D2 servers"
    fi


#reboot servers
elif [ "$1" == "restart" ]; then
    if [ "$2" == "tf2" ]; then
        echo "Restarting TF2 servers!"
        echo "Stopping the servers"       #stop them
        ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
        echo  "Starting the servers"      #start them again
        ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"
    elif [ "$2" == "l4d2" ]; then
        echo "Restarting L4D2 severs!"
        echo "Stopping the servers"       #stop them
        ssh $user1@$host1 'screen -S l4d2_1 -X quit; screen -S l4d2_2 -X quit; screen -S l4d2_3 -X quit; screen -S l4d2_4 -X quit'
        echo "Starting L4D2 servers"
        ssh $user1@$host1 '/home/game/l4d2_1.sh && sleep 10s && /home/game/l4d2_2.sh && sleep 10s && /home/game/l4d2_3.sh && sleep 10s && /home/game/l4d2_4.sh;'
        echo ""
        ssh $user1@$host1 'screen -list | grep "l4d2"'
    else
        echo "no option selected"
        echo -e "\trestart tf2      -   Restart TF2 servers"
        echo -e "\trestart l4d2     -   Restart L4D2 servers"
    fi

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
    #echo ""
    #ssh $user1@$host1 'cd /home/game/minecraft6/ && ./startmc.sh'
    echo "Starting TF2 Servers."
    ssh $user1@$host1 'parallel -k < "/home/game/includes/starttf2.sh"'
    echo "Servers started!"
    echo ""
    #echo "Starting Insurgency servers"
    #ssh $user1@$host1 '/home/game/insserver start; /home/game/insserver_1 start'
    #echo ""
    echo "Starting L4D2 servers"
    ssh $user1@$host1 '/home/game/l4d2_1.sh && sleep 10s && /home/game/l4d2_2.sh && sleep 10s && /home/game/l4d2_3.sh && sleep 10s && /home/game/l4d2_4.sh;'
    ssh $user1@$host1 'screen -list'
    echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
    echo "-----"

#stop ALL core servers/services
elif [ "$1" == "shutdown" ]; then
    echo "Stopping Discord bot"
    echo ""
    ssh $user1@$host1 'screen -S discordbot -X quit'
    #echo "Stopping Minecraft Server"
    #echo ""
    #ssh $user1@$host1 'screen -S discordbot -X quit'
    #echo "REQUIRES MANUAL SHUTDOWN"
    echo "Stopping TF2 Servers."
    ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
    echo "Servers down!"
    echo ""
    #echo "Stopping Insurgency servers"
    #ssh $user1@$host1 '/home/game/insserver stop; /home/game/insserver_1 stop'
    echo "Stopping the L4D2 servers"       #stop them
    ssh $user1@$host1 'screen -S l4d2_1 -X quit; screen -S l4d2_2 -X quit; screen -S l4d2_3 -X quit; screen -S l4d2_4 -X quit'
    echo "Servers down!"
    echo ""
    echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
    echo "-----"
elif [ "$1" == "mirror" ]; then
    echo "Mirror Information"
    echo ""
    read -p 'VPS Login: ' user2
    read -sp 'VPS Password: ' user2pass 
    echo ""
    echo ""
    echo "Uptime"
    sshpass -p $user2pass ssh $user2@$host2 'uptime'
    #pword, port, user, host, permissions1
    echo ""
    echo "File System Usage"
    sshpass -p $user2pass ssh $user2@$host2 'df -h'
    echo ""
    echo "RAM Usage"
    sshpass -p $user2pass ssh $user2@$host2 'free -h'  
#Proxmox Host
#elif [ "$1" == "host" ]; then
#    echo "Host Information"
#    echo ""
#    read -p 'Host Login: ' user3
#    read -sp 'Host Password: ' user3pass
#    port="8222" 
#    echo ""
#    echo ""
#    echo "Uptime"
#    sshpass -p $user3pass ssh -p $port $user3@$host3 'uptime'
#    #pword, port, user, host, permissions1
#    echo ""
#    echo "File System Usage"
#    sshpass -p $user3pass ssh -p $port $user3@$host3 'df -h'
#    echo ""
#    echo "RAM Usage"
#    sshpass -p $user3pass ssh -p $port $user3@$host3 'free -h'  


#print options
else
    echo ""
    echo "Available Options:"
    echo ""
    echo -e "\tStart     -   Start servers"
    echo -e "\tStop      -   Stop servers"
    echo -e "\tUpdate    -   Update servers"
    echo -e "\tRestart   -   Restart servers"
    echo -e "\tInfo      -   Pull local disk usage, memory usage & load average"
    echo -e "\tStartup   -   Start all core servers/services"
    echo -e "\tShutdown  -   Stop all core servers/services"
    echo -e "\tMirror    -   Pull TF2C mirror information"
    echo -e "\tHost      -   Pull host information - BROKEN"
    echo -e "\t"
    echo ""
    echo "$version"
    echo ""
fi
#echo ""
#echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
#echo "-----"
