import turtle as t


t.left(90)
k = 30

for _ in range(4):
    t.forward(8*k)
    t.right(150)
    t.forward(8*k)
    t.right(30)

t.up()
for x in range(100):
    for y in range(-10, 10):
        t.goto(x*k, y*k)
        t.dot(4)