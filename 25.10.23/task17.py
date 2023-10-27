for x in '0123456789ABC':
    a = int(f'8{x}71', 13) + int(f'3{x}DF', 17)
    if a % 197 == 0:
        print(a // 197)
        break
