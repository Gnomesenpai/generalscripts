#!/bin/bash

#define directories
base="home/game/tf2servers"
base2="home/game"
suffix="tf/addons/sourcemod/configs"

curl -L https://raw.githubusercontent.com/Gnomesenpai/generalscripts/master/bulkcopy/serverhop.cfg > /$base2/bulkcopy/serverhop.cfg
#Define game server folders
maattk="/${base}/machine_attacks/${suffix}"
ao3="/${base}/mvm_ao3/${suffix}"
joinblu="/${base}/mvm_joinblu/${suffix}"
nox10="/${base}/mvm_nox10/${suffix}"
uu="/${base}/mvm_uu/${suffix}"
mvmx10="/${base}/mvmx10/${suffix}"
stt="/${base}/stop_that_tank/${suffix}"
#use parallel cp to mass copy serverhop.cfg
#parallel cp -vf "/${base2}/bulkcopy/serverhop.cfg" :::  $serverfiles $mvm30wave $maattk $nox10 $tf2ware $vanilla $insurgency

#parallel rsync to LA
#parallel rsync --progress  -vhz "${base}/bulkcopy/serverhop.cfg" ::: game@aus.moevsmachine.tf:$serverfiles game@aus.moevsmachine.tf:$nox10 game@aus.moevsmachine.tf:$maattk
echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
echo "-----"

echo "$base$vanilla"
