sp = []
for x in '123456789AB':
    for y in '123456789AB':
        a = int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)
        if a % 80 == 0:
            sp.append(a // 80)
print(min(sp))
