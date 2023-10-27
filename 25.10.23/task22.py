mx = 0
for a in range(-100, 100):
    flag = True
    for x in range(1000):
        f = (x & a != 0) <= ((x & 10 == 0) <= (x & 3 != 0))
        if not f:
            flag = False
    if flag:
        mx = a
print(mx)
