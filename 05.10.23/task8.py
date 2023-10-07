sp = []
for x in '01234567':
    for y in '1234567':
        a = int(f'{y}04{x}5', 11) + int(f'253{x}{y}', 8)
        if a % 117 == 0:
            sp.append(a)
print(min(sp) // 117)
