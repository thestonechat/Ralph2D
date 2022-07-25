import pygame
import time

class Clock():
    def __init__(self):
        self.last_call = time.time()

    def tick(self, FPS=60):
        time_elapsed = time.time()-self.last_call
        fps = 1/FPS - time_elapsed

        if fps >= 0:
            time.sleep(fps)

        self.last_call = time.time()

def rotate(surface, rotation, x=None, y=None):
    '''
        surface = image or shape
        rotation = degree of rotation
        x = X location of the image
        y = Y location of the image
    '''
    rotated_image = pygame.transform.rotate(surface, rotation)
    return rotated_image

def load_image(path):
    return pygame.image.load(path)

def resize_image(image, width, height):
    return pygame.transform.scale(image, (width, height))