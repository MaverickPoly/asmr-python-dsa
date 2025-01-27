# Use built-in modules and libraries for hashing securely.

def custom_hash(seed, input_value):
    if not isinstance(input_value, (str, int, bytes)):
        raise TypeError("Input must be either str, int or bytes!")

    if isinstance(input_value, str):
        input_bytes = input_value.encode("utf-8")
    elif isinstance(input_value, int):
        input_bytes = str(input_value).encode("utf-8")
    else:
        input_bytes = input_value

    hash_value = seed
    for byte in input_bytes:
        hash_value = (hash_value * 37 + byte) % (2 ** 32)
    return hash_value


def hash_func(value):
    value = str(value)
    hash_value = 0
    for byte in value:
        hash_value = (hash_value * 31 + ord(byte)) % (2 ** 32)
    return hash_value


if __name__ == '__main__':
    print("Built In Hash Function:")
    print(hash("Hello"))
    print(hash("Helloo"))
    print(hash(1))

    print("\nCustom Hash Function:")
    print(hash_func("Hello"))
    print(hash_func("Helloo"))
    print(hash_func(1))

    print("\nCustom Hashing 2:")
    print(custom_hash(0, "Hello"))
    print(custom_hash(0, "Helloo"))
    print(custom_hash(0, "World"))
    print(custom_hash(0, 1))
    # print(custom_hash(0, [1, 2, 3]))
