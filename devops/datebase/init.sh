#!/bin/bash

# Replace these variables with your own
MONGO_HOST="localhost"
MONGO_PORT="27017"

# Run Mongo command to create new database
mongo --host $MONGO_HOST --port $MONGO_PORT --eval 'db = db.getSiblingDB("dazi"); db.createCollection("sample");'
