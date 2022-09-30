from genericpath import exists
import module
import os
import organize
    


def main():

    # Set endpoint

    path = os.path.join("C:\\Users\\aless\\Desktop\\", "Endpoint")
    if not exists(path):
        os.mkdir(path)

    # Get to bus

    os.chdir(f"{module.FATHER}")
    
    # Organize

    organize.organize(os.listdir())

main()