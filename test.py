import Ralph2D as ralph

window = ralph.Window(width=500, height=500)
clock = ralph.Clock()

image = ralph.load_image('ship.png')
image = ralph.resize_image(image, 100, 100)

image_obj = ralph.ImageObject(window, image, 0, 0)

window.use_object(image_obj)
kets_pressed = {'w': False, 'a': False, 's': False, 'd': False}
while True:
    window.clear()

    keys_down = window.get_keys_down()
    keys_up = window.get_keys_up()

    

    image_obj.move_x(1)

    window.update()
    clock.tick(60)