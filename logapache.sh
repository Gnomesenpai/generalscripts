#!/bin/bash

adddate() {
    while IFS= read -r line; do
        printf '%s %s\n' "$(date)" "$line";
    done
}

/crontab-scripts/apache.sh | adddate >>/var/log/apachereboot.log
