# mcbt
Tool for backing up minecraft worlds on macOS

## Installing
* Open **Terminal** and run these commands:
  * `cd`
  * `git pull https://github.com/NathanK4261/mcbt.git`
  * `cd mcbt`

* Now, open _"setup"_ file in the _"mcbt"_ directory and change the WORLDS_FOLDER and BACKUP_DESTINATION variables to where your minecraft worlds are located. Usually, WORLDS_FOLDER can be changed to _"~/Library/Application Support/minecraft/saves"_.
  * `python setup `

**mcbt** should now be installed on your system! A notification will pop up anytime a backup has been completed, and anytime these has been an error

## Uninstalling
* Remove the _".plist"_ file from the _"~/Library/LaunchAgents"_ directory
