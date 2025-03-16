#ask user to insert  two numbers and store them in variables
a = int(input("Enter integer number: "))
b = float(input("Enter floating point number: "))

#print them as sum
print(f"Sum of a and b: {round(a+b, 4)}")

#print them as difference
print(f"Difference of a and b: {round(a-b, 4)}")
print(f"Difference of b and a: {round(b-a, 4)}")

#print them as multiplication
print(f"Multiplication of a and b: {round(a*b, 4)}")

#print them as quotient
print(f"Quotient of a and b: {round(a/b, 4)}")
print(f"Quotient of b and a: {round(b/a, 4)}")
