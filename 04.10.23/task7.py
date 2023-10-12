for x in range(12):
    a = 3*14**3 + x*14**2 + 13*14 + 10
    b = 5*12**3 + x*12**2 + 10*12 + 6
    if (a + b) % 81 == 0:
        print((a + b) // 81)
        break
