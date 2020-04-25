b = open('output3.txt', 'w')
with open(r"input3.txt") as f:
    a = int(f.read(1))
    num = [int(v) for v in f.read().split()]
Sum = 0
Max = 0
Min = 1
for i in range(a):
    if num[i] > 0:
        Sum = Sum + num[i]
for i in range(a):
    if num[i] > num[Max]:
        Max = i
    if num[i] < num[Min]:
        Min = i

if Max < Min:
    Max, Min = Min, Max

Mult = 1

for n in range(Min + 1, Max):
    Mult *= num[n]

if Min + 1 != Max:
    b.write(str(Sum) + " " + str(Mult))
else:
    b.write(str(Sum) + " " + "0")
b.close()
