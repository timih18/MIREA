a = 3*216**4 + 2*36**6 - 648
s = ''
while a > 0:
    s = str(a % 6) + s
    a //= 6
print(s.count('5'))
