for x in '123456789ABC':
    a = int(f'{x}A04', 13) + int(f'1D{x}3', 18)
    if a % 184 == 0:
        print(a // 184)
        break
