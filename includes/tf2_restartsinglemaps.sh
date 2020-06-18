#!/bin/bash

./cactuscanyon_1 stop
./cactuscanyon_1 start

./asteroid_1 stop
./asteroid_1 start

./mgemod_1 stop
./mgemod_1 start

./orange stop
./orange start

#./tf2ware_1 stop
#./tf2ware_1 start

echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
echo "-----"

