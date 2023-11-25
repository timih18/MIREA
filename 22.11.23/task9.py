res = 0
for i in range(100):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = n + '00'
    else:
        n = n + '11'
    r = int(n, 2)
    if r < 134:
        res = i
    else:
        break
print(res)
