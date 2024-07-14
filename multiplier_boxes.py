from ball import pymunk
import pymunk.pygame_util

class MultiplierBoxesLayer :
    
    def __init__(self, space, screen, layers):
        self.space = space
        self.screen = screen
        self.layers = layers
        self.width = 40
        self.height = 20
        
        self.boxes_positions = []
        self.boxes = []
        self.multipliers = {}
        
        
    def create_bottom_multiplier_box(self, pos):
        #these are all offsets from the center of the rectangle, and pos is the center
        vertices = [(0, self.height*2),         #bottom left
                    (self.width, self.height*2),   #bottom right
                    (self.width, self.height/2),   #top roght
                    (0, self.height/2)]         #top left

        body = pymunk.Body(body_type= pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly(body, vertices)
        shape.elasticity = 0
        shape.friction = 1
        shape.color = self.calculate_box_color(pos)
        shape.collision_type = 2
        #shape.filter = pymunk.ShapeFilter(group=1)
        self.space.add(body, shape)
        return shape
       
    
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

            
    
        
    def create_bottom_layer(self, pins_pos):
        spacing = 40
        number_of_boxes = self.layers + 2 + 1 #bottom layers formula and two boxes for outside(TO DO)
        
        first_pin_bottom_layer_pos = pins_pos[len(pins_pos) - number_of_boxes + 1]
        
        local_pos = list(first_pin_bottom_layer_pos)
        local_pos[0] -= 40
        
        for i in range(number_of_boxes):
            self.boxes.append(self.create_bottom_multiplier_box(local_pos))
            #IF CHECKING BALL Y POS DOESNT WORK, THEN MAKE FIRST AND LAST BOX LONGER, BUT IT
            #FUCKS WITH COLORS  
            #if i == 0:
            #    local_pos[0] -= 500
            #    create_bottom_multiplier_box(screen, space, local_pos, 500)
            #    local_pos[0] += 500
            #elif i == number_of_boxes - 1:
            #    create_bottom_multiplier_box(screen, space, local_pos, 500)
            self.boxes_positions.append(local_pos.copy())
            local_pos[0] +=  spacing
            