import math


def gcd(a, b):
    # return math.gcd(a, b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == '__main__':
    a, b = 8, 12
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
