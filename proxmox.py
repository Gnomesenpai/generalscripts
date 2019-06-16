#!/usr/bin/python3
#!/usr/bin/env python3

import os

#lets define some things
port= <port>
user= "<user>"
host = "<host>"

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
lxcstart = str(input("Would you like to create or delete an LXC? Enter Create or delete or type info for information:\n>"))
print('\n')
if lxcstart in ['create']:
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
    id = vmid("Select an ID:")
    #need to get the ID entered by the user
    operatingsystem = str(input("Chose an OS (Debian, Ubuntu): "))
    if operatingsystem in ['debian']:
        print("Debian 9 has been selected!\n")
        #things here
    elif operatingsystem in ['ubuntu']:
        print("Ubuntu has been selected!\n")
        #things here
    else:
        print("Please select an option")
        #loop here to OS select again 
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
    id = vcore("Select vCores: ")
    #print(type(vcore))

    def ram(message):
        while True:
            try:
                ram = int(input("Select RAM in GB: "))
            except ValueError:
                print("Please select a valid input.")
                continue
            else:
                return ram
                break
    id = ram("Select RAM in GB: ")
    #print(ram)
    #ram2 = "%d" % (ram)
    #print(ram2)
    #example final string: pct create 999 local:vztmpl/debian-8.0-standard_8.0-1_amd64.tar.gz
    #example network string 2:pct set 999 -net0 name=eth0,bridge=vmbr0,ip=<ip address>/cidr,gw=<gateway>

elif lxcstart in ['delete']:
    print("ruh roh, you're getting deleted kiddo")

elif lxcstart in ['info']:
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
    #print(port)
    #print(user)
    #print(host)

    #datainput = "'ls -la'"
    #mycmd = 'ssh -p 8222 root@nagisa.gnome.moe "ls -la"'
    #mycmd = 'ssh -p %d %s@%s %s' % (port, user, host, datainput)
    #os.system(mycmd)