from gasp import *
from random import randint
player_x = randint(0,63)
player_y = randint(0,47)
botx = randint(0,63)
boty = randint(0,47)

def place_robots():
    global b
    b = Circle((10*botx + 5, 10*boty +5), 5, filled=True, color=color.RED)

def movebot():
    global botx, boty, b
    print('bots movin')
    if botx > player_x:
        botx -= 3
    if botx < player_x:
        botx += 3
    if boty > player_y:
        boty -= 3
    if boty < player_y:
        boty += 3
    move_to(b, (10*botx, 10*boty))

def place_player():
    global p
    p = Circle((10*player_x +5, 10*player_y +5), 5, filled=True)

def move_player():
    global p, player_x, player_y
    print('movin')
    key = update_when('key_pressed')
    
    if key == 'Up' and player_y < 47:
        player_y += 2
    if key == 'Left' and player_x > 0:
        player_x -= 2
    if key == 'Down' and player_y > 0:
        player_y -= 2
    if key == 'Right' and player_x < 63:
        player_x += 2
    move_to(p, (10*player_x, 10*player_y ))

def collision():
    global done
    if player_x == botx and player_y == boty:
        Text("Game over", (320, 240), size=50)
        sleep(3)

begin_graphics()

done = False

place_player()
place_robots()

while not done:
    move_player()
    collision()
    movebot()
end_graphics()