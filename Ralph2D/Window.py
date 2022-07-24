import sys
import ctypes
from sdl2 import *
import time

def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Hello World",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              500, 500, SDL_WINDOW_SHOWN)
    windowsurface = SDL_GetWindowSurface(window)

    
    SDL_UpdateWindowSurface(window)

    running = True
    event = SDL_Event()
    last_frame_time = time.time()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break

        
        print(f'{1/(time.time()-last_frame_time)} FPS')
        last_frame_time = time.time()

    SDL_DestroyWindow(window)
    SDL_Quit()
    # return None

if __name__ == "__main__":
    sys.exit(main())
