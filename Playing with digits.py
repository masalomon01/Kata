# 6kyu

def dig_pow(n, p):
    num_l, cnt, tot = [int(x) for x in str(n)], 0, []
    while cnt < len(num_l):
        mult = num_l[cnt]**(p+cnt)
        tot.append(mult)
        cnt+=1
    k, ref = 1, n
    if sum(tot) < n:
        return -1
    elif sum(tot) == n:
        return k
    else:
        while ref < sum(tot):
            ref = n*k
            k+=1
        if ref == sum(tot):
            return k-1
        else:
            return -1



print dig_pow(89, 1) # , 1)
print dig_pow(92, 1) # , -1)
print dig_pow(46288, 3) # , 51)