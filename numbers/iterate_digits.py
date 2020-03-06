def print_digits(integer):
    while integer > 0:
        print(integer % 10)
        integer //= 10

if __name__ == '__main__':
    integer = 123456789
    print_digits(integer)
