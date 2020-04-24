import math

print("1 - триугольник\n2 - прямоугольник\n3 - круг\n")

figure = int(input(">>> "))

if figure == 1:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    p = (a + b + c) / 2
    rez = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print(rez)
elif figure == 2:
    a = int(input("a: "))
    b = int(input("b: "))

    print(a * b)
elif figure == 3:
    r = int(input("r: "))

    print(3.14 * r * r)
else:
    print("Нет такого значения")