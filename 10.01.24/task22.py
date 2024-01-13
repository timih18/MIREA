for a in range(100):
    flag = True
    for x in range(100):
        for y in range(100):
            f = (y + 2*x != 48) or (a < x) or (x < y)
            if not f:
                flag = False
                break
    if flag:
        print(a)
