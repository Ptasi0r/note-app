import sys
import os


class Note:
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

    extension = ""
    folder_name = ""
    file_name = ""
    path = os.getcwd()

    def get_argv(self, ext_num, folder_num):
        try:
            self.extension = str(sys.argv[ext_num]).lower()
            self.extension = self.extensions[self.extension]
        except Exception:
            try:
                self.extension = str(sys.argv[ext_num -1]).lower()
                self.extension = self.extensions[self.extension]
            except Exception:
                self.extension = '.txt'

        try:
            if not self.extensions[str(sys.argv[ext_num]).lower()]:
                self.folder_name = str(sys.argv[folder_num]).lower()
        except Exception:
            self.folder_name = ""

        try:
            self.file_name = str(sys.argv[1])
        except Exception:
            print("Name your note")
            sys.exit()

    def create_file(self):
        self.file_name = self.file_name + self.extension

        # Check if dir exist
        os.chdir('notes')
        if os.path.isdir("./" + self.folder_name):
            os.chdir("./" + self.folder_name)
        else:
            os.mkdir("./" + self.folder_name)
            os.chdir("./" + self.folder_name)
        open(self.file_name, "a").close()
        os.system('start notepad++ ' + self.file_name)

    # TODO dodaj komende noteopen gdzie użytkownik nie musi podać folderu.
    # TODO jeżeli użytkownik nie poda folderu sprawdz w których folderach plik o takiej nazwie się znajduje
    # TODO i wyświetl informację w forimie:
    # TODO ZNALEZIONE NOTATKI:
    # TODO 1. nazzwa in notes/folder_name
    # TODO https://stackoverflow.com/questions/25370774/how-to-check-if-multiple-files-exist-in-different-directories?rq=1
    # from os import listdir
    # from os.path import isdir, isfile, join
    # base_path = "gamedata/areas/"
    # files = listdir(base_path)
    # only_directories = [path for path in files if isdir(join(base_path,path))]
    #
    # for directory_path in only_directories:
    #     dir_path = join(base_path, directory_path)
    #     for file_path in listdir(dir_path):
    #         full_file_path = join(base_path, dir_path, file_path)
    #         is_file = isfile(full_file_path)
    #         is_example = "example" in file_path
    #         if is_file and is_example:
    #             print "Found One!!"


if __name__ == "__main__":
    note = Note()
    note.get_argv(3, 2)
    note.create_file()