def factorial_n(n):
    if n <= 1:
        return 1
    return n * factorial_n(n - 1)


def generate_factorial(n):
    return [factorial_n(i) for i in range(1, n + 1)]


if __name__ == '__main__':
    print(f"Factorial: {factorial_n(4)}")
    print(f"Factorial: {factorial_n(5)}")
    print(f"Factorial: {factorial_n(6)}")
    print(f"Generating Factorial: {generate_factorial(5)}")
    print(f"Generating Factorial: {generate_factorial(8)}")
