from ball import pymunk, pygame

class MultiplierBox:
    
    def __init__(self, space, screen, layers, width, height, pos, collision_type, is_outer):
        self.space = space
        self.screen = screen
        self.layers = layers
        self.width = width
        self.height = height
        self.pos = pos
        self.is_outer = is_outer
        self.collision_type = collision_type
        
        self.multiplier = 0
        
        self.vertices = [(0, self.height*2),         #bottom left
            (self.width, self.height*2),   #bottom right
            (self.width, self.height/2),   #top roght
            (0, self.height/2)]         #top left

        self.body = pymunk.Body(body_type= pymunk.Body.STATIC)
        self.body.position = pos
        self.shape = pymunk.Poly(self.body, self.vertices)
        self.shape.elasticity = 0
        self.shape.friction = 1
        self.shape.color = (0, 0, 0, 255) if self.is_outer else self.calculate_box_color(pos)
        self.shape.collision_type = collision_type
        self.space.add(self.body, self.shape)
        
    
    
    def calculate_box_color(self, pos) -> tuple:
        red = 0
        green = 0
        blue = 0
        alpha = 255
        
        center_x = self.screen.get_width()/2 - 20 #should be 360 if the screen is 720 wide
        
        distance_from_center = abs(center_x - pos[0])
        
        if self.layers < 10:
            red = int(255 - distance_from_center)
            green = int(distance_from_center)
        elif self.layers <= 13:
            red = int(255 - distance_from_center/1.5)
            green = int(distance_from_center/1.5)
        else:
            red = int(255 - distance_from_center/2)
            green = int(distance_from_center/2)
        
        return (red, green, blue, alpha)
        
        
    
    def set_multiplier(self, value):
        self.multiplier = value
          
          
            
    def display_multiplier(self):
        font = pygame.font.SysFont("Arial", 15, True, False)
        
        surface = font.render(str(self.multiplier if not self.is_outer else ""), True, (255, 255, 255))

        center_pos = [self.pos[0] +  self.width/3, self.pos[1] + self.height/1.5]

        self.screen.blit(surface, center_pos)