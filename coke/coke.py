def main():
    amount_due = 50

    while amount_due > 0:
        print("Amount Due:", amount_due)
        money = int(input("Insert Money:"))

        if money in [25, 40, 45, 10, 0]:
            amount_due -= money
    print("Change Owe:", abs(amount_due))

main()