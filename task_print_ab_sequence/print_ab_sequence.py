"""Print 1 2a 3b 4a 5 6ab 7 8a 9b 10a 11 12ab ... 100a sequence,
when each second number has letter 'a'
and each third number has letter 'b'."""


def print_ab_sequence():
    """Function for print ab sequence."""
    print(generate_ab_sequence())


def generate_ab_sequence(number_min=1, number_max=100):
    """Function for generate ab sequence.

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
    return sequence


if __name__ == '__main__':
    print_ab_sequence()
