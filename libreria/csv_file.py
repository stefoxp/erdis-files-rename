import csv


class Csv:
    def __init__(self, path: str, file_input_name: str, file_log_name: str, field_delimiter: str = ";"):
        self.file_input_path = path + file_input_name
        self.file_log_path = path + file_log_name
        self.field_delimiter = field_delimiter

    def file_to_list(self) -> list:
        """
        Trasforma il contenuto del file in una result_list di tuple
        """
        result_list = []

        with open(self.file_input_path, encoding="utf8") as file_csv:
            reader = csv.reader(file_csv, delimiter=self.field_delimiter)

            for row in reader:
                result_list.append(tuple(row))

        # rimuovo intestazione
        return result_list[1:]
