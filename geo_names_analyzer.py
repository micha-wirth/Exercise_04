#! /usr/bin/env python

from collections import Counter
import timeit
import time


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

    my_dict = list(dict())

    my_list = list()

    dict_cnt = Counter(dict())
    dict_map = dict()

    if zipfile.is_zipfile(filename=zip_name):
        with zipfile.ZipFile(file=zip_name, mode='r') as my_zip:
            txt_list = my_zip.namelist()
            txt_name = txt_list[0] if len(txt_list) != 0 else None
            with my_zip.open(name=txt_name, mode='r') as my_text:
                for line in my_text:
                    my_line = (bytes(line).decode(encoding='utf-8').split())
                    if my_line[6] == 'P' and len(my_line) > 14 and my_line[14].isnumeric():
                        if int(my_line[14]) > 0:
                            # my_dict.append({'name': my_line[1], 'inhabitants': int(my_line[14]), 'code': my_line[8]})
                            compute_most_frequent_city_names_by_sorting(my_list, my_line[1])
                            compute_most_frequent_city_names_by_map_cnt(dict_cnt, my_line[1])
                            compute_most_frequent_city_names_by_map_dct(dict_map, my_line[1])
    my_list.sort(reverse=True)
    print(my_list[0])

    print(dict_cnt.most_common(3))
    print(Counter(dict_map).most_common(3))
    compare_runtime(dict_cnt)
    compare_runtime(Counter(dict_map))


def compute_most_frequent_city_names_by_sorting(my_list, name):
    """
    Calculates the most frequent world-wide
    locality names via sorting.
    :return:
    """
    for count, item in enumerate(my_list):
        if item[0] == name:
            my_list[count][1] = item[1] + 1
        else:
            my_list.append([name, 1])
    else:
        my_list.append([name, 1])
    return my_list


def compute_most_frequent_city_names_by_map_cnt(d, name):
    """
    Calculates the most most frequent world-wide
    locality names via an associative array.
    """
    d.update({name: 1})
    return d


def compute_most_frequent_city_names_by_map_dct(d, name):
    """
    Calculates the most most frequent world-wide
    locality names via an associative array.
    """
    d.setdefault(name, 0)
    d[name] += 1


def compare_runtime(d):
    """    Calculates the 3 most-frequent locality names
    world-wide.
    :return:
    """
    start_time = time.process_time()
    d.most_common(3)
    # print(timeit.timeit('compute_most_frequent_city_names_by_map_cnt', globals=globals()))
    # print(timeit.timeit('compute_most_frequent_city_names_by_map_dct', globals=globals()))
    elapsed_time = time.process_time() - start_time
    print(elapsed_time)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    read_info_from_file()