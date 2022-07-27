class RectangleObject():
    def __init__(self, surface, color, x, y, width, height):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        self.surface.draw_rectangle(self.color, self.x, self.y, self.width, self.height)


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