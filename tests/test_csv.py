from libreria.csv_file import Csv
from libreria.strumenti import print_wrapper
import pytest


class TestCsvFileToList:
    @pytest.fixture(autouse=True)
    def create_csv_file(self):
        self.file_csv_test_path = 'dati_test/anagrafica_test_csv_file.csv'
        header = 'Codice fiscale;Matricola;NomeCompleto'

        # create the csv file
        print_wrapper(header, 'w', self.file_csv_test_path, 'utf-8')

        # add records
        self.records = [('XXXYYY75A62L500P', '999', 'Cognome Nome 999'),
                    ('YYYXXX70B21L500B','888','Cognome Nome 888')]
        for record in self.records:
            print_wrapper(';'.join(record), 'a', self.file_csv_test_path, 'utf-8')
    
    def test_filetolist_is_recordslist(self):
        csv_obj = Csv("dati_test/", "anagrafica_test_csv_file.csv", "log_test.txt", ";")

        assert csv_obj.file_to_list() == self.records
