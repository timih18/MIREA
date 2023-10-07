for x in '0123456789ABCDEF':
    a = int(f'8{x}84{x}', 16) + int(f'78{x}34', 16)
    if a % 23 == 0:
        print(a // 23)
        break
