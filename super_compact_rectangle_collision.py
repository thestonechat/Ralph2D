import Ralph2D as ralph
window, clock = ralph.Window(title='Super Compact Rectangle Collision', width=500, height=500), ralph.Clock()
rect1, rect2, rect1_keys, rect2_keys = ralph.RectangleObject(window, (255, 0, 0), 50, 50, 50, 50), ralph.RectangleObject(window, (0, 0, 255), 150, 50, 50, 50), { 'w': False, 'a': False, 's': False, 'd': False }, { 'up': False, 'left': False, 'down': False, 'right': False }
while True:
    keys_up, keys_down = window.get_keys_up(), window.get_keys_down()
    rect1_keys, rect2_keys = { 'w': True if 'w' in keys_down else rect1_keys['w'], 'a': True if 'a' in keys_down else rect1_keys['a'], 's': True if 's' in keys_down else rect1_keys['s'], 'd': True if 'd' in keys_down else rect1_keys['d'] }, { 'up': False if 'up' in keys_up else rect2_keys['up'], 'left': False if 'left' in keys_up else rect2_keys['left'], 'down': False if 'down' in keys_up else rect2_keys['down'], 'right': False if 'right' in keys_up else rect2_keys['right'] }
    rect1_keys, rect2_keys = { 'w': False if 'w' in keys_up else rect1_keys['w'], 'a': False if 'a' in keys_up else rect1_keys['a'], 's': False if 's' in keys_up else rect1_keys['s'], 'd': False if 'd' in keys_up else rect1_keys['d'] }, { 'up': True if 'up' in keys_down else rect2_keys['up'], 'left': True if 'left' in keys_down else rect2_keys['left'], 'down': True if 'down' in keys_down else rect2_keys['down'], 'right': True if 'right' in keys_down else rect2_keys['right'] }
    w, a, s, d, up, left, down, right, collision = rect1.move_y(-5) if rect1_keys['w'] else None, rect1.move_x(-5) if rect1_keys['a'] else None, rect1.move_y(5) if rect1_keys['s'] else None, rect1.move_x(5) if rect1_keys['d'] else None, rect2.move_y(-5) if rect2_keys['up'] else None, rect2.move_x(-5) if rect2_keys['left'] else None, rect2.move_y(5) if rect2_keys['down'] else None, rect2.move_x(5) if rect2_keys['right'] else None, print('Collision Detected!') if ralph.check_collision(rect1, rect2) else None
    rect1.update(), rect2.update(), window.update(), window.clear(), clock.tick(60)