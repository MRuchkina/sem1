# Описание задачи:
#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = input("Введите число N: ")
n = int(n)
m = 1
while m < n:
    if(m < n):
        if (m * 2 > n):
            break
        else:
            m = m * 2
            print(m)