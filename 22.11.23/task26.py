s = '012345678'
sp = []
for x in s[1:]:
    for y in s:
        a = int(f'2{y}66{x}', 9) + int(f'{x}0{y}1', 12)
        if a % 170 == 0:
            sp.append(a // 170)
print(min(sp))
