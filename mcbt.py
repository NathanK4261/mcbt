#!/usr/bin/env python3

# For licensing information, see the "LICENSE" text file
import subprocess as sp
import time

# Config variables
WORLDS_FOLDER = ''
BACKUP_DESTINATION = ''

def backup_worlds():
    try:
        # Perform the backup using cp command
        result = sp.run(f'cp -r "{WORLDS_FOLDER}"/* "{BACKUP_DESTINATION}"', shell=True, capture_output=True, text=True)

        # Check return code
        if result.returncode == 0:
            sp.run(['osascript', '-e', 'display notification "Backup complete!" with title "mcbt"'])
            
        else:
            # Notify about backup error
            error_message = result.stderr.strip() if result.stderr else ""
            sp.run(['osascript', '-e', f'display notification "Error: {error_message}" with title "mcbt"'])
            
    except Exception as e:
        # Handle any unexpected exceptions
        sp.run(['osascript', '-e', f'display notification "Exception: {e}" with title "mcbt"'])

if __name__ == "__main__":
    while True:
        backup_worlds()
        time.sleep(1800)  # Sleep for 30 minutes before next backup
