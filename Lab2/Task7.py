rez = []
while 1:
    num = int(input())
    if num < 10:
        pass
    elif num > 100:
        break
    else: 
        rez.append(num)

for x in rez:
    print(x)