def decimal_to_bin(num):
    # implement decimal to bin without using built-ins
    out = []
    while num > 0:
        out.append(str(num % 2))
        num //= 2
    return "".join(out[::-1])

def bin_to_decimal(num):
    # implement binary (str) to decimal without using built-ins
    out = 0
    base = 1
    for i in range(len(num)-1, -1, -1):
        out += base * int(num[i])
        base <<= 1
    return out

if __name__ == '__main__':
    print(decimal_to_bin(2))
    print(decimal_to_bin(5))
    print(decimal_to_bin(13))
    print(decimal_to_bin(23))

    print(bin_to_decimal('1010001'))
    print(bin_to_decimal('0101011'))
    print(bin_to_decimal('00101'))
