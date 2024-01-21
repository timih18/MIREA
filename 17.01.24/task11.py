s = 'akru'
sp = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    sp.append(a + b + c + d + e)
sp.sort()
print(sp.index('rukaa')+1)
