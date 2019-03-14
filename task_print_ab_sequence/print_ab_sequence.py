# print 1 2a 3b 4a 5 6ab 7 8a 9b 10a 11 12ab ... 100a sequence
def print_ab_sequence():
    for number in range(1, 101):
        letters = ""
        if number % 2 == 0:
            letters = "a"
        if number % 3 == 0:
            letters += "b"
        print(number, letters, sep='', end=' ')


print_ab_sequence()
