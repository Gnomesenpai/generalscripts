#!/bin/bash

if [ "$(systemctl is-active apache2)" == "active" ]; then
    echo "Apache is active"
else
    echo "Apache is inactive"
    echo "starting Apache2 service..."
    systemctl start apache2
    sleep 1
    systemctl is-active apache2
fi
