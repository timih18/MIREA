a = 729**7 + 3**16 - 18
r = ''
while a > 0:
    r = str(a % 9) + r
    a //= 9
print(r.count('0'))
