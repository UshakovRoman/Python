
xyz = int(input("Введите три разных цифры:"))
x = xyz // 100
y = (xyz % 100) // 10
z = xyz % 10
if x==y or x==z or y==z:
    print("Введены одинаковые цифры")
elif len(str(xyz)) <3:
    print("Введено меньше трёх цифр")
elif len(str(xyz)) >3:
    print("Введено больше трёх цифр")
else:
    print(x, y, z)
    print(x, z, y)
    print(y, x, z)
    print(y, z, x)
    print(z, x, y)
    print(z, y, x)

