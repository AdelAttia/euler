from time import time
start = time()

def diff(n):
	s = ss= 0
	for i in xrange(n+1):
		s += i * i
		ss += i
	return ss * ss - s

print(diff(100))

end = time()
total_time = end - start

print ("done in : {} seconds".format(total_time))