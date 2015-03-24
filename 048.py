from time import time


def self_powers_series(n):
    s = 0
    for i in range(1, n+1):
        s += i ** i
    return s


start = time()
print(str(self_powers_series(1000))[-10:])
finish = time()
execution_time = finish - start

print(execution_time)
