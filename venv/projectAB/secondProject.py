#improvement of first
#start of program
while 1:
    #menu
    option = input("Choose what you want to do:\nA. Enter two numbers\nB. End program\n: ")
    option = option.lower()
    if option == "a":
        while 1:
            # ask user to insert  two numbers and store them in variables and check if any of numbers are 0
            a = float(input("Enter number a: "))
            b = float(input("Enter number b: "))
            if a==0 or b==0:
                print("Further equitation won't work with 0")
            else:
                break

        # print them as sum
        print(f"Sum of a and b: {round(a + b, 4)}")

        # print them as difference
        print(f"Difference of a and b: {round(a - b, 4)}")
        print(f"Difference of b and a: {round(b - a, 4)}")

        # print them as multiplication
        print(f"Multiplication of a and b: {round(a * b, 4)}")

        # print them as quotient
        print(f"Quotient of a and b: {round(a / b, 4)}")
        print(f"Quotient of b and a: {round(b / a, 4)}")

    elif option == "b":
        break

    else:
        print("Not valid option")
