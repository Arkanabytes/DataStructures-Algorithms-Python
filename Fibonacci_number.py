
#Memoization - idea: cache values
cache = {}

def fibonacci(n):
    # Check that input is a positive integer.
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # If we have cached the value, then return it.
    if n in cache:
        return cache[n]
    
    # Compute the Nth term 
    if n <= 2:
        value = 1 
    else: 
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it.
    cache[n] = value
    return value

# The first 21 Fibonacci numbers Fn are
for n in range(1,22):
    print(n ,":" , fibonacci(n))
