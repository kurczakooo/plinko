from ball import pymunk, pygame

class Boundaries:
    def __init__(self, space):
        self.space = space
        self.width = 10
        self.height = 500
        
        self.vertices_left = [(0, self.height*2),         #bottom left
            (self.width, self.height*2),   #bottom right
            (self.width, 0),   #top roght
            (0, 0)]         #top left
        
        self.body_left = pymunk.Body(body_type= pymunk.Body.STATIC)
        self.body_left.position = (1000, 100)
        self.shape_left = pymunk.Poly(self.body_left, self.vertices_left)
        self.shape_left.elasticity = 1
        self.shape_left.friction = 0
        
        self.space.add(self.body_left, self.shape_left)
        
        ##############################################################
        
        self.vertices_right = [(-100, self.height*2),         #bottom left
            (self.width-100, self.height*2),   #bottom right
            (self.width+200, 0),   #top roght
            (200, 0)]         #top left
        
        self.body_right = pymunk.Body(body_type= pymunk.Body.STATIC)
        self.body_right.position = (270, 10)
        self.shape_right = pymunk.Poly(self.body_right, self.vertices_right)
        self.shape_right.elasticity = 1
        self.shape_right.friction = 0.5
        self.shape_right.color = (0, 0, 0, 255)
        
        self.space.add(self.body_right, self.shape_right)