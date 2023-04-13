# Найдите сумму цифр трехзначного числа

# Первое решение
number = int(input("Введите 3-значное число: "))
summa = 0
if 1000 > number > 99:
    while number > 0:
        a = number % 10
        summa += a
        number //= 10
    print(f"Сумма цифр: {summa}")
else:
    print("Это не 3-значное число!")


# Второе решение
n = input("Введите 3-значное число: ")
print(f"Сумма цифр: {int(n[0])+int(n[1])+int(n[2])}")