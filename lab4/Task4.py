b = open('output4.txt', 'w')
with open(r"input4.txt") as f:
    nums = [int(v) for v in f.read().split()]

for x in range(-100, 101):
    if (nums[0] * x * x * x + nums[1] * x * x + nums[2] * x + nums[3]) == 0:
        b.write(str(x) + " ")
b.close()
