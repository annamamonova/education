"""Print Fibonacci sequence."""


def generate_fibonacci_sequence(number=21):
    """Function for generate Fibonacci sequence.

    param:
    number: max number in sequence
    """
    first_number, second_number = 0, 1
    sequence = ''
    while second_number < number:
        result = first_number + second_number
        sequence += str(result) + ' '
        first_number = second_number
        second_number = result
    return sequence


def print_fibonacci_sequence(number=21):
    """Function for print fibonacci sequence.

    param:
    number: max number in sequence
    """
    print(generate_fibonacci_sequence(number))


if __name__ == '__main__':
    print_fibonacci_sequence()
