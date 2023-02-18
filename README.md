# DESCRIPTION
A program that opens a list of browser urls using a python script that is compiled to an executable.

# INFO
Only supports Windows (for now)
Used pyinstaller package

# REQUIREMENTS
PyInstaller

# HOW TO USE
- Edit `main.py`'s `URLS` list as you wish

## On windows:
- Run `compile.sh` to compile the exe 
- Run `run.bat` and the windows should open using the system's default web browser.

## On linux:
- Run the script directly using python `python3 main.py`

For ease of usage, create an alias in your .bashrc or .zshrc depending on which shell you use
- `vim .bashrc` or `vim .zshrc`
- add the following line to the bottom of the config `alias morning_news="python3 /path/to/projects/main.py"`
Re-open your shell and type in morning_news to see its effect
