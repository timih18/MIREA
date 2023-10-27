for a in range(100):
    flag = True
    for x in range(100):
        f = (x & 17 == 0) <= ((x & 29 != 0) <= (x & a != 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)
        break
