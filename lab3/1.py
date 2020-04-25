a = open('input.txt', 'r')
b = open('output.txt', 'w')
j = int(a.read())
c = j // 10
b.write(str(c * (c + 1)*100+25))
b.close()
a.close()
