import sys
import os
from core import (linux,
                  win,
                  macos)
import time

def start_program() -> None:
    if sys.platform == "win32": # If it is windows, start code for windows
        pass

    elif sys.platform == "linux": # If it is linux, start code for linux
        sorter: linux.Sorter = linux.Sorter() # Object of sort class
        sorter.move_to_downloads() # Check exectly in downloads
        sorter.make_directories() # Make importatnt dirs
        
        while True:
            sorter.sort_files()

    elif sys.platform == "darwin": # if it is macOS, start code for macOS
        pass

def main() -> None:
    start_program()
    
if __name__ == "__main__":
    main()