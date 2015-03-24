from time import time


def factorial(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f


def digits_sum(n):
    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum


start = time()

print(digits_sum(factorial(100000)))

finish = time()
execution_time = finish - start

print(execution_time)
