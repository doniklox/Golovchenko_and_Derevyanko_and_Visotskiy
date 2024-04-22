def get_drink_of_the_day(day_number):2
    drinks = ["кофе", "чай", "компот", "какао"]
    return drinks[day_number % len(drinks)]


n = int(input("Введите количество дней: "))

schedule = [get_drink_of_the_day(day) for day in range(n)]
print(" ".join(schedule))

