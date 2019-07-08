#!/usr/bin/python3
#!/usr/bin/env python3

import os
import time
import getpass
#lets define some things
port= 22
user= "<user>" #dont use root for fucks sake
host = "<host>" #hostname or IP of proxmox management
nodeid = "<node>" #node ID
templatestorage = "local" #location of ISO/cache folder (local on new install) 
templatelocation = "vztmpl" #generally never needs to change
vmstoragelocation = "local-lvm" #default local-zfs or local-lvm on fresh install

#below here shouldn't need modifying by end users?


#lxcupdate = 'ls /mechmirror/templates/template/cache > /mechmirror/backend/lxcdownloaded.txt' # done manually for now
#lxcupdate2 = 'ssh -p %d %s@%s %s' % (port, user, host, lxcupdate)                             # 
#os.system(lxcupdate2)
#
#
#
#
# Could potentionally use : pvesm list templates -content vztmpl - with templates being defined by the 'templatestorage'


#
#VMID needs to ideall be automated, possibly done with listing the current configs on the server?
#

#pull LXC cache
print("Updating LXC template cache")
lxccache = 'pveam update'
lxccache2 = 'ssh -p %d %s@%s %s' % (port, user, host, lxccache)
os.system(lxccache2)
print("Done!")
time.sleep(2)

#start main program
creation = str(input("Would you like to create or delete an LXC? Enter Create or delete or type info for information:\n>"))
print('\n')
#start of LXC creation
if creation in ['create']:
    #start VMID selection
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
    #end VMID selection
    print("\n")
    #start template download (optional)
    lxccurrenttemplate = 'pveam available --section system'# % (templatestorage, templatelocation)
    lxccurrenttemplate2 = 'ssh -p %d %s@%s %s' % (port, user, host, lxccurrenttemplate)
    os.system(lxccurrenttemplate2)
    osdownload = str(input("would you like to download a template? "))
    if osdownload in ['yes']:
        print("Lets go!")
        osdownload2 = str(input("Plese enter the complete template name: "))

        osdownload3 = 'pveam download  %s %s' % (templatestorage, osdownload2)

        osdownload4 = 'ssh -p %d %s@%s %s' % (port, user, host, osdownload3)

        os.system(osdownload4)
    else:
        print("Ok, skipping!")


    #end template download
    print("\n")
    #start OS selection
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
    #end OS selection
    print("\n")
    #start Vcore selection
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
    #end Vcore selection
    print("\n")
    #start ram selection
    def ram(message):
        while True:
            try:
                ram = int(input("Select RAM in MB (min 512): "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return ram
                break
    ramid = ram("Select RAM in MB (min 512): ")
    #end ram selection
    print("\n")
    #start HDD selection
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
    #end HDD selection
    print("\n")
    #start password creation
    pass1 = getpass.getpass('Enter the Root password: ')
    pass2 = getpass.getpass('Enter the Root password AGAIN: ')    
    if pass2==pass1:
        print("password created")
    else:
        print("Password does not match. Please try again")
    #end password creation
    print("\n")
    #VM host/FQDN    
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
    #networking IF statement
    initialnetwork = str(input("Please select a networking configuration, static/dhcp or blank for none:\n"))
    if initialnetwork in ['static']:
        print('static Selected')
        #Inputting IP/CIDR
        def networkingipaddr(message):
            while True:
                try:
                    networkingipaddr = str(input("Enter an IP address and CIDR eg 192.168.2.10/24: "))
                except ValueError:
                    print("Please select a valid input.")
                    continue
                else:
                    return networkingipaddr
                    break
        networkingipaddr2 = networkingipaddr("Enter an IP address and CIDR eg 192.168.2.10/24: ")
        #Inputting gateway
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
        #end of Static configuration
    #start dhcp elif
    elif initialnetwork in ['dhcp']:
        print('DHCP Selected')
        networkingipaddr2 = 'dhcp'
        networkinggw2 = '0.0.0.0'
    #end dhcp elif
    else:
        print('No network configuration selected, continuing!')
    initialnetworkvlan = int(input("Please select a VLAN, leave blank for none: "))
    print("\n")

    #print('Creating LXC Container ID %d with Operating system %s') % (vmid2, ostemplateid)
    finalstring = 'pvesh create /nodes/%s/lxc -vmid %d -hostname %s -storage %s -cores %d -memory %d -swap 0 -ostemplate %s:%s/%s -rootfs %d -unprivileged -password %s -swap 0' % (nodeid, vmid2, vmhostnameid, vmstoragelocation, vcoreid, ramid, templatestorage, templatelocation, ostemplateid, hddsize, pass1) #s-size %d
    finalstring2 = 'ssh -p %d %s@%s %s' % (port, user, host, finalstring)
    os.system(finalstring2)
    lxccreation = 'LXC %d has been created' % (vmid2)
    print(lxccreation)
    time.sleep(5)
    #lets do some networking
    networstring = 'pvesh set /nodes/%s/lxc/%d/config -net0 bridge=vmbr0,ip=%s,gw=%s,name=eth0,type=veth,tag=%d' % (nodeid, vmid2, networkingipaddr2, networkinggw2, initialnetworkvlan)
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
    #get all VM's version
    #proxvmlist = "'pvesh get /cluster/resources --type vm'"
    #proxvmlist2 = 'ssh -p %d %s@%s %s' % (port, user, host, proxvmlist)
    #os.system(proxvmlist2)

    #print("Lets get some information!\n")
    #print('CPU Usage:', psutil.cpu_percent()),     
    #print(psutil.virtual_memory())  # physical memory usage
    #print('memory used in %:', psutil.virtual_memory()[2])
 #   ssh root@$host

else:
    print("No option selected, exiting!")



#to do:
#   General improvements:
#       some way to better impliment OS selection, current works but not ideal.
#
#   User account creation:
#       create user accounts on proxmox box assign permissions to VMID and correct overall permissions
#       randomly generate a password for said user account to then print on screen (maybe email?)
#   
#   Web frontend:
#       find out how to actually interlink the two, node.js and wordpress maybe?
#
#
#
  