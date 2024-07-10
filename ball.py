import pygame
import pymunk, pymunk.pygame_util
import random
                 
                 
class Ball:
    def __init__(self, radius, position, space):
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, radius))
        self.body.position = position
        self.body.velocity = (random.uniform(-10, 10), 0)
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0.85

        self.shape.friction = 0.5
        self.shape.collision_type = 1
        self.shape.filter = pymunk.ShapeFilter(group=1)
        self.shape.color = (255, 0, 0, 255)
        space.add(self.body, self.shape)      
        
    def collide(self, arbiter, space, data):
        del self



    
        
