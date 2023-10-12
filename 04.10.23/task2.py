sp = []
for x in range(1, 9):
    for y in range(9):
        a = 2*9**4 + y*9**3 + 6*9**2 + 6*9 + x
        b = x*12**3 + y*12 + 1
        if (a + b) % 170 == 0:
            sp.append(a + b)
print(min(sp) // 170)
