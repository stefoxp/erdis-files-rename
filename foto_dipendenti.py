from libreria import csv_file, files

INPUT_PATH: str = 'dati/'
OUTPUT_PATH: str = 'dati/output_files/'
EXTENSIONS: list = ['.jpg']
FILE_NAME_LEN: int = 10


def main():
    csv_obj = csv_file.Csv(INPUT_PATH, "anagrafica.csv", "log.txt", ";")
    anagrafica_list = csv_obj.file_to_list()

    # debug
    print(anagrafica_list)

    # riformatta il numero badge
    anagrafica_list = formatta_file_name(anagrafica_list)

    # debug
    print('anagrafica_list:', anagrafica_list)

    files_obj = files.Files(INPUT_PATH + 'foto/', OUTPUT_PATH)
    # files_obj.rename(anagrafica_list, EXTENSIONS)
    for anagrafica in anagrafica_list:
        codice_fiscale = anagrafica[0]
        matricola = anagrafica[1]
        nome_completo = anagrafica[2]

        for ext in EXTENSIONS:
            message = nome_completo + ' non ha un file ' + matricola + ext + ' associato'
            files_obj.rename(matricola + ext, codice_fiscale + ext, message)

    files_name_calculate = files.get_files_list(OUTPUT_PATH)

    # debug
    print(files_name_calculate)


def formatta_file_name(anagrafica_list):
    anagrafica_badge_da_dieci_list = []
    for anagrafica in anagrafica_list:
        zero_str: str = ''
        for zero in range(FILE_NAME_LEN - len(anagrafica[1])):
            zero_str += '0'

        badge = zero_str + anagrafica[1]
        anagrafica_tup = (anagrafica[0], badge, anagrafica[2])

        anagrafica_badge_da_dieci_list.append(anagrafica_tup)
    return anagrafica_badge_da_dieci_list


if __name__ == '__main__':
    main()
