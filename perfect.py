def is_perfect_number(n):
 
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    
    if sum_of_divisors == n:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_perfect_number(number):
    print(number, "is a perfect number")
else:
    print(number, "is not a perfect number")
