# mcbt
Tool for backing up minecraft worlds on macOS

## Installing
* Open **Terminal** and run these commands:
  * `cd`
  * `git pull https://github.com/NathanK4261/mcbt.git`
  * `cd mcbt`

* Now, open the _"setup"_ file in the _"mcbt"_ directory and change the WORLDS_FOLDER variable to where your minecraft worlds are located, and the BACKUP_DESTINATION variable to the directory in which you mant your worlds to be backed up to. Usually, WORLDS_FOLDER can be changed to _"~/Library/Application Support/minecraft/saves"_.
* Now, run `python setup` to setup the _mcbt_ agent on your computer. Your worlds will be backed up every 30 minutes (unless changed in the script)

**mcbt** should now be installed on your system! A notification will pop up anytime a backup has been completed, and anytime these has been an error

## Uninstalling
* Remove the _".plist"_ file from the _"~/Library/LaunchAgents"_ directory
