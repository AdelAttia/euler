from time import time


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    c = x = 1
    while c < n:
        x += 2
        if is_prime(x):
            c += 1
    return x


start = time()

print(nth_prime(10001))

end = time()
total_time = end - start

print("done in {} s".format(total_time))