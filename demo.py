def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main part of the code
# Calculate factorial and check for prime status of numbers 1-10
for i in range(1, 11):
    print(f"Number: {i}")
    print(f"Factorial: {factorial(i)}")
    print(f"Is Prime: {is_prime(i)}")
    print("-" * 20)
