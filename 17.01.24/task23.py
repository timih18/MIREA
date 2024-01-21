a = 343**5 - 7**9 + 48
res = ''
while a > 0:
    res = str(a % 7) + res
    a //= 7
print(res.count('6'))
