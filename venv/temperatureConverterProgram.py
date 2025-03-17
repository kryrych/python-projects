while 1:
    option = input("Temperature Converter Program!\nC. Convert Fahrenheit degree to Celsius degree\nF. Convert Celsius degree to Fahrenheit degree\nE. Exit\n:")
    option = option.lower()
    if option == "f":
        temp = float(input("Enter temperature in fahrenheit degree: "))
        print(f"{round((temp-32)*5/9, 2)}°C")
    elif option == "c":
        temp = float(input("Enter temperature in celsius degree: "))
        print(f"{round((temp * 9) / 5 + 32, 2)}°F")
    elif option == "e":
        break
    else:
        print("Option not valid\n")