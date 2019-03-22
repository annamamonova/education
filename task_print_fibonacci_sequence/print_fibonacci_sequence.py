"""Print Fibonacci sequence."""


# def generate_fibonacci_sequence(max_count=21):
#     """Function for generate Fibonacci sequence.
#
#     param:
#     max_count: max number in sequence
#     """
#     first_number, second_number = 0, 1
#     sequence = ''
#     while second_number < max_count:
#         result = first_number + second_number
#         sequence += str(result) + ' '
#         first_number = second_number
#         second_number = result
#     return sequence


class Fibonacci:
    """Class for Fibonacci sequence"""

    def __init__(self, max_count=21):
        self.first_number = 0
        self.second_number = 1
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_count:
            self.first_number, self.second_number = self.second_number, \
                                                    self.first_number + self.second_number
            self.count += 1
            return self.second_number
        raise StopIteration


def generate_fibonacci_sequence(max_count):
    """Function for generate Fibonacci sequence.

    param:
    max_count: max number in sequence
    """
    return [element for element in Fibonacci(max_count)]


def print_fibonacci_sequence(max_count=21):
    """Function for print fibonacci sequence.

    param:
    number: max number in sequence
    """
    print(generate_fibonacci_sequence(max_count))


if __name__ == '__main__':
    print_fibonacci_sequence()
