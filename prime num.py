import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

start =1
end = 100

print("Prime numbers in the range", start, "to", end, "are:")

prime_count = 0

for number in range(start, end + 1):
    if is_prime(number):
        print(number)
        prime_count += 1

print("Total prime numbers in the range:", prime_count)
