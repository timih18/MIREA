s = '3' * 68
while '999' in s or '333' in s:
    if '333' in s:
        s = s.replace('333', '9', 1)
    else:
        s = s.replace('999', '3', 1)
print(s)
