import turtle as t


k = 30
t.left(90)

for _ in range(6):
    t.forward(10*k)
    t.right(60)

t.up()
for x in range(120):
    for y in range(-10, 20):
        t.goto(x*k, y*k)
        t.dot(4)
