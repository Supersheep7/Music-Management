import os

username = os.getlogin()
father = input("Give me the name of the folder you wish to manage: \n")
endpoint = input("Give me the name of the destination folder: \n")

# Setup variables

FATHER = f"C:\\Users\\{username}\\Documents\\{father}"
ENDPOINT = f"C:\\Users\\{username}\\Documents\\{endpoint}"
