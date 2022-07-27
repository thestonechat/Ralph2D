import Ralph2D as ralph
from Ralph2D.Physics import check_collision
import time
window = ralph.Window(title='Image Test', width=500, height=500)
clock = ralph.Clock()
rect1 = ralph.RectangleObject(window, (255, 0, 0), 50, 50, 50, 50)
rect2 = ralph.RectangleObject(window, (0, 0, 255), 150, 50, 50, 50)
last_frame_time = time.time()

rect1_keys = { 'w': False, 'a': False, 's': False, 'd': False }
rect2_keys = { 'up': False, 'left': False, 'down': False, 'right': False }

window.use_object(rect1)
window.use_object(rect2)
while True:
    window.clear()
    mouse_pos = window.get_mouse_pos()
    keys_down = window.get_key_down()
    keys_up = window.get_key_up()

    for key in keys_down:
        if key in rect1_keys: rect1_keys[key] = True
        if key in rect2_keys: rect2_keys[key] = True
    for key in keys_up:
        if key in rect1_keys: rect1_keys[key] = False
        if key in rect2_keys: rect2_keys[key] = False

    # Move rectangle 1
    if rect1_keys['w']: rect1.move_y(-5)
    if rect1_keys['a']: rect1.move_x(-5)
    if rect1_keys['s']: rect1.move_y(5)
    if rect1_keys['d']: rect1.move_x(5)

    # Move rectangle 2
    if rect2_keys['up']: rect2.move_y(-5)
    if rect2_keys['left']: rect2.move_x(-5)
    if rect2_keys['down']: rect2.move_y(5)
    if rect2_keys['right']: rect2.move_x(5)

    if check_collision(rect1, rect2):
        print('Collision Detected!')

    window.update()
    clock.tick(60)