import turtle as t


t.left(90)
k = 30

for _ in range(3):
    t.forward(7*k)
    t.right(90)

t.forward(10*k)

for _ in range(3):
    t.left(90)
    t.forward(6*k)

t.up()
for x in range(-10, 100):
    for y in range(-15, 15):
        t.goto(x*k, y*k)
        t.dot(4)
