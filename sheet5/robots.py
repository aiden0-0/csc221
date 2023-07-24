from gasp import *
from random import randint

def place_robots():
    global b, botx, boty
    botx = randint(0,63)
    boty = randint(0,47)
    b = Circle((10*botx + 5, 10*boty +5), 5, filled=True, color=color.RED)
    

def movebot():
    global botx, boty, b
    print('bots movin')
    if botx > player_x:
        botx -= 1
    if botx < player_x:
        botx += 1
    if boty > player_y:
        boty -= 1
    if boty < player_y:
        boty += 1
    move_to(b, (10*botx, 10*boty))

def place_player():
    global p, player_x, player_y
    player_x = randint(0,63)
    player_y = randint(0,47)
    p = Circle((10*player_x +5, 10*player_y +5), 5, filled=True)
    

def move_player():
    global p, player_x, player_y
    print('movin')
    key = update_when('key_pressed')
    
    if key == 'Up' and player_y < 47:
        player_y += 1
    if key == 'Left' and player_x > 0:
        player_x -= 1
    if key == 'Down' and player_y > 0:
        player_y -= 1
    if key == 'Right' and player_x < 63:
        player_x += 1
    if key == '8' and player_y < 47:
        player_y += 1
    if key == '4' and player_x > 0:
        player_x -= 1
    if key == '2' and player_y > 0:
        player_y -= 1
    if key == '6' and player_x < 63:
        player_x += 1
    elif key == '7':
        if player_y < 47:
            player_y +=1
        if player_x > 0:
            player_x -= 1
    elif key == '9':
        if player_y < 47:
            player_y += 1
        if player_x < 63:
            player_x += 1
    elif key == '1':
        if player_x > 0:
            player_x -= 1
        if player_y > 0:
            player_y -= 1
    elif key == '3':
        if player_y > 0:
            player_y -= 1
        if player_x < 63:
            player_x += 1

    move_to(p, (10*player_x, 10*player_y ))
    if key == 'space':
        remove_from_screen(p)
        place_player()
def collision():
    global done
    if botx - 1  <= player_x <= botx + 1  and boty - 1 <= player_y <= boty +1 :
        Text("Game over", (320, 240), size=50)
        sleep(3)
        done = True

begin_graphics()

done = False

place_player()
place_robots()

while not done:
    move_player()
    collision()
    movebot()
end_graphics()