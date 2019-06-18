#!/usr/bin/python3
#!/usr/bin/env python3

import os
import time
#lets define some things
port= 22
user= "<user>" #dont use root for fucks sake
host = "<host>"
nodeid = "<node>"
templatestorage = "<dir>" #location of ISO/cache folder (local on new install)
templatelocation = "vztmpl" #generally never needs to change
vmstoragelocation = "<storage>" #default local-zfs or local-lvm on fresh install

#below here shouldn't need modifying by end users?

#def lxcstart(message):
#    while True:
#        try:
#            lxcstart = int(input("Would you like to create or delete an LXC? Enter Create or delete:\n>"))
#        except ValueError:
#            print("Plese select a valid option.")
#            continue
#        else:
#            return lxcstart
#            break
#id = lxcstart("Would you like to create or delete an LXC? Enter Create or delete:\n>")
print("Updating LXC download cache")
#lxcupdate = 'ls /mechmirror/templates/template/cache > /mechmirror/backend/lxcdownloaded.txt' # done manually for now
#lxcupdate2 = 'ssh -p %d %s@%s %s' % (port, user, host, lxcupdate)                             # 
#os.system(lxcupdate2)
#
#
#
#
# Could potentionally use : pvesm list templates -content vztmpl - with templates being defined by the 'templatestorage'

creation = str(input("Would you like to create or delete an LXC? Enter Create or delete or type info for information:\n>"))
print('\n')
if creation in ['create']:
    print("this is the create script")
    def vmid(message):
        while True:
            try:
                vmid = int(input("Pick an ID: "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return vmid
                break
    (vmid2) = vmid("Select an ID:")
    lxcdownloaded = 'pvesm list %s -content %s' % (templatestorage, templatelocation)
    lxcdownloaded2 = 'ssh -p %d %s@%s %s' % (port, user, host, lxcdownloaded)
    os.system(lxcdownloaded2)
    def osid(message):
        while True:
            try:
                osid = str(input("Select an operating system from the above list: "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return osid
                break
    ostemplateid = osid("Select an operating system from the above list: ")
    def vcore(message):
        while True:
            try:
                vcore = int(input("Select vCores: "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return vcore
                break
    vcoreid = vcore("Select vCores: ")
    def ram(message):
        while True:
            try:
                ram = int(input("Select RAM in MB: "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return ram
                break
    ramid = ram("Select RAM in MB: ")

    def hdd(message):
        while True:
            try:
                hdd = int(input("Chose HD size in GB: "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return hdd
                break
    hddsize = hdd("Chose HD size in GB: ")

    def vmhostname(message):
        while True:
            try:
                vmhostname = str(input("Enter a FQDN: "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return vmhostname
                break
    vmhostnameid = vmhostname("Enter a FQDN: ")
    #ip addressing:
    def networkingipaddr(message):
        while True:
            try:
                networkingipaddr = str(input("Enter an IP address and CIDR eg 192.168.2.10/24 or dhcp: "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return networkingipaddr
                break
    networkingipaddr2 = networkingipaddr("Enter an IP address and CIDR eg 192.168.2.10/24 or dhcp: ")   
    #gateway:
    def networkinggw(message):
        while True:
            try:
                networkinggw = str(input("Enter the gateway: "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return networkinggw
                break
    networkinggw2 = networkinggw("Enter the gateway: ")  
    #print('Creating LXC Container ID %d with Operating system %s') % (vmid2, ostemplateid)
    finalstring = 'pvesh create /nodes/%s/lxc -vmid %d -hostname %s -storage %s -cores %d -memory %d -swap 0 -ostemplate local:%s/%s -rootfs %d -unprivileged -pass' % (nodeid, vmid2, vmhostnameid, vmstoragelocation, vcoreid, ramid, templatelocation, ostemplateid, hddsize) #s-size %d
    finalstring2 = 'ssh -p %d %s@%s %s' % (port, user, host, finalstring)
    os.system(finalstring2)
    lxccreation = 'LXC %d has been created' % (vmid2)
    print(lxccreation)
    time.sleep(5)
    #lets do some networking
    networstring = 'pvesh set /nodes/%s/lxc/%d/config -net0 bridge=vmbr0,ip=%s,name=eth0,type=veth' % (nodeid, vmid2, networkingipaddr2)
    networstring2 = 'ssh -p %d %s@%s %s' % (port, user, host, networstring)
    os.system(networstring2)
    #print completion
    lxcnetworkcreation = 'LXC %d network has been configured' % (vmid2)
    print(lxcnetworkcreation)    
    time.sleep(5)
    #starting LXC
    print('Starting LXC, wait 10 seconds:')
    lxcstart = 'pvesh create /nodes/%s/lxc/%d/status/start' % (nodeid, vmid2)
    lxcstart2 = 'ssh -p %d %s@%s %s' % (port, user, host, lxcstart)
    os.system(lxcstart2)
    time.sleep(10)
    #pulling LXC status
    lxcstatus = 'pvesh get /nodes/%s/lxc/%d/status/current' % (nodeid, vmid2)
    lxcstatus2 = 'ssh -p %d %s@%s %s' % (port, user, host, lxcstatus)
    os.system(lxcstatus2)
    #print('LXC %d created!') % (vmid2)
elif creation in ['delete']:
    print("ruh roh, you're getting deleted kiddo")

elif creation in ['info']:
    print("Polling system information, please wait!")
    #get pve version
    proxversion = "'pvesh get /version'"
    proxversion2 = 'ssh -p %d %s@%s %s' % (port, user, host, proxversion)
    #get uptime
    proxuptime = "'uptime'"
    proxuptime2 = 'ssh -p %d %s@%s %s' % (port, user, host, proxuptime)
    #get storage information
    proxstorage = "'df -h'"
    proxstorage2 = 'ssh -p %d %s@%s %s' % (port, user, host, proxstorage)
    print("Proxmox Information:\n")
    os.system(proxversion2)
    print("\n")
    print("Server Uptime:\n")
    os.system(proxuptime2)
    print("\n")
    print("Disk and mapping usage:\n")
    os.system(proxstorage2)
    print("\n")

    
    #print("Lets get some information!\n")
    #print('CPU Usage:', psutil.cpu_percent()),     
    #print(psutil.virtual_memory())  # physical memory usage
    #print('memory used in %:', psutil.virtual_memory()[2])
 #   ssh root@$host

else:
    print("No option selected, exiting!")



    #to do:
    #   Add password field, as it stands you have to pct connect <vmid> manually to change the password which isn't ideal.
    #