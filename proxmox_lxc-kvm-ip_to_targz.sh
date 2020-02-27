#!/bin/bash

#define
backupdir='/hgstmirror'
pve='/etc/pve'
vps='/mainssd/subvol-100-disk-0/home/game/backup/'

#kvm backups
cp -Rv $pve/qemu-server/ $backupdir/backup/

#lxc backup
cp -Rv $pve/lxc/ $backupdir/backup/

#interface backups
cp -Rv /etc/network/interfaces $backupdir/backup/

#copy backup to another location? rysnc maybe?
#cp -Rv /exmemory/backup /exmemory/backup2/

#copy this script to backup
cp -v $backupdir/configbackup.sh $backupdir/backup/

#set permissions
chmod 777 -R $backupdir/backup

#Remove TARGZ archives
rm $backupdir/backup.tar.gz
rm $vps/backup.tar.gz

# TARGZ
tar -zcvf $backupdir/backup.tar.gz $backupdir/backup/

#copy to VPS for external backup
cp -vf  $backupdir/backup.tar.gz $vps


echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
echo "-----"