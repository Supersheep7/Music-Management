from genericpath import exists
import module
import os
import directory_manager    

# TODO: Fix the media problem
# TODO: Make it for everyone
# TODO: Check line 53 in organize.py

def main():

    father = input("Who's your daddy?")
    endpoint = input("What's your endpoint?")

    # Make endpoint directory

    path = os.path.join("C:\\Users\\aless\\Documents\\", "Endpoint")
    if not exists(path):
        os.mkdir(path)

    # Organize
    directory_manager.organize(f"{module.FATHER}")

main()