from time import time
start = time()


def is_palindrome(string):
    result = True
    str_len = len(string)
    for x in range(0, int(str_len/2)):
        if string[x] != string[str_len-x-1]:
            result = False
            break
    return result

largest = 1

for i in xrange(100, 1000):
    for j in xrange(100, 1000):
        n = i*j
        if is_palindrome(str(n)) and n > largest:
            largest = n


print(largest)

end = time()
total_time = end - start

print ("done in : {} ms".format(total_time))