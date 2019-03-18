"""Print Fibonacci sequence."""


def generate_fibonacci_sequence(number=21):
    """Function for generate Fibonacci sequence.

    param:
    number: max number in sequence
    """
    x, y = 0, 1
    sequence = ''
    while y < number:
        res = x + y
        sequence += str(res) + ' '
        x = y
        y = res
    return sequence


def print_fibonacci_sequence(number=21):
    """Function for print fibonacci sequence.

    param:
    number: max number in sequence
    """
    print(generate_fibonacci_sequence(number))


if __name__ == '__main__':
    print_fibonacci_sequence()
