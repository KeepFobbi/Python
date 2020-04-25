b = open('output1.txt', 'w')
with open(r"input1.txt") as f:
    nums = [int(v) for v in f.read().split()]
b.write(str(max(nums)))
b.close()