import turtle as t


k = 30
t.left(90)

for _ in range(6):
    t.right(36)
    t.forward(10*k)
    t.right(36)

t.up()
for x in range(0, 100):
    for y in range(-10, 10):
        t.goto(x*k, y*k)
        t.dot(3)
