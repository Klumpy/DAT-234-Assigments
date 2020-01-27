#! /bin/bash

# Backup my NOTES to a zip, with date

fromthis=/root/Notebooks/
tothis=/root/backup/notes-$(date "+%Y.%m.%d")-$(date "+%H:%M").tgz

tar -cZf $tothis $fromthis

echo "NOTES BACKUP DONE $(date "+%Y.%m.%d")-$(date "+%H:%M")"