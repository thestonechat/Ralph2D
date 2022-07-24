import pygame
import time

pygame.init()
  
surface = pygame.display.set_mode((512,512))
  
white_color = pygame.Color(199, 147, 129)
black_color = pygame.Color(173, 79, 47)

def draw_chess_board():
    for i in range(8):
        for n in range(8):
            x = n*64
            y = i*64

            if i % 2 == 0:
                if n % 2 == 0:
                    pygame.draw.rect(surface, black_color, pygame.Rect(x, y, 64, 64))
                else:
                    pygame.draw.rect(surface, white_color, pygame.Rect(x, y, 64, 64))
            else:
                if n % 2 == 0:
                    pygame.draw.rect(surface, white_color, pygame.Rect(x, y, 64, 64))
                else:
                    pygame.draw.rect(surface, black_color, pygame.Rect(x, y, 64, 64))

last_frame_time = time.time()
while True:

    draw_chess_board()
    pygame.display.update()

    print(f'{1/(time.time()-last_frame_time)} FPS')
    last_frame_time = time.time()