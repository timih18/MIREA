for x in '0123456789ABCD':
    a = int(f'1{x}563', 14) + int(f'871{x}3', 14)
    if a % 24 == 0:
        print(a // 24)
        break
