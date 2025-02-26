import os

def testPath(path):
    if os.path.exists(path):
        print("Path exist")

        if os.path.isdir(path):
            print("It is the folder path")
            print("Directory: ", path)
            print("Filename: ", None)
        else:
            print("Directory: ", os.path.split(path)[0])
            print("Filename: ", os.path.split(path)[1])
    else:
        print("Path does not exist")
    
path = input("Enter the path: ")
testPath(path)