#!/bin/sh

if [[ "$(systemctl is-active apache2)" == active ]]; then
    echo "Apache is active"
else
    echo "Apache is ded fam"
fi
