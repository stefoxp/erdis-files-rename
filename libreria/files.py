import os
from libreria import strumenti


def get_files_list(files_path):
    return os.listdir(files_path)


def clear_directory(dir_to_clear_path: str):
    for file in get_files_list(dir_to_clear_path):
        os.remove(dir_to_clear_path + file)


class Files:
    """
    Gestisce i files della directory indicata
    """

    def __init__(self, input_dir_path_p: str, output_dir_path_p: str):
        self.input_dir_path = input_dir_path_p
        self.output_dir_path = output_dir_path_p
        self.log_file_path = self.input_dir_path + 'log.txt'

        # crea file di log
        strumenti.print_wrapper('', 'w', self.log_file_path)

    def rename(self, name_to_find, name_to_set, msg):
        # if self.exists(name_to_find):
        if os.path.exists(self.input_dir_path + name_to_find):
            # TODO: gestione errori  OSError in caso di files di destinazione già esistenti
            os.rename(self.input_dir_path + name_to_find, self.output_dir_path + name_to_set)
        else:
            # log delle anagrafiche prive di file
            strumenti.print_wrapper(msg, 'a', self.log_file_path)
