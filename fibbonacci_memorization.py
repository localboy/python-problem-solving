# Using recursion in fibonacci function

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


# Memorization

# Implicit implementation
fibonnaci_cach = {}

def fibonacci(n):
    if n in fibonnaci_cach:
        return fibonnaci_cach[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-2) + fibonacci(n-1)
    fibonnaci_cach[n] = value

    return value


# Using builtin cache
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 1001):
    print(fibonacci(i))