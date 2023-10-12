s = 'pytnisa'
cnt = 0
for a in 'pytisa':
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if word.count('y') == 1:
                        cnt += 1
print(cnt)
