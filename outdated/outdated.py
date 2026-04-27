months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def main():
    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            
            else:
                month_name, rest = date.split(" ", 1)
                day, year = rest.split(",")
                day = int(day.strip())
                year = int(year.strip())

                if month_name not in months:
                    continue

                month = months.index(month_name) + 1

            
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break

        except ValueError:
            pass


if __name__ == "__main__":
    main()