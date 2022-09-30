from asyncio.windows_events import NULL
import module
import shutil
from tinytag import TinyTag
import os


# Debug Organizer

# og_path =  C:\\Users\\aless\\Desktop\\Pullmino\\{child} e.g. C:\\Users\\aless\\Desktop\\Pullmino\\Artist\\Album\\Hallelujah.mp3
# file = {child} e.g. Hallelujah.mp3


# Main

def read(og_path, file):

    # OK: Get audio metadata and store into audio obj

    audio = TinyTag.get(str(file))

    ######### Escape bad meta ######### 

    # If there are no meta about anything

    if audio.album == NULL and audio.artist == NULL:

        # Create Unknown Artist folder

        unknown_artist_folder = create("Unknown Artist")

        # Go there

        os.chdir(unknown_artist_folder)

        # Create Unknown Album folder

        unknown_album_folder = create("Unknown Album")    

        # Move file there

        shutil.move(og_path, f"{unknown_album_folder}\\{file}")

    # If there are no meta about the album

    elif audio.album == NULL:

        # Create unknown album folder
        
        unknown_album_folder = create(og_path, "Unknown Album")

        # Move file to unknown album folder

        shutil.move(og_path, f"{unknown_album_folder}\\{file}")

        # Move unknown album folder to artist folder

        shutil.move(unknown_album_folder, f"{module.ENDPOINT}\\{audio.artist}")

    # If there are no meta about the artist

    elif audio.artist == NULL:

        # Create unknown artist folder

        unknown_artist_folder = create("Unknown Artist")

        # Move file to new album folder

        shutil.move(og_path, f"{module.ENDPOINT}\\{audio.album}")

        # Move new album folder to Unknown artist Folder

        shutil.move(f"{module.ENDPOINT}\\{audio.album}", unknown_artist_folder)

    
    ######### OK: We've got everything, let's go #########
    
    else:
        
        # OK: Create

        artist_folder = create(f"{module.ENDPOINT}\\{audio.artist}")
        album_folder = create(f"{artist_folder}\\{audio.album}")

        # OK: Move

        shutil.move(og_path, f"{album_folder}\\{file}")       

# Submain create function

def create(end):

    # TODO: func
    
    # If there are no folders with that name

        # Create

    # Else 

        # Nope

    # Return newly created path

    # TODO: We need to return a string

    return