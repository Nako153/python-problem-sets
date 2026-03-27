def main():
    grocery = products()
    print_products(grocery)

def products():
    grocery = {}

    while True:
        try:
            item = input().upper()
            grocery[item] = grocery.get(item, 0) + 1
        except EOFError:
            break

    return grocery

def print_products(grocery):
    for item in sorted(grocery):
        print(grocery[item], item)

main()