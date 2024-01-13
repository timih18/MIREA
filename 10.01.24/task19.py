a = 729**6 + 3**14 - 36
r = ''
while a > 0:
    r = str(a % 9) + r
    a //= 9
print(r.count('0'))
