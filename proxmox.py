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

answer = str(input("Would you like to create or delete an LXC? Enter Create or delete:\n>"))
print('\n')
if answer in ['create']:
    print("this is the create script")
    answer = str(input("Pick an ID:\n>"))
    #need to get the ID entered by the user
    answer = str(input("Select aount of vcores:\n>"))
    #also need to forward number
    answer = str(input("Select RAM"))
    #same issue


    #example final string: 

elif answer in ['delete']:
    print("ruh roh, you're getting deleted kiddo")

elif answer in ['info']:
    print("Lets get some information!\n")
    print('CPU Usage:', psutil.cpu_percent()),     
    #print(psutil.virtual_memory())  # physical memory usage
    print('memory used in %:', psutil.virtual_memory()[2])

else:
    print("No option selected!")