from time import time
start = time()

s = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        s += i

print (s)

end = time()
total_time = end - start

print ("done in : {} ms".format(total_time))