import sys
import os

#todo jezeli ostatnie jest rozszerzenie lub podano tylko nazwę notatka tworzy się w domyśnyn folderze.
# todo jeżeli rozszerzenia nie ma na ost. miejscu sprawdx przedostatnie!
python = ".py"
text = ".txt"
markdown = '.md'

extensions = {
    "text": text,
    "txt": text,
    ".txt": text,
    "python": python,
    "pyn": python,
    ".py": python,
    "markdown": markdown,
    "md": markdown,
    ".md": markdown
}


def create_file():
    print("Hello CMD!")
    # print(sys.argv)
    file_name = str(sys.argv[1])
    dir = str(sys.argv[2])
    extension = str(sys.argv[3])
    try:
        file_extension = extensions[extension]
    except Exception:
        file_extension = '.txt'

    file = file_name + file_extension
    open(file, 'a').close()
    os.system('start notepad++ ' + file)


if __name__ == "__main__":
    create_file()
