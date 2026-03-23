def main():
    camel = input("camelCase:")
    print("snake_case:", convert(camel))

def convert(text):
    result = ""
    
    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result

main()
