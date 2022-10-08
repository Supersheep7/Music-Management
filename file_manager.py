from asyncio.windows_events import NULL
from genericpath import exists
import module
import shutil
from tinytag import TinyTag
import os
import re

# Main read func

def read_and_move(og_path, file):

    if file.lower().endswith(('.mp3', '.flac', '.m4a', '.mp4', '.wav', '.wma', '.aac')):
        
        # Get metadata

        audio = TinyTag.get(str(f"{og_path}"))

        # Escape bad meta characters, no meta or bad whitespace

        if audio.artist is None:
            
            artistname = "Unknown Artist"

        else:

            artistname = re.sub(r"[/:*?\"<>|\\]", "-", audio.artist.strip())

        if audio.album is None:

            albumname = "Unknown Album"

        else:

            albumname = re.sub(r"[/:*?\"<>|\\]", "-", audio.album.strip())

        # Create folders, then move file there

        if not exists(f"{module.ENDPOINT}\\{artistname}"):
            
            create(f"{module.ENDPOINT}", f"{artistname}")

        if not exists(f"{module.ENDPOINT}\\{artistname}\\{albumname}"):
            
            create(f"{module.ENDPOINT}\\{artistname}", f"{albumname}")

        shutil.move(og_path, f"{module.ENDPOINT}\\{artistname}\\{albumname}\\{file}")   

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