# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

side1 = int(input("Введите кол-во долек по горизонтали: "))
side2 = int(input("Введите кол-во долек по вертикали: "))
shares = int(input("Введите кол-во долек, которые нужно отломить: "))
if side1*side2>=shares and (shares % side1 == 0 or shares % side2 == 0):
    print("Да, можно.")
else:
    print("Нет, нельзя.")