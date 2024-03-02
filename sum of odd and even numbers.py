end = int(input("Enter the end number of the range: "))

sum_odd = 0
sum_even = 0

for num in range(1, end+1 ):
 
    if num % 2 == 0:
          sum_even += num
    else:
          sum_odd += num

print("Sum of odd numbers:", sum_odd)
print("Sum of even numbers:", sum_even)    