#! /bin/bash

# Backup my scripts to a zip, with date

fromthis=/root/scripts/
tothis=/root/backup/scripts-$(date "+%Y.%m.%d")-$(date "+%H:%M").tgz

tar -cZf $tothis $fromthis

echo "SCRIPT BACKUP DONE $(date "+%Y.%m.%d")-$(date "+%H:%M")"