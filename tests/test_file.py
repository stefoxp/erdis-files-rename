from libreria import strumenti, files


class TestFileCreation:
    def test_files_in_directory(self):
        file_path = 'dati_test/directory/'

        files_in_dir_list = ['gatto.txt', 'cane.txt', 'topo.txt']
        files_in_dir_calcolati = files.get_files_list(file_path)

        # ordina le liste per poterle confrontare (N.B. sort() return always None)
        files_in_dir_calcolati.sort()
        files_in_dir_list.sort()

        assert files_in_dir_calcolati == files_in_dir_list

    def test_clear_directory(self):
        dir_to_clear_path = 'dati_test/output_files/'

        files.clear_directory(dir_to_clear_path)

        assert files.get_files_list(dir_to_clear_path) == []

    def test_file_rename(self):
        input_path = 'dati_test/input_files/'
        output_path = 'dati_test/output_files/'
        anagrafica_list = [('XXXYYY75A62L500P', '999', 'Cognome Nome 999'),
                           ('YYYXXX70B21L500B', '888', 'Cognome Nome 888'),
                           ('AAABBB60C46L500C', '777', 'Cognome Nome 777')]
        extensions = ['.jpg', '.txt']
        files_name_result = ['XXXYYY75A62L500P.txt',
                             'YYYXXX70B21L500B.jpg']
        files_in_dir_list = ['999.txt', '888.jpg']

        # populate input directory
        for file_name in files_in_dir_list:
            strumenti.print_wrapper('', 'w', input_path + file_name)

        # clear output directory
        files.clear_directory(output_path)

        files_obj = files.Files(input_path, output_path)

        for anagrafica in anagrafica_list:
            codice_fiscale = anagrafica[0]
            matricola = anagrafica[1]
            nome_completo = anagrafica[2]

            for ext in extensions:
                message = nome_completo + ' non ha un file ' + matricola + ext + ' associato'
                files_obj.rename(matricola + ext, codice_fiscale + ext, message)

        files_name_calculate = files.get_files_list(output_path)

        # ordina le liste per poterle confrontare (N.B. sort() return always None)
        files_name_result.sort()
        files_name_calculate.sort()

        assert files_name_calculate == files_name_result
