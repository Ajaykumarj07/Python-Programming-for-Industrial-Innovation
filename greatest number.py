num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))

greatest = num1

if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3

print("The greatest number among the numbers is:", greatest)
