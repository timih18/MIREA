for x in '012345678':
    a = int(f'88{x}4{x}', 9) + int(f'7{x}344', 9)
    if a % 67 == 0:
        print(a // 67)
        break
