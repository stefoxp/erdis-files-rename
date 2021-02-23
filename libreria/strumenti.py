def print_wrapper(obj, mode: str = 'a', destination: str = "", encode: str = "utf-8") -> None:
    """
    Writes the records on video or in the specified destination

    :param obj: string or list or printable object
    :param mode: 'w', 'a', or others valid values
    :param destination: path of the file. If omitted print on video
    :param encode:
    """
    if len(destination) > 0:
        # make or empty the file
        file_out = open(destination, mode, encoding=encode)
        print(obj, file=file_out)
        file_out.close()
    else:
        print(obj)

def normalize_list_of_strings(original_list: list) -> list:
    result = []

    for o in original_list:
        o_normalized = o.replace('"', '')
        o_normalized = o_normalized.replace("’", "'")
        o_normalized = o_normalized.replace("à", "a")

        result.append(o_normalized)

    return result