# mcbt
Tool for backing up minecraft worlds on macOS

## Installing
* Open **Terminal** and run these commands:
  * `cd`
  * `git clone https://github.com/NathanK4261/mcbt.git`
  * `cd mcbt`

* Now, open the _"setup"_ file in the _"mcbt"_ directory and change the WORLDS_FOLDER variable to where your minecraft worlds are located, and the BACKUP_DESTINATION variable to the directory in which you mant your worlds to be backed up to. Usually, WORLDS_FOLDER can be changed to _"~/Library/Application Support/minecraft/saves"_.
* Now, run `python setup` to setup the _mcbt_ agent on your computer. Your worlds will be backed up every 30 minutes (unless changed in the script)

**mcbt** should now be installed on your system! A notification will pop up anytime a backup has been completed, and anytime there has been an error.

NOTE: mcbt will only backup to latest version, and will not keep old backups!

## Uninstalling
* Remove the _".plist"_ file from the _"~/Library/LaunchAgents"_ directory
* Delete the file containing the repository, and delete the file containing your backed up minecraft worlds
