a = input("Enter string of chars: ")

i = a.__len__()-1

b = ""

while i >= 0:
    b += a[i]
    i-=1

print(b)