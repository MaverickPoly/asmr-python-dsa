def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


if __name__ == '__main__':
    str1 = "listen"
    str2 = "silent"
    print(f"{str1} and {str2} are anagrams: {is_anagram(str1, str2)}")
