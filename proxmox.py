#!/usr/bin/python3
#!/usr/bin/env python3
#testing information using psutil
#install psutil with "pip3 install psutil"
import psutil

#lets define some things
host="<proxmoxurl>"
port="<port>"

#maybe use SSH keys instead? for testing purposes user&pass will do
user="<username>"
password="<password>"

lxcstart = str(input("Would you like to create or delete an LXC? Enter Create or delete:\n>"))
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

    #answer = int(input("Select aount of vcores: "))
    #also need to forward number
    #answer = int(input("Select RAM in GB: "))
    #same issue
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

    print=('vmid')
    #example final string: pct create 999 local:vztmpl/debian-8.0-standard_8.0-1_amd64.tar.gz

elif lxcstart in ['delete']:
    print("ruh roh, you're getting deleted kiddo")

elif lxcstart in ['info']:
    print("Lets get some information!\n")
    print('CPU Usage:', psutil.cpu_percent()),     
    #print(psutil.virtual_memory())  # physical memory usage
    print('memory used in %:', psutil.virtual_memory()[2])

else:
    print("No option selected! Exiting!")