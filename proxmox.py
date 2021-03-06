#!/usr/bin/python3
#!/usr/bin/env python3

import os
import time
import getpass
import random
import subprocess
import string
import crypt
#lets define some things
#web panel stuff
webprotocol = "https"
webpanelport = 8123 # Web access port
#host = "nagisa.gnome.moe" #hostname or IP of proxmox management
userrole = "vps" #E.g. PVEAdmin
backupgroup = "vps-backup-users" # usergroup for backup drives?
#backend stuff
port= 8222 # SSH port
user= "root" # ROOT is required to use pveam/pvesh
nodeid = "miku" #node ID
templatestorage = "templates" #location of ISO/cache folder (local on new install) 
templatelocation = "vztmpl" #generally never needs to change
vmstoragelocation = "sas10k" #default local-zfs or local-lvm on fresh install
# use SSH keys instead of usename & password
#below here shouldn't need modifying by end users?
#testting

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

print("Proxmox Root is required to use API functions.")
host = str(input("hostname/ip: "))
#user = str(input("Root login: "))
pword = getpass.getpass('Password: ')
print("Updating LXC template cache")
lxccache = 'pveam update'
lxccache2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxccache)
os.system(lxccache2)
print("Done!")
time.sleep(1)

#start main program
creation = str(input("Would you like to create or delete an LXC? Enter Create or delete or type info for information:\n>"))

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
    
    #start template download (optional)
    lxccurrenttemplate = 'pveam available --section system'# % (templatestorage, templatelocation)
    lxccurrenttemplate2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxccurrenttemplate)
    os.system(lxccurrenttemplate2)
    osdownload = str(input("would you like to download a template? "))
    if osdownload in ['yes']:
        print("Lets go!")
        osdownload2 = str(input("Plese enter the complete template name: "))

        osdownload3 = 'pveam download  %s %s' % (templatestorage, osdownload2)

        osdownload4 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, osdownload3)

        os.system(osdownload4)
    else:
        print("Ok, skipping!")


    #end template download
    
    #start OS selection
    lxcdownloaded = 'pvesm list %s -content %s' % (templatestorage, templatelocation)
    lxcdownloaded2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxcdownloaded)
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
        #static network gateway
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
    initialnetworkvlan = input("Please select a VLAN, leave blank for none: ")
    # start password generator
    def randompassword():
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        # + string.punctuation
        #chars = string.printable
        size = random.randint(10, 10)
        return ''.join(random.choice(chars) for x in range(size))
    pass2 = randompassword()
    pass3 = randompassword()
    
    print('Random password generated!')
    time.sleep(3)
    #end password generator
    #print('Creating LXC Container ID %d with Operating system %s') % (vmid2, ostemplateid)
    finalstring = 'pvesh create /nodes/%s/lxc -vmid %d -hostname %s -storage %s -cores %d -memory %d -swap 0 -ostemplate %s:%s/%s -rootfs %d -unprivileged -password %s -swap 0' % (nodeid, vmid2, vmhostnameid, vmstoragelocation, vcoreid, ramid, templatestorage, templatelocation, ostemplateid, hddsize, pass2) #s-size %d
    finalstring2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, finalstring)
    os.system(finalstring2)
    lxccreation = 'LXC %d has been created' % (vmid2)
    print(lxccreation)
    time.sleep(5)
    #lets do some networking
    networstring = 'pvesh set /nodes/%s/lxc/%d/config -net0 bridge=vmbr0,ip=%s,gw=%s,name=eth0,type=veth' % (nodeid, vmid2, networkingipaddr2, networkinggw2, )
    networstring2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, networstring)
    os.system(networstring2)
    # vlan ,tag=%d
    if (initialnetworkvlan.isdigit()):
        print("vlans")
    else:
        print("onwards!")
    # if (x.isDigit())
    #print completion
    lxcnetworkcreation = 'LXC %d network has been configured' % (vmid2)
    print(lxcnetworkcreation)    
    time.sleep(5)
    #backup base configuration/install
    #basebackup1 = 'pvesh create /nodes/nagisa/vzdump -vmid %s -storage baselxc -compress 1 -mode snapshot' % (vmid2)
    #basebackup2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, basebackup1)
    #completed = subprocess.check_output(basebackup2, shell=True)
    #starting LXC
    print('Starting LXC, wait 10 seconds:')
    lxcstart = 'pvesh create /nodes/%s/lxc/%d/status/start' % (nodeid, vmid2)
    lxcstart2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxcstart)
    os.system(lxcstart2)
    time.sleep(10)
    #pulling LXC status
    lxcstatus = 'pvesh get /nodes/%s/lxc/%d/status/current' % (nodeid, vmid2)
    lxcstatus2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxcstatus)
    os.system(lxcstatus2)
    #print password creation
    passwordoutput = 'Your Root password is: %s please note it down!' % (pass2)
    print(passwordoutput)
    time.sleep(1)
    print('adding user to lxc')


    #
    #start of user creation for Proxmox web panel
    #
    def username(message):
        while True:
            try:
                username = str(input("Please enter a your forename for your user account:\n>"))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return username
                break
    username2 = username("Please enter a your forename for your user account:\n>")
    email1 = str(input("Please enter your email address:\n>"))

    #uuid creation
    uuidoptions = "01234567890"
    uuidlen = 4
    uuid2 =  "".join(random.sample(uuidoptions ,uuidlen ))
    uuid1 = uuid2
    #end uuid creation
    #user creation
    usercreation1 = 'pvesh create /access/users --userid %s_%s@pve -password %s -groups %s -email %s' % (username2, uuid2, pass3, backupgroup, email1)
    usercreation2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, usercreation1)   
    os.system(usercreation2)
    userpassoutput = 'Your Username is: %s_%s \npassword is: %s' % (username2, uuid2, pass3)
    print(userpassoutput)
    print("Assigning permissions to LXC")
    permissions1 = 'pvesh set /access/acl --path /vms/%d --roles %s --users %s_%s@pve' % (vmid2, userrole, username2, uuid2)
    permissions2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, permissions1)   
    os.system(permissions2)
    print("Permissions assigned!")
    weboutput1 = ('Website accessible through %s://%s:%d') % (webprotocol, host, webpanelport)
    print(weboutput1)
    ipoutput = ('LXC IP address is %s') % (networkingipaddr2)
    print(ipoutput)
    #encrypt lxc root password to sha512 to inject
    hashpass = crypt.crypt('%s', crypt.mksalt(crypt.METHOD_SHA512)) % (pass2)
    #inject created lxc root user into LXC
    lxcuser1 = '/usr/sbin/useradd -m -p %s -s /bin/bash  %s_%s' % (hashpass, username2, uuid2)
    lxcuser2 = 'pct exec %d -- bash -c %s'  % (vmid2, lxcuser1)
    os.system(lxcuser1)


    #string:        pvesh set /access/acl --path /vms/336 --roles vps --users testuser2@pve

