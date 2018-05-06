# AbletonScripts

This project tries to create a big modular script connection to the Ableton Live API. The goal is to make the API usable to everyone without knowledge of the API or Python.

*Note 1*

For the moment this script is developed for Ableton Live 9, so compatibility for older or newer versions is **not** guaranteed. If anyone wants to check and create this compatibility, let me know!

*Note 2*

This script is tested with the Lemur iPad app. If anyone has wishes for special versions, let me know!

## How to Contribute

Pull requests, issue reports, and suggestions are welcome.

If you are interested in contributing to the code, please fork the
repository and submit pull requests to the `master` branch.

Check the [TODO](TODO.md) to see jobs left to do.

## Usage

Move the `AbletonScripts folder` to the `MIDI Remote Scripts folder`.

***Mac***

This folder can be found on MAC inside the Live application:

`/Applications/Ableton\ Live\ x\ Suite.app/Contents/App-Resources/MIDI\ Remote\ Scripts/`

Reach this by right clicking on the app and click `Show package contents`

***Windows***

This folder can be found on Windows inside the Live application:

`\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts`

When Live start, it will compile the `.py` files and create a bunch of `.pyc` files. When you change something in one of the `.py` files, you need to remove the `.pyc`. This way Ableton will recompile the files on next start.
