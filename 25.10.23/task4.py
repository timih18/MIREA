print('x y w z')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = ((x <= y) == (y <= z)) and (y or w)
                if f:
                    print(x, y, w, z)
