file = open('17.txt', 'r')
sp = [int(i) for i in file.readlines()]

cnt = 0
mx = 0
for i in range(len(sp)-1):
    for j in range(i+1, len(sp)):
        if (sp[i] + sp[j]) % 7 == 0:
            cnt += 1
            mx = max(mx, sp[i] + sp[j])
print(cnt, mx)
