def read_info_from_file():
    """
    Read information from the GeoNames.org
    tab-separated table file allCountries.txt.

    :return:
    """
    import glob
    import zipfile

    # with zipfile.ZipFile(file='allCountries_04.zip', mode='r') as my_zip:
    #     with my_zip.open(name='allCountries.txt', mode='r') as my_text:
    #         print(my_text.readline().decode(encoding='utf-8').split())

    zip_list = glob.glob(pathname='*.zip')
    print(zip_list)

    zip_name = zip_list[0] if len(zip_list) != 0 else None

    # zip_name = 'allCountries_04.zip'
    if zipfile.is_zipfile(filename=zip_name):
        with zipfile.ZipFile(file=zip_name, mode='r') as my_zip:
            txt_list = my_zip.namelist()
            txt_name = txt_list[0]
            with my_zip.open(name=txt_name, mode='r') as my_text:
                for line in my_text:
                    my_line = (bytes(line).decode(encoding='utf-8').split())
                    print(type(my_line))
                    break




            # locality = line[6] is 'P'
            # name = line[1]
            # inhabitants = line[14]
            # country_code = line[8]
            #     print(line)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    read_info_from_file()