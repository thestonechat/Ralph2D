import Ralph2D as ralph
import time

window = ralph.Window(title='Image Test', width=500, height=500)
clock = ralph.Clock()

test_img = ralph.load_image('ship.gif')

last_frame_time = time.time()
reverse = False
size = 0
while True:
    window.clear()

    if reverse == False:
        size+=1
        if not size < 50:
            reverse = True
            size-=1
    else:
        size-=1
        if not size > 0:
            reverse = False
            size+=1
    
    smaller_img = ralph.resize_image(test_img, test_img.get_width()-size, test_img.get_height()-size)
    window.draw_image_centered(smaller_img, 50, 50, original_width=test_img.get_width(), original_height=test_img.get_height())

    window.update()
    
    print(f'{1/(time.time()-last_frame_time)} FPS')
    last_frame_time = time.time()
    clock.tick(60)