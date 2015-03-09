from time import time
start = time()

number = 600851475143

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return factors

print(max(prime_factors(number)))

end = time()
total_time = end - start

print ("done in : {} ms".format(total_time))