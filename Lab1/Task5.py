import math

a = int(input("Сторона а: "))
b = int(input("Сторона б: "))
c = int(input("Сторона с: "))

p = (a + b + c) / 2
rez = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(rez)