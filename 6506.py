#cesar's code

step = int(input("Enter step of move: "))
message = input("Enter message: ")
secret = ""
for i in message:
    a = ord(i)
    a += step
    secret += chr(a)


print(secret)