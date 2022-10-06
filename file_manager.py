from asyncio.windows_events import NULL
from genericpath import exists
import module
import shutil
from tinytag import TinyTag
import os

# Main read func

def read_and_move(og_path, file):

    # Our file is an audio one?

    if file.lower().endswith(('.mp3', '.flac', '.m4a', '.mp4', '.wav', '.wma', '.aac')):
        
        # Get metadata

        audio = TinyTag.get(str(f"{og_path}"))
        
        # Create artist folder
        
        if not exists(f"{module.ENDPOINT}\\{audio.artist}"):
            create(f"{module.ENDPOINT}", f"{audio.artist}")
        
        # Create album folder

        if not exists(f"{module.ENDPOINT}\\{audio.artist}\\{audio.album}"):
            create(f"{module.ENDPOINT}\\{audio.artist}", f"{audio.album}")

        # Move file in album folder

        shutil.move(og_path, f"{module.ENDPOINT}\\{audio.artist}\\{audio.album}\\{file}")   

        return

    # Nah, burn it

    else:
            os.remove(og_path)

# Submain create function

def create(father, child):
    
    # What's your name?

    path = os.path.join(f"{father}", f"{child}")

    # Create

    if not exists(path):

        os.mkdir(path)

    # Return newborn path

    return str(f"{path}")