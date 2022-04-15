#!/usr/bin/python3
#!/usr/bin/env python3


#TO TO:
# re-write using hwinfo --disks --short for disk information
# assume os is installed on /dev/sda and asume b-z is in nuking range
#
import os
import string
import getpass
import time
print("This script requires ROOT")
time.sleep(1)
usercheck = os.popen('whoami').read() 
print(usercheck)




if usercheck == 'root':
    print("This script requires hwinfo")
    print("THIS UTILITY CAN WIPE ALL DATA!!!!!!")
    confirmdelete1 = str(input("Are you sure you wish to continue? (yes/no): ")).lower()

    confirmdelete2 = str(input("Are you REALLY sure you wish to continue? (yes/no): ")).lower()
    print ("yes")
    if confirmdelete1 == 'yes' and confirmdelete2 == 'yes':
        print("responses match")
        #fdisk = 'fdisk --list | grep  "Disk /dev/" | grep -v  -i 'Partition 2''
        diskinfo = 'hwinfo --disk --short'

        #os.system(fdisk)
        os.system(diskinfo)
    else:
        print("Responses dont match")
        exit()

else:   
    print("Not root! Exiting...")
    exit()

#this isnt finished