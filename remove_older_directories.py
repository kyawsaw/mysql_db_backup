#!/usr/bin/env python3

import os
import shutil
import time

def delete_old_directories(root_dir, days_old):
    # Convert days to seconds 86400
    cutoff_time = time.time() - (days_old * 86400)

    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            dir_to_check = os.path.join(dirpath, dirname)
            try:
                dir_created_time = os.path.getctime(dir_to_check)
                
                if dir_created_time < cutoff_time:
                    print(f"Deleting directory: {dir_to_check}")
                    shutil.rmtree(dir_to_check)
            except Exception as e:
                print(f"Error deleting directory {dir_to_check}: {e}")

if __name__ == "__main__":
    root_directory = "/home/vagrant/backups/db_backups"  
    days_threshold = 15  
    
    delete_old_directories(root_directory, days_threshold)