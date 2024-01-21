for a in range(1000):
    flag = True
    for x in range(100):
        for y in range(100):
            f = (x > a) or (y > x) or (2*y + x < 110)
            if not f:
                flag = False
                break
    if flag:
        print(a)
