from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
rad = math.radians(1)

while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)

    x = x + (20 * math.cos(rad))
    y = y + (20 * math.sin(rad))
    rad = rad + math.radians(5)

    character.draw_now(x + 400, y + 90)
    delay(0.01)
    
close_canvas()
