import datetime
import os
import shutil
import time
import argparse
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

def get_latest_mtime(directory):
    """
    Walks over the whole directory and checks for all files the latest m_time.
    """
    latest_mtime = 0
    for root, dirs, files in os.walk(directory):
        for single_file in files:
            mtime = os.path.getmtime(os.path.join(root, single_file))
            if mtime > latest_mtime:
                latest_mtime = mtime
    return latest_mtime


def get_backupdir(backupdir):
    """
    Generates a string consisting of date and time and appends it 
    to the directory name to be saved.
    """
    date = datetime.datetime.now().strftime('%Y-%m.%d_%Hh%Mm%Ss')
    return backupdir+'_'+date


def perform_backup(basedir, backupdir):
    backupstore = os.path.join(backupdir, get_backupdir(basedir))
    shutil.copytree(basedir, backupstore)


if __name__=="__main__":
    parser = argparse.ArgumentParser(prog="simple-backup",
            description="Checks a directory for changes and performs a backup if something changed")

    parser.add_argument("basedir", help="The directory for which the backups should be done")
    parser.add_argument("backupdir", help="The directory where the backups should go")
    parser.add_argument("backup_frequency", help="The frequency how often the check should be performed in seconds")
    args = parser.parse_args()
    basedir = args.basedir
    backupdir = args.backupdir
    BUfrequency = int(args.backup_frequency)
    
    perform_backup(basedir, backupdir)
    note_str = "Directory was saved.\n"+get_backupdir(basedir)
    
    notifier.send_sync(title="Backup", message=note_str)
    time_of_last_BU = time.time()
    time.sleep(BUfrequency)

    while True:
        
        latest_mtime = get_latest_mtime(basedir)
        if time_of_last_BU < latest_mtime:                    
            perform_backup(basedir, backupdir)
            time_of_last_BU = time.time()
            time.sleep(BUfrequency)

            # Notification after a backup:
            note_str = "Directory was saved\n"+get_backupdir(basedir)
            notifier.send_sync(title="Backup", message=note_str)
            time.sleep(BUfrequency)
        
        else:
            #Notification if there was no backup done:
            note_str = "Directory was not saved.\nLast Change: " + time.ctime(latest_mtime)
            notifier.send_sync(title="Backup", message=note_str)
            time.sleep(BUfrequency)





