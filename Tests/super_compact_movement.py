import Ralph2D as ralph
window = ralph.Window(title='red box do car', width=500, height=500)
clock = ralph.Clock()
rectangle_obc = ralph.RectangleObject(window, (255, 0, 0), 50, 50, 50, 50)
keys_pressed = { 'w': False, 'a': False, 's': False, 'd': False }
while True:
    window.clear()
    mouse_pos, keys_up, keys_down = window.get_mouse_pos(), window.get_key_up(), window.get_key_down()
    keys_pressed = { 'w': keys_pressed['w'] if 'w' not in keys_down else True, 'a': keys_pressed['a'] if 'a' not in keys_down else True, 's': keys_pressed['s'] if 's' not in keys_down else True, 'd': keys_pressed['d'] if 'd' not in keys_down else True }
    keys_pressed = { 'w': keys_pressed['w'] if 'w' not in keys_up else False, 'a': keys_pressed['a'] if 'a' not in keys_up else False, 's': keys_pressed['s'] if 's' not in keys_up else False, 'd': keys_pressed['d'] if 'd' not in keys_up else False }
    if keys_pressed['w']: rectangle_obc.move_y(-5)
    if keys_pressed['a']: rectangle_obc.move_x(-5)
    if keys_pressed['s']: rectangle_obc.move_y(5)
    if keys_pressed['d']: rectangle_obc.move_x(5)
    rectangle_obc.update()
    window.update()
    clock.tick(60)