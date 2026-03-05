def main():
    time = input("What time is it? ")
    k = convert(time)

    if 7 <= k <= 11:
        print("breakfast time")
    elif 12 <= k <= 17:
        print("lunch time")
    elif 18 <= k <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60


if __name__ == "__main__":
    main()