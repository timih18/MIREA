s = 'sveta'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if word.count('s') > 0:
                        cnt += 1
print(cnt)
