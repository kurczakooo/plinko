from ball import pymunk
from multiplier_box import MultiplierBox
import pymunk.pygame_util

class MultiplierBoxesLayer :
    
    def __init__(self, space, screen, layers):
        self.space = space
        self.screen = screen
        self.layers = layers
        self.number_of_boxes = self.layers + 2 + 1 #bottom layers formula and two boxes for outside(TO DO)
        
        self.boxes = []
    
        
    def create_bottom_layer(self, pins_pos):
        spacing = 40
        
        first_pin_bottom_layer_pos = pins_pos[len(pins_pos) - self.number_of_boxes + 1]
        
        local_pos = list(first_pin_bottom_layer_pos)
        local_pos[0] -= spacing
        
        for i in range(self.number_of_boxes):
            self.boxes.append(MultiplierBox(self.space, self.screen, self.layers, 40, 20, local_pos.copy(), i + 2))
            #IF CHECKING BALL Y POS DOESNT WORK, THEN MAKE FIRST AND LAST BOX LONGER, BUT IT
            #FUCKS WITH COLORS  
            #if i == 0:
            #    local_pos[0] -= 500
            #    create_bottom_multiplier_box(screen, space, local_pos, 500)
            #    local_pos[0] += 500
            #elif i == number_of_boxes - 1:
            #    create_bottom_multiplier_box(screen, space, local_pos, 500)
            local_pos[0] +=  spacing
            