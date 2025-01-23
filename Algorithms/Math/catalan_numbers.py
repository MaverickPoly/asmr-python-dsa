def catalan_n(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_n(i) * catalan_n(n - i - 1)
    return res


def generate_catalan(n):
    return [catalan_n(i) for i in range(n)]


if __name__ == '__main__':
    print(f"Catalan: {catalan_n(2)}")
    print(f"Catalan: {catalan_n(5)}")
    print(f"Catalan: {catalan_n(10)}")
    print(f"Generating catalan: {generate_catalan(8)}")
    print(f"Generating catalan: {generate_catalan(15)}")
