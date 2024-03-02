m = eval(input("Enter the first number: "))
n = eval(input("Enter the second number: "))

print("Before swapping:")
print("First number:", m)
print("Second number:", n)

m = m + n
n= m - n
m = m - n

print("\nAfter swapping:")
print("First number:", m)
print("Second number:", n)
