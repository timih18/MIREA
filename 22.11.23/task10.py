for i in range(10000, 100000):
    sp = [i//10000 + i%1000//100 + i%10, i%10000//1000 + i%100//10]
    sp.sort()
    if sp[0] == 7 and sp[1] == 23:
        print(i)
        break
