import os

def delete(path):
    if os.path.exists(path) and os.path.isfile(path):
        print("Path exist")
        
        print("Access to read: ", os.access(path, os.R_OK))
        print("Access to execute: ", os.access(path, os.X_OK))
        print("Access to write: ", os.access(path, os.W_OK))

        os.remove(os.path.split(path)[1])
        
        if not (os.path.exists(path)):
            print("File successfully deleted!")
        else:
            print("File is not deleted...")
    else:
        print("Path does not exist or it is the path to directory, not for file")

path = input("Path: ")
delete(path)