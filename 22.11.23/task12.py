mx = 0
for i in range(1000):
    n = bin(i)[2:]
    if i % 3 == 0:
        n = n + n[-3:]
    else:
        ost = (i % 3) * 3
        n = n + bin(ost)[2:]
    r = int(n, 2)
    if 170 > r > mx:
        mx = r
print(mx)
