a = int(input("Число а:"))
b = int(input("Число б:"))
c = int(input("Число с:"))

if a < b: a, b = b, a
if b < c: b, c = c, b
if a < b: a, b = b, a

print(a, b, c)