print('x y w z')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = (((not z) or w) and ((not x) == y)) <= (x and z)
                if not f:
                    print(x, y, w, z)
                    