#!usr/bin/python3
import os

#lets define some things!
html = "~/html_files/foragingcompanion"
giturl = "<url>"
#remove directory "map"
remove = 'rm -Rv %s/map' %s (html)
os.system(remove)

#git clone new
clone = 'git clone %s %s' % (giturl, html)
os.system(clone)