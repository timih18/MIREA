import turtle as t


k = 30
t.left(90)
for _ in range(4):
    t.forward(10*k)
    t.right(90)

t.up()
for x in range(0, 100):
    for y in range(0, 11):
        t.goto(x*k, y*k)
        t.dot(4)
