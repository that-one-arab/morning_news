#!/bin/bash
# Compiles main.py into an executable.


echo compiling...
# Run pyinstaller on main.py
python3 -m  PyInstaller main.py

echo ...finished!