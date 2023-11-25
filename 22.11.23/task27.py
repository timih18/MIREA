def de(n, m):
    if n % m == 0:
        return True
    return False


for a in range(1, 100):
    flag = True
    for x in range(1, 100):
        f = (de(x, 2) <= (not de(x, 3))) or (x + a >= 100)
        if not f:
            flag = False
            break
    if flag:
        print(a)
        break
