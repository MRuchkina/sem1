#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
#Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
s = input("Сумма чисел: ")
s = int(s)
p = input("Произведение чисел: ")
p = int(p)
for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == s and x * y == p:
            print(x, y)
            break









