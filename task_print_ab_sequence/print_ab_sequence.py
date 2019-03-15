# print 1 2a 3b 4a 5 6ab 7 8a 9b 10a 11 12ab ... 100a sequence
def print_ab_sequence():
    sequence = ''
    for number in range(1, 101):
        letters = ""
        if number % 2 == 0:
            letters = "a"
        if number % 3 == 0:
            letters += "b"
        sequence += str(number) + letters + ' '
    print(sequence)


if __name__ == '__main__':
    print_ab_sequence()
