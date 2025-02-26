import os

def listDF(path):
    try:
        print("Directories:")
        for item in os.listdir(path): #выводит все элементы в указанном пути
            if os.path.isdir(os.path.join(path, item)): #проверяет, является ли элемент директорией
                print(item)

        print("\nFiles:")
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path, item)): #проверяет, является ли элемент файлом
                print(item)

        print("\nAll Directories and Files:")
        for root, dirs, files in os.walk(path): #обходит все
            for dir_name in dirs:
                print("Directory:", os.path.join(root, dir_name))
            for file_name in files:
                print("File:", os.path.join(root, file_name))
    except FileNotFoundError:
        print("The specified path does not exist.")
    except Exception as e:
        print("An error occurred:", e)

path = input("Enter the path: ")
listDF(path)