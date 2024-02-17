file = open('107_17.txt')
sp = [int(i) for i in file.readlines()]

min_21 = 100001
for i in sp:
    if i % 21 == 0:
        min_21 = min(i, min_21)

cnt = 0
mx = 0
for i in range(len(sp)-1):
    if sp[i] % min_21 == 0 or sp[i+1] % min_21 == 0:
        cnt += 1
        mx = max(sp[i] + sp[i+1], mx)

print(cnt, mx)
