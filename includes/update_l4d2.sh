#!/bin/bash
l4d2_srv="/home/game/l4d2_srv"
appid="222860"
./steamcmd.sh +login "anonymous"  +force_install_dir "${l4d2_srv}" +app_update "${appid}"  validate +quit

#./steamcmd.sh +login "anonymous"  +force_install_dir "/home/game/l4d2_srv" +app_update "222860"  validate +quit