# Simple Backup

This is a simple backup programm which checks a directory 
for changed files and copies the directory to the given
target directory if something changed.
The check will be done in the frequency of the specified time.
The programm informs the user if a backup was done or not by a desktop notification.

    usage: simple-backup [-h] basedir backupdir backup_frequency

    Checks a directory for changes and performs a backup if something changed

    positional arguments:
      basedir           The directory for which the backups should be done
      backupdir         The directory where the backups should go
      backup_frequency  The frequency how often the check should be performed in seconds

    options:
      -h, --help        show this help message and exit

## How to install
The only dependency is `desktop-notifier`
You can install it by 

    pip install desktop-notifier
