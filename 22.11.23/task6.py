print('x y z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x == z) or (x <= (y and z))
            if not f:
                print(x, y, z)
                