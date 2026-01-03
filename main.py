import sys
import os
from core import (linux,
                  win,
                  macos)

def main() -> None:
    if sys.platform == "win32": # If it is windows, start code for windows
        pass

    elif sys.platform == "linux": # If it is linux, start code for linux
        sorter: linux.Sorter = linux.Sorter() # Object of sort class
        sorter.move_to_downloads() # Check exectly in downloads
        sorter.make_directories() # Make importatnt dirs
        
        while True:
            if sorter.check_for_new_files():
                

    elif sys.platform == "darwin": # if it is macOS, start code for macOS
        pass