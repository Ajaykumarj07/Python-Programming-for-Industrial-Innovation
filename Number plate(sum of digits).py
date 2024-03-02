def sum_of_digits(number):
    total_sum = 0
    while number > 0:
        total_sum += number % 10
        number //= 10
    return total_sum

number_plate = input("Enter the number plate: ")
number_plate_digits = ''

for char in number_plate:

    if char.isdigit():
 
        number_plate_digits += char

number_plate_int = int(number_plate_digits)

sum_of_plate = sum_of_digits(number_plate_int)

print("Sum of digits in the number plate is:", sum_of_plate)
