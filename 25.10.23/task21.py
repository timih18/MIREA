for a in range(100):
    flag = True
    for x in range(100):
        f = (x & 51 == 0) or ((x & 41 == 0) <= (x & a == 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)
        break
