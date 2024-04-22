
numbers = []
total = 0
count = 0

# Ввод чисел
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)
    total += num
    count += 1

# Проверка наличия четных чисел и их обработка
if count > 0:
    average = total / count
    print("avg = {:.2f}".format(average))
    for num in numbers:
        if num % 2 == 0:
            num += average
        print(num)
else:
    print("avg = 0")