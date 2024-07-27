#!/usr/bin/env python3

import os
from datetime import datetime

# List of databases to backup // {edit path to list}
DB_NAME='/home/vagrant/backups/db_names_list.txt'

# Directory to store backups // {edit path to backup}
BACKUP_PATH='/home/vagrant/backups/db_backups'

# Getting current DateTime to create the separate backup folder like "2024-07-27"
DATETIME = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
TODAY_BACKUP_PATH = f"{BACKUP_PATH}/{DATETIME}"

# Checking if backup folder already exists or not. If not exists will create it.
try:
    os.stat(TODAY_BACKUP_PATH)
except:
    os.makedirs(TODAY_BACKUP_PATH, exist_ok=True)

# Checking if you want to take single database backup or assinged multiple backups in database_names_list.txt
print ("checking for databases names file.")
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print ("Databases file found...")
    print (f"Starting backup of all dbs listed in file {DB_NAME}")
else:
    print ("Databases file not found...")
    print (f"Starting backup of database {DB_NAME}")
    multi = 0

# Starting actual database backup process.
if multi:
   in_file = open(DB_NAME,"r")
   flength = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(DB_NAME,"r")

   while p <= flength:
       db = dbfile.readline()   # reading database name from file
       db = db[:-1]         # deletes extra line
       timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
       dump_command = f"mysqldump {db} > {TODAY_BACKUP_PATH}/{db}_{timestamp}.sql"

       os.system(dump_command)
       # Tar gzip
       gzipcmd = f"gzip {TODAY_BACKUP_PATH}/{db}_{timestamp}.sql"
       os.system(gzipcmd)

       p = p + 1
   dbfile.close()
else:
   db = DB_NAME
   timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
   dump_command = f"mysqldump {db} > {TODAY_BACKUP_PATH}/{db}_{timestamp}.sql"
   
   os.system(dump_command)
   # Tar gzip
   gzipcmd = f"gzip {TODAY_BACKUP_PATH}/{db}_{timestamp}.sql"
   os.system(gzipcmd)

print (f"Backup script completed")
print (f"Your backups have been created in {TODAY_BACKUP_PATH} directory")