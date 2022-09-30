import read_and_create
import module
import os

# list = Pullmino listdir

def organize(list): 

    # Set counter: C:\\Users\\aless\\Desktop\\Pullmino

    dir_counter = f"{module.FATHER}"

    # Check if folder has folder inside

    while len(list) > 0:

    # Loop through folders

        for child in list:

            # If the child is a folder

            if os.path.isdir(child):

                # Set counter: C:\\Users\\aless\\Desktop\\Pullmino\\{child}

                dir_counter = dir_counter + f"\\{child}"
                
                # Go to child

                os.chdir(f"{dir_counter}")

                # Update listdir, rerun While loop

                list = os.listdir()

            # Else if the child is a file

            elif os.path.isfile(child):

                # We need to copy that in a new directory: run read_and_create

                read_and_create.read(dir_counter, child)

    # When there are no childs in a folder we need to remove the folder and go back

    else:
        print("The end")

        # Remove folder

        os.remove(os.getcwd)

        # Back to C:\\Users\\aless\\Desktop\\Pullmino

        os.chdir(f"{module.FATHER}")

        # TODO: Restart the loop?

        return 200

