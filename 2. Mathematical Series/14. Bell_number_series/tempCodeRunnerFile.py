for i in range(1, n+1):
    total = 0
    for k in range(i):
        total += math.comb(i-1, k) * bell[k]
    bell[i] = total
