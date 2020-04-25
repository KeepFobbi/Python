b = open('output2.txt', 'w')
with open(r"input2.txt") as f:
    nums = [int(v) for v in f.read().split()]
    if nums[0] * nums[1] == nums[2]:
        b.write("YES")
    else:
        b.write("NO")
b.close()
