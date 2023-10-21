sp = []
for x in range(7):
    for y in range(1, 7):
        a = int(f'{y}{x}320', 7) + int(f'1{x}3{y}3', 9)
        if a % 181 == 0:
            sp.append(a)
print(min(sp) // 181)
