file = open('17.txt', 'r')
sp = [int(i) for i in file.readlines()]

cnt = 0
mx = 0
for i in range(len(sp)-1):
    for j in range(i + 1, len(sp)):
        if ((abs(sp[i] - sp[j])) % 36 == 0) and (sp[i] % 13 == 0 or sp[j] % 13 == 0):
            cnt += 1
            mx = max(mx, abs(sp[i] - sp[j]))
print(cnt, mx)
