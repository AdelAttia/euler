from time import time
now = time()

s = 0
t1 = 1
t2 = 2
limit = 4000000

while t2 < limit:
    if t2 % 2 == 0:
        s += t2
    t = t1 + t2
    t1 = t2
    t2 = t

print (s)

done = time()
total_time = done - now

print ("done in : {} ms".format(total_time))