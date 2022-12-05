#!/bin/bash
wget 
#define directories
base="/home/game"
suffix="/addons/sourcemod/configs"

#Define game server folders
serverfiles="${base}/serverfiles/tf${suffix}"
mvm30wave="${base}/tf2_adventures_30wave/tf${suffix}"
maattk="${base}/tf2_machine_attacks/tf${suffix}"
nox10="${base}/tf2_nox10/tf${suffix}"
tf2ware="${base}/tf2_tf2ware/tf${suffix}"
vanilla="${base}/tf2_machine_attacks/tf${suffix}"
insurgency="${base}/insurgency/insurgency${suffix}"

#use parallel cp to mass copy Webshortcuts.txt
parallel cp -vf "${base}/bulkcopy/Webshortcuts.txt" :::  $serverfiles $mvm30wave $maattk $nox10 $tf2ware $vanilla $insurgency

#parallel rsync to LA
#parallel rsync --progress  -vhz "${base}/bulkcopy/Webshortcuts.txt" ::: game@la.moevsmachine.tf:$serverfiles game@la.moevsmachine.tf:$nox10 game@la.moevsmachine.tf:$maattk
echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
echo "-----"

echo "$base$vanilla"
