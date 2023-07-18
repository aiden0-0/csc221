from gasp import *
from random import randint
player_x = randint(0,63)
player_y = randint(0,47)


def place_player():
    global c
    c = Circle((10*player_x +5, 10*player_y +5), 5, filled=True)

def move_player():
    global c, player_x, player_y
    print('movin')
    key = update_when('key_pressed')
    
    if key == 'Up' and player_y < 47:
        player_y += 3
    if key == 'Left' and player_x > 0:
        player_x -= 3
    if key == 'Down' and player_y > 0:
        player_y -= 3
    if key == 'Right' and player_x < 63:
        player_x += 3 

    move_to(c, (player_x, player_y ))
    remove_from_screen(c)

begin_graphics()
while True:
    place_player()
    move_player()