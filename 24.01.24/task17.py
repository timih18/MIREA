file = open('17.txt', 'r')
sp = [int(i) for i in file.readlines()]

cnt = 0
mn = 200001

min5 = 1000
for i in sp:
    if len(str(i)) == 3 and i % 10 == 5 and i < min5:
        min5 = i

for i in range(len(sp)-1):
    if (len(str(sp[i])) == 3 and len(str(sp[i+1])) != 3) or (len(str(sp[i+1])) == 3 and len(str(sp[i])) != 3):
        if (sp[i] + sp[i+1]) % min5 == 0:
            cnt += 1
            mn = min(mn, sp[i] + sp[i+1])
print(cnt, mn)
