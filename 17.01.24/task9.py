import turtle as t


k = 30
t.left(90)

for _ in range(10):
    t.forward(5*k)
    t.right(60)

t.up()
for x in range(-3, 100):
    for y in range(-5, 7):
        t.goto(x*k, y*k)
        t.dot(4)
