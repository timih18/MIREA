sp = []
s = 'aou'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    sp.append(word)
sp.sort()
print(sp.index('oaaaa') + 1)
