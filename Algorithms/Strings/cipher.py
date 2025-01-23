"""For secure and more advanced encryption, use libraries like 'cryptography' or 'hashlib'"""


def cipher_encrypt(text: str, shift):
    result = []
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result.append(encrypted_char)
        else:
            result.append(char)
    return "".join(result)


def cipher_decrypt(text: str, shift):
    return cipher_encrypt(text, -shift)


if __name__ == '__main__':
    plain_text = input("Enter a text: ")
    shift = int(input("Enter a shift amount: "))

    encrypted_text = cipher_encrypt(plain_text, shift)
    print("Encrypted text: {}".format(encrypted_text))

    decrypted_text = cipher_decrypt(encrypted_text, shift)
    print("Decrypted Text: {}".format(decrypted_text))
