a = open('input2.txt', 'r')
b = open('output2.txt', 'w')
n = 3
for v in range(n):
    j = int(a.readline())
    c = str(j * 100 + 90 + (9 - j))
    b.write(c + '\n')
