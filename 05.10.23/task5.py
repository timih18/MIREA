for x in '0123456789ABCDEF':
    a = int(f'2{x}BAD', 16) + int(f'3C{x}FE', 16)
    if a % 15 == 0:
        print(a // 15)
