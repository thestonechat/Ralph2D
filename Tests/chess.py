import Ralph2D as ralph
import time

window = ralph.Window(title='EPIC WINDOW', width=512, height=512)

white_color = (199, 147, 129)
black_color = (173, 79, 47)

def draw_chess_board():
    for i in range(8):
        for n in range(8):
            x = n*64
            y = i*64

            if i % 2 == 0:
                if n % 2 == 0:
                    window.draw_rectangle(black_color, x, y, 64, 64)
                else:
                    window.draw_rectangle(white_color, x, y, 64, 64)
            else:
                if n % 2 == 0:
                    window.draw_rectangle(white_color, x, y, 64, 64)
                else:
                    window.draw_rectangle(black_color, x, y, 64, 64)

last_frame_time = time.time()
while True:
    window.clear()
    draw_chess_board()
    window.update()

    print(f'{1/(time.time()-last_frame_time)} FPS')
    last_frame_time = time.time()