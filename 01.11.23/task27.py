mx = 0
for a in range(100):
    flag = True
    for x in range(100):
        for y in range(100):
            f = (2*x + y != 70) or (x < y) or (a < x)
            if not f:
                flag = False
                break
    if flag:
        mx = a
print(mx)
