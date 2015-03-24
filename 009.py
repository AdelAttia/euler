from time import time


def pythagorean_triplet(limit):
    for x in range(1, limit):
        for y in range(x+1, limit):
            for z in range(y+1, limit):
                s = x + y + z
                if x * x + y * y == z * z and s == 1000:
                    return x * y * z


start = time()
print(pythagorean_triplet(450))
end = time()
execution_time = end - start
print("execution time", execution_time)