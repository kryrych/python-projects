import math

a = int(input("Enter num of n!: "))

print(math.factorial(a))#python math lib

n = 1

for i in range(1, a + 1):#funkcja iteracyjna
    n *= i

print(n)