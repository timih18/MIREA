print('x y w z')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = ((x <= y) == (w <= x)) and (z <= w)
                if f:
                    print(x, y, w, z)
