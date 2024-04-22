words = set()

# Ввод слов
while True:
    word = input()
    if word == "STOP":
        break
    words.add(word)

# Вывод отсортированных слов без повторений
for word in sorted(words):
    print(word)
