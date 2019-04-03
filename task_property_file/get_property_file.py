"""Get property file(number lines, number words, size file.)"""
import sys
from chardet.universaldetector import UniversalDetector
from os import path


def get_num_line(context):
    """
    Function count number lines.
    :param context: text for count.
    """
    return len(context)


def get_num_word(context):
    """
    Function count number words.
    :param context: text for count.
    """
    num_word = 0
    for line in context:
        num_word += len(line.split(' '))
    return num_word


def get_encoding(path_file):
    """
    Function for get encoding file.
    :param path_file: path to file.
    """
    detector = UniversalDetector()
    with open(path_file, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result


def get_property_file(path_file):
    """
    Function for get property file(number lines, number words, size file.)
    :param path_file: path to file.
    """
    x = get_encoding(path_file)
    try:
        with open(path_file, 'r', encoding=x['encoding']) as file:
            context = file.readlines()
    except OSError:
        print("Cannot open given file!")
        sys.exit(1)
    return {'num_line': get_num_line(context),
            'num_word': get_num_word(context),
            'size_file': path.getsize(path_file)}

if __name__ == '__main__':
    get_property_file()
