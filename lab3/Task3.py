b = open('output3.txt', 'w')
with open(r"input3.txt") as f:
    a = int(f.read(1))
    nums = [int(v) for v in f.read().split()]
k = 0
c = 0
for i in range(a):
    if nums[i] % 2 == 1:
        k += 1
        b.write(str(nums[i]) + " ")
b.write('\n')
for i in range(a):
    if nums[i] % 2 == 0:
        c += 1
        b.write(str(nums[i]) + " ")
b.write('\n')
if c >= k:
    b.write("YES")
else:
    b.write("NO")
