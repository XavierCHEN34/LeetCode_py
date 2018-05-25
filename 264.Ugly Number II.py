def n_ugly(n):
    l = [1]
    t1 = 0
    t2 = 0
    t3 = 0
    if n == 1:
        return 1

    for i in range(n-1):
        ugly = min(l[t1]*2,l[t2]*3,l[t3]*5 )
        l.append(ugly)
        if ugly == l[t1]*2:
            t1 += 1
        if ugly == l[t2]*3:
            t2 += 1
        if ugly == l[t3]*5:
            t3 += 1

    return l[-1]


print(n_ugly(10))