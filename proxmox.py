#!/usr/bin/python3

#lets define some things
host="<proxmoxurl>"
port="<port>"

#maybe use SSH keys instead? for testing purposes user&pass will do
user="<username>"
password="<password>"

answer = str(input("Would you like to create or delete an LXC? Enter Create or delete:\n"))
print('\n')
if answer in ['create']:
    print("this is the create script")

elif answer in ['delete']:
    print("ruh roh, you're getting deleted kiddo")
    