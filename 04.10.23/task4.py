for x in range(13):
    a = x*13**3 + 10*13**2 + 4
    b = 18**3 + 13*18**2 + x*18 + 3
    if (a + b) % 184 == 0:
        print((a + b) // 184)
        break
