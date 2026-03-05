def convert(text):
    text = text.replace(":)", "Hello")
    text = text.replace(":(", "Goodbye")
    return text


def main():
    text = input("(Hello / Goodbye): ")
    print(convert(text))


main()