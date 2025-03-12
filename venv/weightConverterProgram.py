#variables
orginWeight = 0
newWeight = 0
unit = ""

#user input
orginWeight = float(input("Enter your weight: "))
unit = input("Enter unit to which you want convert your weight(Kgs/Lbs): ")
unit = unit.lower()

#check if unit ist correct
while 1:
    if unit == "kgs" or unit == "lbs":
        break

    unit = input("Incorrect unit. Enter kgs or lbs: ")
    unit = unit.lower()


#converting into kilograms
if unit == "kgs":
    newWeight = orginWeight / 2.205

#converting into pounds
else:
    newWeight = orginWeight * 2.205


#display new weight
print(f"Your new weight is {round(newWeight, 2)} {unit}")
