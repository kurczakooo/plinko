import pygame
import pymunk, pymunk.pygame_util
import random
import math
                 
                 
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



def create_static_circle(space, position, radius):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.5
    shape.friction = 0.5
    shape.color = (255, 255, 255, 255)
    space.add(body, shape)
    return shape

    
    
def calculate_box_color(screen, layers, pos) -> tuple:
    red = 0
    green = 0
    blue = 0
    alpha = 255
    
    center_x = screen.get_width()/2 - 20 #should be 360 if the screen is 720 wide
    
    distance_from_center = abs(center_x - pos[0])
    
    if layers < 10:
        red = int(255 - distance_from_center)
        green = int(distance_from_center)
    elif layers <= 13:
        red = int(255 - distance_from_center/1.5)
        green = int(distance_from_center/1.5)
    else:
        red = int(255 - distance_from_center/2)
        green = int(distance_from_center/2)
    
    return (red, green, blue, alpha)
    
    
def create_bottom_layer(screen, space, layers, pins_pos):
    spacing = 40
    number_of_boxes = layers + 2 + 1 #bottom layers formula and two boxes for outside(TO DO)
    
    first_pin_bottom_layer_pos = pins_pos[len(pins_pos) - number_of_boxes + 1]
    
    local_pos = list(first_pin_bottom_layer_pos)
    local_pos[0] -= 40
    
    boxes = []
    
    for i in range(number_of_boxes):
        #print(local_pos)
        boxes.append(create_bottom_multiplier_box(screen, space, local_pos, layers))
        #IF CHECKING BALL Y POS DOESNT WORK, THEN MAKE FIRST AND LAST BOX LONGER, BUT IT
        #FUCKS WITH COLORS  
        #if i == 0:
        #    local_pos[0] -= 500
        #    create_bottom_multiplier_box(screen, space, local_pos, 500)
        #    local_pos[0] += 500
        #elif i == number_of_boxes - 1:
        #    create_bottom_multiplier_box(screen, space, local_pos, 500)
        local_pos[0] +=  spacing
        
    return boxes
        
def display_wallet(screen, pos, amount):
    font = pygame.font.SysFont("Times New Roman", 40, True, False)
    
    surface = font.render(amount, True, (255, 255, 255))

    screen.blit(surface, pos)