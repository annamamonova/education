"""Print 1 2a 3b 4a 5 6ab 7 8a 9b 10a 11 12ab ... 100a sequence, when each second number has letter 'a'
and each third number has letter 'b'."""


def print_ab_sequence(number_min, number_max):
    """Function for print ab sequence.

    :param
    number_min: number for start sequence.
    number_max: number for finish sequence.
    """
    sequence = ''
    for number in range(number_min, number_max + 1):
        letters = ""
        if number % 2 == 0:
            letters = "a"
        if number % 3 == 0:
            letters += "b"
        sequence += str(number) + letters + ' '
    return print(sequence)


if __name__ == '__main__':
    print_ab_sequence()
