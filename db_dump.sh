MONGO_DATABASE="life-api"
MONGO_HOST="127.0.0.1"
MONGO_PORT="27017"
DATESTAMP=`date "+%Y-%m-%d"`
MONGODUMP_PATH="/usr/bin/mongodump"
BACKUPS_DIR="/data/mongodb/backups/$MONGO_DATABASE/$DATESTAMP"

$MONGODUMP_PATH -v -o $BACKUPS_DIR