elif creation in ['delete']:
    print("ruh roh, you're getting deleted kiddo")
    deletion = str(input("Please select the type you would like to delete qemu/lxc/user:\n>"))
    # AUTHENTICATION NEEDED
    #  POSSIBLE POLLING OF ROOT TO PROVE AUTH?

    if deletion in ['qemu']:
        print('qemu deletion')
        qemulist1 = 'pvesh get /nodes/%s/qemu' % (nodeid)
        qemulist2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, qemulist1)
        os.system(qemulist2)
        qemudelete = int(input("Please select a VMID: "))
        confirmdelete1 = str(input("Are you sure you wish to continue? (yes/no): ")).lower()
        confirmdelete2 = str(input("Are you REALLY sure you wish to continue? (yes/no): ")).lower()
        
        if confirmdelete1 == 'yes' and confirmdelete2 == 'yes'::
            deletepw = getpass.getpass('Please re-enter Root password: ')
            #THIS CODE WILL DELETE THE CHOSEN VM
            qemudelete1 = 'pvesh delete /nodes/%s/qemu/%d' % (nodeid, qemudelete)
            qemudelete2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (deletepw, port, user, host, qemudelete1)
            print('VM {} deleted'.format(qemudelete))
        else:
            print("Responses dont match")
    
    elif deletion in ['lxc']:
        print('lxc deletion')
        lxclist1 = 'pvesh get /nodes/%s/lxc' % (nodeid)
        lxclist2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxclist1)
        os.system(lxclist2)
        lxcdelete = int(input("Please select a VMID: "))  
        confirmdelete1 = str(input("Are you sure you wish to continue? (yes/no): ")).lower()
        confirmdelete2 = str(input("Are you REALLY sure you wish to continue? (yes/no): ")).lower()
        if confirmdelete1 == 'yes' and confirmdelete2 == 'yes':
            #THIS CODE WILL DELETE THE CHOSEN LXC
            #STOP THE LXC
            lxcstop1 = 'pvesh create /nodes/%s/lxc/%d/status/stop' % (nodeid, lxcdelete)
            lxcstop2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxcstop1)
            os.system(lxcstop2)
            time.sleep(2)
            #GET LXC STATUS
            lxcstatus = 'pvesh get /nodes/%s/lxc/%d/status/current' % (nodeid, lxcdelete)
            lxcstatus2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxcstatus)
            os.system(lxcstatus2)
            #DELETE THE LXC
            lxcdelete1 = 'pvesh delete /nodes/%s/lxc/%d' % (nodeid, lxcdelete)
            lxcdelete2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxcdelete1)
            os.system(lxcdelete2)
            print('VM {} deleted'.format(lxcdelete))
            print("yeet")
        else:
            print("Responses dont match")
    elif deletion in ['user']:
        print("User deletion")
    else:
        print('NO OPTION SELECTED, EXITING!')

    #print('returncode:', completed.returncode)

elif creation in ['info']:
    print("Polling system information, please wait!")
    #get pve version
    proxversion = "'pvesh get /version'"
    proxversion2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, proxversion)
    #get uptime
    proxuptime = "'uptime'"
    proxuptime2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, proxuptime)
    #get storage information
    proxstorage = "'df -h'"
    proxstorage2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, proxstorage)
    #get quemu status
    qemulist1 = 'pvesh get /nodes/%s/qemu' % (nodeid)
    qemulist2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, qemulist1)
    #get lxc status
    lxclist1 = 'pvesh get /nodes/%s/lxc' % (nodeid)
    lxclist2 = 'sshpass -p %s ssh -p %d %s@%s %s' % (pword, port, user, host, lxclist1)
    print("Proxmox Information:\n")
    os.system(proxversion2)
    print("\n")
    print("Server Uptime:\n")
    os.system(proxuptime2)
    print("\n")
    print("Disk and mapping usage:\n")
    os.system(proxstorage2)
    print("\n")
    print("Qemu list:\n")
    os.system(qemulist2)
    print("\n")
    print("LXC list:\n")
    os.system(lxclist2)
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
  