for x in '0123456789ABCDE':
    a = int(f'97968{x}13', 15) + int(f'7{x}213', 15)
    if a % 14 == 0:
        print(a//14)
        break
