#!/bin/bash
version="Version 3.1.0"
#requires SSH keys
#requres GNU parallel
#server details
user1="game"
host1="uk.moevsmachine.tf"
host2="vps.moevsmachine.tf"
host3="miku.gnome.moe"
#start servers
#fixes formatting/line ending issues between platforms.
dos2unix "tf2servers_v3.sh"
#start main funtions
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
    if [ "$2" == "tf2" ]; then
        echo "Inb4 localisation files, updating servers!"
        sleep 5s
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
    elif [ "$2" == "l4d2" ]; then
        echo "updating L4D2"
        sleep 5s
        echo "Stopping the servers"       #stop them
        #ssh $user1@$host1 'parallel -k < "/home/game/includes/stoptf2.sh"'
        echo "Running update script, this will freeze on waiting for user info..."      #run the update script
        #ssh $user1@$host1 '/home/game/includes/update_l4d2.sh'
        ssh $user1@$host1 '/home/game/steamcmd/steamcmd.sh +login "anonymous"  +force_install_dir "/home/game/l4d2_srv" +app_update "222860"  validate +quit'
        echo  "Starting the servers"      #start them again
        ssh $user1@$host1 '/home/game/l4d2_1.sh; /home/game/l4d2_2.sh; /home/game/l4d2_3.sh; /home/game/l4d2_4.sh;'
        echo ""
        echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
        echo "-----"
    else
        echo "no option selected"
    fi


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
    #echo "Starting Insurgency servers"
    #ssh $user1@$host1 '/home/game/insserver start; /home/game/insserver_1 start'
    #echo ""
    echo "Starting L4D2 servers"
    ssh $user1@$host1 '/home/game/l4d2_1.sh; /home/game/l4d2_2.sh; /home/game/l4d2_3.sh; /home/game/l4d2_4.sh;'
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
    echo -e "\tStart     -   Start TF2 servers"
    echo -e "\tStop      -   Stop TF2 servers"
    echo -e "\tUpdate    -   Update TF2 servers"
    echo -e "\tRestart   -   Restart TF2 servers"
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
