from ball import pymunk, pygame

class MultiplierBox:
    
    def __init__(self, space, screen, layers, width, height, pos, collision_type):
        self.space = space
        self.screen = screen
        self.layers = layers
        self.width = width
        self.height = height
        self.pos = pos
        
        self.multiplier = chr(collision_type + 95)

        self.vertices = [(0, self.height*2),         #bottom left
            (self.width, self.height*2),   #bottom right
            (self.width, self.height/2),   #top roght
            (0, self.height/2)]         #top left

        self.body = pymunk.Body(body_type= pymunk.Body.STATIC)
        self.body.position = pos
        self.shape = pymunk.Poly(self.body, self.vertices)
        self.shape.elasticity = 0
        self.shape.friction = 1
        self.shape.color = self.calculate_box_color(pos)
        self.shape.collision_type = collision_type
        #shape.filter = pymunk.ShapeFilter(group=1)
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
        
    
    def calculate_multipliers(self):
        for i in range(len(self.boxes_positions)):
            self.multipliers.update({f'szmata{i}' : 1})
            
    def display_multiplier(self):
        font = pygame.font.SysFont("Arial", 20, True, False)
        
        surface = font.render(str(self.multiplier), True, (255, 255, 255))

        center_pos = [self.pos[0] + 10, self.pos[1] + 15]

        self.screen.blit(surface, center_pos)