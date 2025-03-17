#event isScheduled
while 1:
    #ask user to enter temperature and if is raining outside
    option = input("1.Enter weather outside\n2.Exit\n:")
    if option == "1":
        temp = float(input("What temperature is outside: "))
        isRaining = bool(input("Is raining (0/1): "))
        if (20 < temp < 35) and isRaining:
            print("Event is still scheduled")
        elif (20 < temp < 35) and not isRaining:
            print("Event is canceled due to rain")
        elif temp < 20 and isRaining:
            print("Event is canceled due to low temperature")
        elif temp < 20 and not isRaining:
            print("Event is canceled due to low temperature and rain")
        elif temp > 35 and isRaining:
            print("Event is canceled due to too high temperature")
        elif temp > 35 and not isRaining:
            print("Event is canceled due to too high temperature and rain")
    elif option == "2":
        break
    else:
        print("Not valid option.\n")