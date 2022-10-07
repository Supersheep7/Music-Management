from genericpath import exists
import os
import module
import directory_manager    

def main():

    # Prompt user for directory names

    module.username
    module.father

    # Escape bad input

    if not exists(module.FATHER):
        print("There's no such directory!\nPlease give me a directory to manage, it should be in your \"Documents\" folder")
        return
    if len(os.listdir(module.FATHER)) <= 0:
        print("That folder is empty! Please choose a populated folder")
        return
    module.endpoint

    # Make endpoint directory

    path = os.path.join(f"C:\\Users\\{module.username}\\Documents\\", f"{module.endpoint}")
    if not exists(path):
        os.mkdir(path)

    # Organize
    directory_manager.organize(f"{module.FATHER}")

main()