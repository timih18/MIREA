cnt = 0
for i in range(1000, 10000):
    s = str(i)
    if '0' not in s and '2' not in s and '4' not in s and '6' not in s and '8' not in s:
        sp = [i//1000 + i%1000//100, i%100//10 + i%10]
        sp.sort()
        if sp[0] == 4 and sp[1] == 14:
            cnt += 1
print(cnt)
