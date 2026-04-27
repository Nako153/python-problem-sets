def main():
    user = input("Input: ")
    print(remove_vowels(user))


def remove_vowels(word):
    result = ""
    for c in word:
        if c.lower() not in "aeiou":
            result += c
    return result


if __name__ == "__main__":
    main()