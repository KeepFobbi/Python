a = int(input("a: "))
b = int(input("b: "))

def nsd(a, b):
    while b > 0:
        a %= b
        a, b = b, a
    return a

print(a * b / nsd(a, b))