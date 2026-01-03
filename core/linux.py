import sys
import os
import time
from pathlib import Path
from typing import Set

class Sorter():
    HOME_DIR: str = os.path.expanduser('~') # Constant of home library
    PATH: Path = Path(f"{HOME_DIR}/Downloads")
    
    def __init__(self) -> None:
        pass
    
    def move_to_downloads(self) -> None:
        os.chdir(self.PATH) # Move to downloads directory
        
    def check_for_new_files(self, interval: int = 5) -> bool:
        self.is_new_files: bool = False
        # Get current files
        initial_files: Set[str] = set(os.listdir(self.PATH))
        
        while True:
            time.sleep(interval)
            #Check for new files
            current_files: Set[str] = set(os.listdir(self.PATH))
            
            if current_files - initial_files != 0:
                print("New files detected!")
                self.is_new_files = True

    def make_directories(self) -> None:
        # Make all Directories
        if not "Images" in os.listdir(self.PATH):
            os.mkdir("Images")
        elif not "Documents" in os.listdir(self.PATH):
            os.mkdir("Documents")
        elif not "Other" in os.listdir(self.PATH):
            os.mkdir("Other")
        
    def sort_files(self) -> None:
        