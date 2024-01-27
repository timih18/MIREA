s = 'bltu'
sp = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                sp.append(a + b + c + d)
sp.sort()
print(sp[97])
