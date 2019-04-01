"""Get property file(number lines, number words, size file.)"""
from os import path


def get_num_line(context):
    """
    Function count number lines.
    :param context: text for count.
    """
    return sum(1 for line in context)


def get_num_word(context):
    """
    Function count number words.
    :param context: text for count.
    """
    num_word = 0
    for line in context:
        for _ in line.split(' '):
            num_word += 1
    return num_word


def get_property_file(path_file):
    """
    Function for get property file(number lines, number words, size file.)
    :param path_file: path to file.
    """
    try:
        with open(path_file) as file:
            context = file.readlines()
    except FileNotFoundError:
        print("File doesn't find.")
        raise
    except Exception:
        print("Unknown error!")
    return {'num_line': get_num_line(context),
            'num_word': get_num_word(context),
            'size_file': path.getsize(path_file)}
