import pygame
import Ralph2D as ralph
from Ralph2D.Collisions import Collisions
import time

window = ralph.Window(title='Image Test', width=500, height=500)
clock = ralph.Clock()

rectangle_obc = ralph.RectangleObject(window, (255, 0, 0), 50, 50, 50, 50)
rectangle_obc_2 = ralph.RectangleObject(window, (255, 0, 0), 50, 50, 50, 50)

Collisions().check(rectangle_obc, rectangle_obc_2)

last_frame_time = time.time()
keys_pressed = {
    'w': False,
    'a': False,
    's': False,
    'd': False
}
while True:
    window.clear()

    mouse_pos = window.get_mouse_pos()
    keys_down = window.get_key_down()
    keys_up = window.get_key_up()

    for key in keys_down:
        if key in keys_pressed:
            keys_pressed[key] = True

    for key in keys_up:
        if key in keys_pressed:
            keys_pressed[key] = False

    if keys_pressed['w']:
        rectangle_obc.move_y(-5)

    if keys_pressed['a']:
        rectangle_obc.move_x(-5)

    if keys_pressed['s']:
        rectangle_obc.move_y(5)

    if keys_pressed['d']:
        rectangle_obc.move_x(5)

    rectangle_obc.update()

    window.update()
    
    # print(f'{1/(time.time()-last_frame_time)} FPS')
    last_frame_time = time.time()
    clock.tick(60)