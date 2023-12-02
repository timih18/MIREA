import turtle as t


k = 15
t.left(90)
t.right(315)
for _ in range(7):
    t.forward(16*k)
    t.right(45)
    t.forward(8*k)
    t.right(135)

t.up()
for x in range(-15, 100):
    for y in range(25):
        t.goto(x*k, y*k)
        t.dot(4)
