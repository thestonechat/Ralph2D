import sys
import ctypes
from sdl2 import *
from sdl2 import ext
import sdl2
import time

class Window():
    def __init__(self, title='', width=255, height=255):
        self.empty = ext.Color(0,0,0)
        win_flags = (
            sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN
        )
        self.window = ext.Window(title, (width, height), flags=win_flags)
        self.surface = self.window.get_surface()

    def update(self):
        self.window.refresh()

    def quit(self):
        SDL_DestroyWindow(self.window)
        SDL_Quit()



    def clear(self):
        ext.fill(self.surface, self.empty)

    def draw_rectangle(self, color, x, y, width, height):
        ext.fill(self.surface, color, (x, y, width, height))




def Color(r=255, g=255, b=255):
    return ext.Color(r, g, b)