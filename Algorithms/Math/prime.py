def is_prime(number):
    if number < 2:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_2(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def generate_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


if __name__ == '__main__':
    print(is_prime(5))
    print(is_prime(6))

    print("\nPrime numbers:")
    print(generate_prime(27))
