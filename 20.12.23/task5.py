import turtle as t


t.left(90)
k = 30
for _ in range(10):
    t.forward(5*k)
    t.right(60)
t.up()
for x in range(100):
    for y in range(-5, 10):
        t.goto(x*k, y*k)
        t.dot(4)