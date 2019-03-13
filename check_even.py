# Test check number is even or odd
def check_even(number):
    if type(number) is int:
        if number == 0:
            return 'This is null!'
        if number % 2 is 0:
            return True
        return False
    return "Number isn't integer!"
