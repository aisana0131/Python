def factorial(n):
    if n == 1:  # Base case
        return 1
    else:
        print(n-1)
        return n * factorial(n - 1)  # Recursive case
print(factorial(5))  

# Output: 120