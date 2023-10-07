a = 125**4 + 25**8 - 30
s = ''
while a > 0:
    s = str(a % 5) + s
    a //= 5
print(s.count('4'))
