for x in '123456789ABCDE':
    a = int(f'{x}B09', 17) + int(f'{x}8E8', 15)
    if a % 155 == 0:
        print(a // 155)
        break
        