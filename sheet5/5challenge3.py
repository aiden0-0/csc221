from gasp import *
begin_graphics()
x = 5
y = 5
c = Circle((x, y), 5)
while True:
    x += 4
    y += 3
    move_to(c, (x,y))
    sleep(.02)
