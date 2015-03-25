def digits_sum(n):
    st = str(n)
    s = 0
    for i in range(len(st)):
        s += int(s[i])
    return s


print(digits_sum(2 ** 1000))