import random
import string


def generate_password(size=8, punctuation=True, numbers=True):
    chars = string.ascii_letters
    if punctuation:
        chars += string.punctuation
    if numbers:
        chars += string.digits
    return "".join([random.choice(chars) for _ in range(size)])


if __name__ == '__main__':
    print(generate_password(punctuation=True, numbers=True))
    print(generate_password(punctuation=True, numbers=False))
    print(generate_password(punctuation=False, numbers=False))
    print(generate_password(16, punctuation=False, numbers=False))
