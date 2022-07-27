class ImageObject():
    def __init__(self, surface, image, x, y):
        self.surface = surface
        self.image = image
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_width()

    def update(self):
        self.surface.draw_image(self.image, self.x, self.y)


    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color


    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def move_x(self, n):
        self.x += n

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def move_y(self, n):
        self.y += n


    def set_width(self, width):
        self.width = width

    def change_width(self, n):
        self.width += n
    
    def set_height(self, height):
        self.height = height

    def change_height(self, n):
        self.height += n


    def move(self, x, y):
        self.x += x
        self.y += y

    def move_to(self, x, y):
        self.x = x
        self.y = y


    
    ### CENTER SHIT
    def move_to_center(self, x, y):
        self.x = x - int(self.width/2)
        self.y = y - int(self.height/2)