#first nums

import math

a = int(input("Enter number: "))

stop = math.ceil(math.sqrt(a))

nums = []

for i in range(2, a+1):
    nums.append(i)

for l in range(2, stop+1):
    for i in range(2, a):
        p = l
        p *= i
        if nums.__contains__(p):
            nums.remove(p)

if nums.__contains__(a):
    print("First num")
else:
    print("Not first num")

print(nums)