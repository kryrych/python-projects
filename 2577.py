a = int(input("N word of Fi: "))

f = [0, 1]
i = 0

if a == 0:
    print(f[0])
elif a == 1:
    print(f[1])
else:
    while i < a-1:
        fi = f[0] + f[1]
        f[0] = f[1]
        f[1] = fi
        i+=1
    print(f[1])
#1. 1 1, 2. 1 2