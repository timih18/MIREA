s = '0123456789ABCDE'
for x in s:
    a = int(f'98{x}79641', 22) + int(f'25{x}49', 22) + int(f'63{x}5', 22)
    if a % 21 == 0:
        print(a // 21)
        break
