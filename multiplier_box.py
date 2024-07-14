from ball import pymunk

class MultiplierBox:
    
    def _init__(self, space, screen, width, height, pos, collision_type):
        self.space = space
        self.screen = screen
        self.width = width
        self.height = height
        self.pos = pos
        
    