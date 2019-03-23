"""Task for check lucky number."""


def conversion(number, dec):
    """Function for conversion number in sequence numerals

    :param
    number: number for conversion
    dec: system numeral(e.g. 10, 2, 3).
    """
    conv_number = []
    while number > 0:
        conv_number.append(number % dec)
        number = number // dec
    return conv_number


def is_lucky_number(number):
    """Function for check lucky number

    :param
    number: number for check.
    """
    conv_number, sum1 = conversion(number, 10), 0
    sum1 = sum(conv_number[:(len(conv_number) // 2)])
    if sum(conv_number) - sum1 == sum1:
        return True
    return False


def print_is_lucky_number(number):
    """Function for print answer on question: is lucky number?

    param:
    number: number for check.
    """
    print(is_lucky_number(number))
