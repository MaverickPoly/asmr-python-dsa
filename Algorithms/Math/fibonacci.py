def fibonacci_n(n):
    if n <= 1:
        return n
    return fibonacci_n(n - 1) + fibonacci_n(n - 2)


def generate_fibonacci(n):
    return [fibonacci_n(i) for i in range(n)]


if __name__ == '__main__':
    print(f"Fibonacci: {fibonacci_n(4)}")
    print(f"Fibonacci: {fibonacci_n(5)}")
    print(f"Fibonacci: {fibonacci_n(6)}")
    print(f"Generating Fibonacci: {generate_fibonacci(6)}")
    print(f"Generating Fibonacci: {generate_fibonacci(20)}")
