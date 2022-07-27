import pygame

mouse_position = (0, 0)

def get_mouse_position():
    for event in pygame.event.get():
        last_mouse_position = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print('awa awa')