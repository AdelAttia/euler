from time import time
import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_sum(limit):
    s = 2
    for i in range(3, limit+1, 2):
        if is_prime(i):
            s += i
    return s


start = time()
print(prime_sum(2000000))
end = time()
execution_time = end - start
print("execution time", execution_time)