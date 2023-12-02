print('x y w z')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = ((x == (not y)) <= (y and (not z))) or (z and (not w))
                if not f:
                    print(x, y, w, z)
