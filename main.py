print("BMI Calculator")

name = input("Enter your name: ")

print()
print("Choose your height unit")
print("1. Meter")
print("2. Centimeter")
print("3. Feet and inches")

choice = input("Enter your choice: ")

if choice == "1":
    height = float(input("Enter height in meters: "))

elif choice == "2":
    height_cm = float(input("Enter height in cm: "))
    height = height_cm / 100

elif choice == "3":
    feet = float(input("Enter height in feet: "))
    inches = float(input("Enter extra inches: "))

    total_inches = feet * 12
    total_inches = total_inches + inches
    height = total_inches * 0.0254

else:
    print("Invalid choice")
    exit()

if height <= 0:
    print("Please enter a valid height")
    exit()

weight = float(input("Enter your weight in kg: "))

if weight <= 0:
    print("Please enter a valid weight")
    exit()

bmi = weight / (height * height)

print()
print("Name:", name)
print("Height:", round(height, 2), "meters")
print("Weight:", weight, "kg")
print("BMI:", round(bmi, 2))

print()

if bmi < 18.5:
    print("You are in the underweight range.")

elif bmi < 25:
    print("You are in the healthy range.")

elif bmi < 30:
    print("You are in the overweight range.")

else:
    print("You are in the obesity range.")

print()
print("BMI calculation is completed.")

print()
print("BMI Formula:")
print("BMI = weight / (height * height)")

print()
print("BMI ranges:")
print("Below 18.5 - Underweight")
print("18.5 to 24.9 - Healthy range")
print("25 to 29.9 - Overweight")
print("30 and above - Obesity range")

again = input("\nDo you want to calculate again? yes/no: ")

while again.lower() == "yes":

    print()
    print("Choose your height unit")
    print("1. Meter")
    print("2. Centimeter")
    print("3. Feet and inches")

    choice = input("Enter your choice: ")

    if choice == "1":
        height = float(input("Enter height in meters: "))

    elif choice == "2":
        height_cm = float(input("Enter height in cm: "))
        height = height_cm / 100

    elif choice == "3":
        feet = float(input("Enter height in feet: "))
        inches = float(input("Enter extra inches: "))

        total_inches = feet * 12
        total_inches = total_inches + inches
        height = total_inches * 0.0254

    else:
        print("Invalid choice")
        again = input("Do you want to try again? yes/no: ")
        continue

    if height <= 0:
        print("Please enter a valid height")
        again = input("Do you want to try again? yes/no: ")
        continue

    weight = float(input("Enter your weight in kg: "))

    if weight <= 0:
        print("Please enter a valid weight")
        again = input("Do you want to try again? yes/no: ")
        continue

    bmi = weight / (height * height)

    print()
    print("Name:", name)
    print("Height:", round(height, 2), "meters")
    print("Weight:", weight, "kg")
    print("BMI:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")

    elif bmi < 25:
        print("Category: Healthy range")

    elif bmi < 30:
        print("Category: Overweight")

    else:
        print("Category: Obesity range")

    again = input("\nDo you want to calculate again? yes/no: ")

print()
print("Thank you for using my BMI Calculator!")