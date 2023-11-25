s = '12345'
cnt =  0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    w = a + b + c + d + e
                    if w.count('1') == 3:
                        cnt += 1
print(cnt)
