a = 16**8 * 4**20 - 4*5 - 64
r = ''
while a > 0:
    r = str(a%4) + r
    a //= 4

print(r.count('3'))