from asyncio.windows_events import NULL
from genericpath import exists
import module
import shutil
from tinytag import TinyTag
import os

# Main read func

def read_and_move(og_path, file):

    if file.lower().endswith(('.mp3', '.flac', '.m4a', '.mp4', '.wav', '.wma', '.aac')):
        
        # Get metadata

        audio = TinyTag.get(str(f"{og_path}"))
        
        if not exists(f"{module.ENDPOINT}\\{audio.artist}"):
            
            create(f"{module.ENDPOINT}", f"{audio.artist}")

        if not exists(f"{module.ENDPOINT}\\{audio.artist}\\{audio.album}"):
            
            create(f"{module.ENDPOINT}\\{audio.artist}", f"{audio.album}")

        shutil.move(og_path, f"{module.ENDPOINT}\\{audio.artist}\\{audio.album}\\{file}")   

        return

    # Media manager (It should work better...)

    else:

        dir_finder = og_path.rsplit("\\")
        directory = dir_finder[-2]

        if not exists(f"{module.ENDPOINT}\\_Media"):

            create(f"{module.ENDPOINT}", "_Media")

        if not exists(f"{module.ENDPOINT}\\_Media\\{directory}"):

            create(f"{module.ENDPOINT}\\_Media", f"{directory}")

        shutil.move(og_path, f"{module.ENDPOINT}\\_Media\\{directory}\\{file}")


# Submain create function

def create(father, child):
    
    # What's your name?

    path = os.path.join(f"{father}", f"{child}")

    # Create

    if not exists(path):

        os.mkdir(path)

    # Return newborn path

    return str(f"{path}")