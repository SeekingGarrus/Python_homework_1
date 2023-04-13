# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# Первое решение
ticket = int(input("Введите 6-значный номер билета: "))
if 1000000 > ticket > 99000:
    ticket1 = ticket // 1000
    ticket2 = ticket % 1000
    summa1 = 0
    summa2 = 0
    while ticket1 > 0:
        a1 = ticket1 % 10
        summa1 += a1
        ticket1 //= 10
    print(f"Сумма первых трех цифр: {summa1}")
    while ticket2 > 0:
        a2 = ticket2 % 10
        summa2 += a2
        ticket2 //= 10
    print(f"Сумма вторых трех цифр: {summa2}")

    if summa1 == summa2:
        print("Это счастливый билет!")
    else:
        print("Это не счастливый билет.")
else:
    print("Это не 6-значный номер!")

# Второе решение
n = input("Введите 6-значное число: ")
if (int(n[0])+int(n[1])+int(n[2])) == (int(n[3])+int(n[4])+int(n[5])):
    print("Это счастливый билет!")
else:
    print("Это не счастливый билет!")