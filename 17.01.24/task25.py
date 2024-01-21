for a in range(1000):
    flag = True
    for x in range(100):
        f = ((x & 45 > 0) or (x & 89 > 0)) <= (x & a > 0)
        if not f:
            flag = False
            break
    if flag:
        print(a)
        break
