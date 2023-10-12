glas = 'oa'
sogl = 'rsmx'
cnt = 0
for a in glas:
    for b in sogl:
        for c in glas:
            for d in sogl:
                for e in glas:
                    for f in sogl:
                        for g in glas:
                            for h in sogl:
                                w = a + b + c + d + e + f + g + h
                                if w.count('r') == 1 and w.count('o') == 2 and w.count('s') == 1 and w.count('m') == 1 and w.count('a') == 2 and w.count('x') == 1:
                                    cnt += 2
print(cnt)
