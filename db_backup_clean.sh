BACKUP_DIR="/data/mongodb/backups/life-api";

find $BACKUP_DIR/* -type d -ctime +7 | sudo xargs rm -rf
