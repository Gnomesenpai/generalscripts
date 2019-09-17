#!/bin/bash

#define
exmemory='/exmemory'
pve='/etc/pve'
vps='/mainssd/subvol-100-disk-0/home/game/backup/'

#kvm backups
cp -Rv $pve/qemu-server/ $exmemory/backup/

#lxc backup
cp -Rv $pve/lxc/ $exmemory/backup/

#interface backups
cp -Rv /etc/network/interfaces $exmemory/backup/

#copy backup to another location? rysnc maybe?
#cp -Rv /exmemory/backup /exmemory/backup2/

#copy this script to backup
cp -v $exmemory/configbackup.sh $exmemory/backup/

#set permissions
chmod 777 $exmemory/backup

#Remove TARGZ archives
rm /exmemory/backup.tar.gz
rm $vps/backup.tar.gz

# TARGZ
tar -zcvf $exmemory/backup.tar.gz $exmemory/backup/

#copy to VPS for external backup
cp -vf  $exmemory/backup.tar.gz $vps


echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
echo "-----"