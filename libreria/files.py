import os
from libreria import strumenti


def get_files_list(files_path):
    return os.listdir(files_path)


class Files:
    """
    Gestisce i files della directory indicata
    """

    def __init__(self, input_dir_path_p: str):
        self.input_dir_path = input_dir_path_p

    def exist(self, name: str):
        return os.path.exists(self.input_dir_path + name)

    def rename(self, anagrafica_list, extensions_list, output_path):
        # crea file di log
        strumenti.print_wrapper('', 'w', self.input_dir_path + 'log.txt')

        for anagrafica in anagrafica_list:
            for ext in extensions_list:
                if self.exist(anagrafica[1] + ext):
                    # TODO: gestione errori  OSError in caso di files di destinazione già esistenti
                    os.rename(self.input_dir_path + anagrafica[1] + ext, output_path + anagrafica[0] + ext)
                else:
                    # log delle anagrafiche prive di file
                    strumenti.print_wrapper(anagrafica[2] + ' non ha un file ' + ext + ' associato',
                                            'a', self.input_dir_path + 'log.txt')
