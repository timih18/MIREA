print('x y w z')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = ((y <= x) and (z or w)) <= ((x and (not w)) or (y == z))
                if not f:
                    print(x, y, w, z)
