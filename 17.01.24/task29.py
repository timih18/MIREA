file = open('17.txt', 'r')
sp = [int(i) for i in file.readlines()]

cnt = 0
mx = 0
for i in range(len(sp)-2):
    a = sp[i]
    b = sp[i+1]
    c = sp[i+2]
    if a == max(a, b, c):
        if a**2 == b**2 + c**2:
            cnt += 1
            if a + b + c > mx:
                mx = a + b + c
    if b == max(a, b, c):
        if a**2 == b**2 + c**2:
            cnt += 1
            if a + b + c > mx:
                mx = a + b + c
    if c == max(a, b, c):
        if a**2 == b**2 + c**2:
            cnt += 1
            if a + b + c > mx:
                mx = a + b + c
print(cnt, mx)
