from time import time
start = time()


def smallest_multiple(d):
    n = d
    t = d
    while True:
        while n % d == 0:
            d -= 1
            if d == 1:
                return n
        d = t
        n += 1

print(smallest_multiple(20))


end = time()
total_time = end - start

print ("done in : {} seconds".format(total_time))