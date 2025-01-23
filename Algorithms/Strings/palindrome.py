def reverse_string(string) -> str:
    result = ""
    for char in string:
        result = char + result
    return result


def is_palindrome(str1, str2):
    return str1 == str2[::-1]
    # return str1 == "".join(list(reversed(str2)))


if __name__ == '__main__':
    print(reverse_string("Python"))
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    if is_palindrome(str1, str2):
        print("The strings are palindrome!")
    else:
        print("Strings are not palindrome!")
