#!/bin/bash

#remove the directory "map"
rm -Rv ~/html_files/foragingcompanion/map

#clone new files to base directory, git has name of "map" so directory will be re-created
git clone <url> ~/html_files/foragingcompanion/

echo $(date '+%d %b %Y %H:%M:%S')."- Complete";
echo "-----"
