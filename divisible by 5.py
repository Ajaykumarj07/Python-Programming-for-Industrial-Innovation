end = int(input("Enter the end number of the range: "))

num = 0
for num in range(1, end+1 ):
 
    if num % 5 == 0:
        print("in the range of:",end,"the number",num," is divisible by 5")
    else:
        print("in the range of:",end,"the number",num," is not divisible by 5")