import pygame
import time
  
surface = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption('PYGAME WINDOW')

image = pygame.image.load('ship.gif')

last_frame_time = time.time()
angle = 0
while True:
    surface.fill(0)

    rotated_surface = pygame.transform.rotate(image, angle)
    rect = rotated_surface.get_rect(center = (image.get_width()/2+50, image.get_height()/2+50))
    surface.blit(rotated_surface, (rect.x, rect.y))
    angle += 1

    pygame.display.update()

    print(f'{1/(time.time()-last_frame_time)} FPS')
    last_frame_time = time.time()
    clock.tick(60)