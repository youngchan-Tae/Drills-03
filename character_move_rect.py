from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0

while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    if(x <= 790 and y == 0):
        x = x + 4
    elif(x >= 790 and y <= 500):
        y = y + 4
    elif(x >= 0 and y >= 500):
        x = x - 4
    elif(x <= 0 and y <= 520):
        y = y - 4

    character.draw_now(x, y + 90)
    delay(0.01)
    
close_canvas()
