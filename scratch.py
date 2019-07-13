#!/usr/bin/python3
#!/usr/bin/env python3

import os
import time
import getpass
import random
#lets define some things
#web panel stuff


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