a = input("Enter whole number: ")

a = tuple(a)

b = 0

for i in a:
    b += int(i)

print(b)