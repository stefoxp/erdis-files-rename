from libreria import strumenti, files


class TestFileCreation:
    def test_file_txt_created_is_true(self):
        file_path = 'dati_test/'
        files_list = ['cane.txt',
                      'gatto.txt',
                      'topo.txt']

        files_obj = files.Files(file_path)

        for file_name in files_list:
            strumenti.print_wrapper('', 'w', file_path + file_name)

            assert files_obj.exist(file_name) is True

    def test_file_not_present_is_false(self):
        file_path = 'wrong_dir/'
        file_name = 'wrong_name.txt'

        files_obj = files.Files(file_path)

        assert files_obj.exist(file_name) is False

    def test_files_in_directory(self):
        file_path = 'dati_test/input_files/'
        # files_obj = files.Files(file_path)

        files_in_dir_list = ['cat.jpg', 'gatto.txt', 'mouse.jpg', 'topo.txt', '999.txt', '888.jpg']
        files_in_dir_calcolati = files.get_files_list(file_path)

        # ordina le liste per poterle confrontare (N.B. sort() return always None)
        files_in_dir_calcolati.sort()
        files_in_dir_list.sort()

        assert files_in_dir_calcolati == files_in_dir_list

    def test_file_rename(self):
        input_path = 'dati_test/input_files/'
        output_path = 'dati_test/output_files/'
        anagrafica_list = [('XXXYYY75A62L500P', '999', 'Cognome Nome 999'),
                           ('YYYXXX70B21L500B', '888', 'Cognome Nome 888'),
                           ('AAABBB60C46L500C', '777', 'Cognome Nome 777')]
        extensions_list = ['.jpg', '.txt']
        files_name_result = ['XXXYYY75A62L500P.txt',
                             'YYYXXX70B21L500B.jpg']

        files_obj = files.Files(input_path)
        files_obj.rename(anagrafica_list, extensions_list, output_path)

        files_name_calculate = files.get_files_list(output_path)

        # ordina le liste per poterle confrontare (N.B. sort() return always None)
        files_name_result.sort()
        files_name_calculate.sort()

        assert files_name_calculate == files_name_result
