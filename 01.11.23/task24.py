a = 9**8 + 3**8 - 2
res = ''
while a > 0:
    res = str(a % 3) + res
    a //= 3
print(res.count('2'))
