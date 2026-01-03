import sys
import os
from core import (linux,
                  win,
                  macos)
import time

def main() -> None:
    if sys.platform == "win32": # If it is windows, start code for windows
        pass

    elif sys.platform == "linux": # If it is linux, start code for linux
        sorter: linux.Sorter = linux.Sorter() # Object of sort class
        sorter.move_to_downloads() # Check exectly in downloads
        sorter.make_directories() # Make importatnt dirs
        
        while True:
            time.sleep(60) # Check for new files every minute
            if sorter.check_for_new_files():
                sorter.sort_files()
            else:
                continue

    elif sys.platform == "darwin": # if it is macOS, start code for macOS
        pass