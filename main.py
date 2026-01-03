import os
from pathlib import Path
from typing import Set
import time
import shutil

class Sorter():
    PATH: str = str(Path.home() / "Downloads")
    DOCS_EXT = {".txt", ".doc", ".docx", ".pdf"}
    IMAGES_EXT = {".jpeg", ".png", ".jpg", ".gif"}
    VIDEOS_EXT = {".mov", ".mp4"}
    AUDIO_EXT = {".wav", ".mp3", ".aac", ".flac"}
    PROGRAM_EXT = {".py", ".cpp", ".c", ".h", ".hpp", ".java", ".csharp", ".rust"}
    INITIAL_FILES: Set[str] = set(os.listdir(PATH))

    
    def __init__(self) -> None:
        pass
    
    def move_to_downloads(self) -> None:
        os.chdir(self.PATH) # Move to downloads directory
        
    def check_for_new_files(self) -> bool:
        is_new_files: bool = False
        
        #Check for new files
        current_files: Set[str] = set(os.listdir(self.PATH))
        self.new_files: Set[str] = current_files - self.INITIAL_FILES
        
        if len(self.new_files) != 0:
            print("New files detected!")
            is_new_files = True
            
        return is_new_files

    def make_directories(self) -> None:
        # Make all Directories
        if not "Images" in os.listdir(self.PATH):
            os.mkdir("Images")
        if not "Documents" in os.listdir(self.PATH):
            os.mkdir("Documents")
        if not "Videos" in os.listdir(self.PATH):
            os.mkdir("Videos")
        if not "Programming" in os.listdir(self.PATH):
            os.mkdir("Programming")
        if not "Audio" in os.listdir(self.PATH):
            os.mkdir("Audio")
        if not "Other" in os.listdir(self.PATH):
            os.mkdir("Other")
        
    def sort_files(self) -> None:
        """
        Check for extension in files in sort them
        """
        while True:
            time.sleep(60)
            if self.check_for_new_files():
                
                for f in self.new_files:
                    file: Path = Path(f)
                    
                    # Where file should go
                    if file.suffix.lower() in self.IMAGES_EXT:
                        shutil.move(file, "Images")
                    elif file.suffix.lower() in self.DOCS_EXT:
                        shutil.move(file, "Documents")
                    elif file.suffix.lower() in self.PROGRAM_EXT:
                        shutil.move(file, "Programming")
                    elif file.suffix.lower() in self.AUDIO_EXT:
                        shutil.move(file, "Audio")
                    elif file.suffix.lower() in self.VIDEOS_EXT:
                        shutil.move(file, "Videos")
                    else:
                        shutil.move(file, "Other")

def start_program() -> None:
    sorter: Sorter = Sorter() # Object of sort class
    sorter.move_to_downloads() # Check exectly in downloads
    sorter.make_directories() # Make importatnt dirs
    
    while True:
        sorter.sort_files()
        
def main() -> None:
    start_program()
    
if __name__ == "__main__":
    main()