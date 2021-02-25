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
