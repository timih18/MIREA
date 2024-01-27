file = open('17.txt', 'r')
sp = [int(i) for i in file.readlines()]

min3 = 10001
for i in sp:
    if abs(i) % 10 == 3:
        min3 = min(min3, i)
min3 *= min3
cnt = 0
mx = 0
for i in range(len(sp)-1):
    if sp[i]**2 + sp[i+1]**2 < min3 and abs(min(sp[i], sp[i+1])) % 10 == 3:
        cnt += 1
        mx = max(mx, sp[i]**2 + sp[i+1]**2)
print(cnt, mx)
