#!/usr/bin/python3
#!/usr/bin/env python3

import os
import string

print("THIS UTILITY CAN WIPE ALL DATA!!!!!!")
confirmdelete1 = str(input("Are you sure you wish to continue? (yes/no): ")).lower()

confirmdelete2 = str(input("Are you REALLY sure you wish to continue? (yes/no): ")).lower()


if confirmdelete1 == 'yes' and confirmdelete2 == 'yes':
    print("responses match")
    fdisk = 'fdisk --list | grep  "Disk /dev/" | grep -v  -i 'Partition 2''
'
    os.system(fdisk)
else:
    print("Responses dont match")
    exit()

#this isnt finished