def n_divisible(number, base):
    return number % base == 0


def divisible_2(number):
    return number % 2 == 0


def divisible_3(number):
    return number % 3 == 0


if __name__ == '__main__':
    print(n_divisible(25, 5))
    print(n_divisible(26, 3))
    print(n_divisible(56, 4))
    print(divisible_2(6))
    print(divisible_3(9))
    print(divisible_3(11))
