class CircleObject():
    def __init__(self, surface, color, x, y, radius):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.width = radius*2
        self.height = radius*2
        self.radius = radius

    def update(self):
        self.surface.draw_circle(self.color, self.x, self.y, self.radius)


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


    def set_radius(self, radius):
        self.radius = radius

    def change_radius(self, n):
        self.radius += n
    

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