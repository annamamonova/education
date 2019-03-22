"""Task for check lucky number."""


def conversion(number):
    """Function for conversion number in sequence numerals

    :param
    number: number for conversion.
    """
    conv_number = []
    while number > 0:
        conv_number.append(number % 10)
        number = number // 10
    return conv_number


def is_lucky_number(number):
    """Function for check lucky number

    :param
    number: number for check.
    """
    conv_number, sum1 = conversion(number), 0
    for i in range(len(conv_number) // 2):
        sum1 += conv_number[i]
    if sum(conv_number) - sum1 == sum1:
        return True
    return False


def print_is_lucky_number(number):
    """Function for print answer on question: is lucky number?

    param:
    number: number for check.
    """
    print(is_lucky_number(number))
