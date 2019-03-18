# print 1 2a 3b 4a 5 6ab 7 8a 9b 10a 11 12ab ... 100a sequence
def print_ab_sequence(number_min, number_max):
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
    print(print_ab_sequence())
