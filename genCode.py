import random

codes = ()
codes = set(codes)

file = open("codes.txt", "r")

for i in file:
    codes.add(i.strip("\n"))

file.close()

for i in codes:
    print(i)

while True:
    code = ""
    stop = input(": ")
    if stop == 'q':
        break

    while True:
        for i in range(4):
            a = random.randrange(9)
            code = code + str(a)
        codes.add(str(code))
        if code in codes:
            print(code)
            create = open(code+".py", "x")
            create.close()
            break
file = open("codes.txt", "w")

for i in codes:
    file.write(i + "\n")
file.close()