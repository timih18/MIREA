def treug(n, m, k):
    if max(n, m, k) <= min(m, n, k) + m + n + k - max(m, n, k) - min(m, n, k):
        return True
    return False


mx = 0
for a in range(1, 100):
    flag = True
    for x in range(1, 100):
        f = not ((treug(x, 11, 16) == (not (max(x, 5) > 10))) and (treug(4, a, x)))
        if not f:
            flag = False
    if flag:
        mx = a
print(mx)
