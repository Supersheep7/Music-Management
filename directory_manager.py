from genericpath import exists
import file_manager
import module
import os

# First folder_path = module.FATHER
# Then, when the recursion happens, folder_path will be the "current" folder

def organize(folder_path): 

    # Initialize list for loops (list updates each time organize func gets called)

    list = os.listdir(folder_path)

    # Set counter: C:\\Users\\aless\\Documents\\Pullmino

    dir_counter = folder_path

    # While folder not empty

    while len(list) > 0:

    # Loop through folder

        for child in list:

            # If the child is a folder

            if os.path.isdir(f"{dir_counter}\\{child}"):

                # Set counter: C:\\Users\\aless\\Documents\\Pullmino\\{child}

                dir_counter = dir_counter + f"\\{child}"

                # Organize current folder recursively

                organize(dir_counter)

            # Else if the child is a file

            elif os.path.isfile(f"{dir_counter}\\{child}"):

                # Run read_and_create func

                file_manager.read_and_move(f"{dir_counter}\\{child}", child)
                
                # Restart from the beginning until done

                organize(f"{module.FATHER}")

            # Else if the child is something else

            else:
                
                # Nothing to see here

                return 202

    # When there are no childs in a folder we need to remove the folder and go back

    else:

        # Back to C:\\Users\\aless\\Documents\\Pullmino
        # We need the second condition to avoid module.FATHER destruction
    
        os.chdir(f"{module.FATHER}")
    
        # Remove folder

        os.rmdir(dir_counter)

        # Is module.FATHER still populated?

        if len(os.listdir(f"{module.FATHER}")) > 0:

            # Recursion

            organize(f"{module.FATHER}")

        # Yeah
        
        else: 

            print ("The End")
            return 200


