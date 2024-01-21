for one in range(100):
    for two in range(100):
        for three in range(100):
            s = '0' + '1' * one + '2' * two + '3' * three
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 50 and s.count('2') == 12 and s.count('3') == 7:
                print(one)
