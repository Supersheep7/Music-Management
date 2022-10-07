from genericpath import exists
import file_manager
import module
import os

# First folder_path = module.FATHER
# Then, when the recursion happens, folder_path will be the "current" folder

def organize(folder_path): 

    # Initialize list for loops (list updates each time organize func gets called)

    list = os.listdir(folder_path)

    # Set counter: C:\\Users\\user\\Documents\\father

    dir_counter = folder_path

    # While folder not empty

    while len(list) > 0:

        for child in list:

            if os.path.isdir(f"{dir_counter}\\{child}"):

                # Set counter: C:\\Users\\aless\\Documents\\Pullmino\\{child}

                dir_counter = dir_counter + f"\\{child}"

                # Organize current folder recursively

                organize(dir_counter)

            elif os.path.isfile(f"{dir_counter}\\{child}"):

                file_manager.read_and_move(f"{dir_counter}\\{child}", child)
                
                # Restart from the beginning until done

                organize(f"{module.FATHER}")

            else:

                return 202

    # When there are no childs in a folder we need to remove the folder and go back

    else:

        # Back to C:\\Users\\user\\Documents\\father
    
        os.chdir(f"{module.FATHER}")
    
        # Remove last folder

        os.rmdir(dir_counter)

        # Is module.FATHER still populated?

        if len(os.listdir(f"{module.FATHER}")) > 0:

            # Recursion

            organize(f"{module.FATHER}")
        
        else: 

            print (f"Done! You can find your results in {module.ENDPOINT}")
            return 200


