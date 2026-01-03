import sys
import os
import time
from pathlib import Path
from typing import Set

class Sorter():
    HOME_DIR: str = os.path.expanduser('~') # Constant of home library
    PATH: Path = Path(f"{HOME_DIR}/Downloads")
    DOCS_EXT = {".txt", ".doc", ".docx"}
    
    def __init__(self) -> None:
        pass
    
    def move_to_downloads(self) -> None:
        os.chdir(self.PATH) # Move to downloads directory
        
    def check_for_new_files(self) -> bool:
        is_new_files: bool = False
        # Get current files
        initial_files: Set[str] = set(os.listdir(self.PATH))
        
        #Check for new files
        current_files: Set[str] = set(os.listdir(self.PATH))
        self.new_files: Set[str] = initial_files - current_files
        
        if self.new_files != 0:
            print("New files detected!")
            is_new_files = True
            
        return is_new_files

    def make_directories(self) -> None:
        # Make all Directories
        if not "Images" in os.listdir(self.PATH):
            os.mkdir("Images")
        elif not "Documents" in os.listdir(self.PATH):
            os.mkdir("Documents")
        elif not "Videos" in os.listdir(self.PATH):
            os.mkdir("Videos")
        elif not "Other" in os.listdir(self.PATH):
            os.mkdir("Other")
        
    def sort_files(self) -> None:
        """
        Check for extension in files in sort them
        """
        for f in self.new_files:
            file: Path = Path(f)
            if file.suffix.lower() in 