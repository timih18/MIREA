import turtle as t


k = 30
t.left(90)
for _ in range(3):
    t.forward(7*k)
    t.right(90)
t.forward(8*k)
for _ in range(3):
    t.left(90)
    t.forward(5*k)

t.up()
for x in range(-2, 100):
    for y in range(-5 ,8):
        t.goto(x*k, y*k)
        t.dot(4)
