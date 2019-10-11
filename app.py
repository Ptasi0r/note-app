import sys
import os

#todo jezeli ostatnie jest rozszerzenie lub podano tylko nazwę notatka tworzy się w domyśnyn folderze.


def create_file():
    print("Hello CMD!")
    # print(sys.argv)
    file_name = str(sys.argv[1])
    dir = str(sys.argv[2])
    extension = str(sys.argv[3])
    file = file_name + extension
    open(file, 'a').close()
    os.system('start notepad++ ' + file)


if __name__ == "__main__":
    create_file()
