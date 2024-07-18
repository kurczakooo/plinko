from ball import pymunk
from multiplier_box import MultiplierBox
import pymunk.pygame_util

class MultiplierBoxesLayer :
    
    def __init__(self, space, screen, layers, risk_level):
        self.space = space
        self.screen = screen
        self.layers = layers
        self.risk_level = risk_level
        self.number_of_boxes = self.layers + 2 + 1 #bottom layers formula and two boxes for outside(TO DO)
        
        self.boxes = []
    
        
    def create_bottom_layer(self, pins_pos):
        spacing = 40
        
        first_pin_bottom_layer_pos = pins_pos[len(pins_pos) - self.number_of_boxes + 1]
        
        local_pos = list(first_pin_bottom_layer_pos)
        local_pos[0] -= spacing
        
        for i in range(self.number_of_boxes):
            if i == 0:
                local_pos[0] -= 500
                self.boxes.append(MultiplierBox(self.space, self.screen, self.layers, 40 + 500, 20, local_pos.copy(), i + 2, True))
                local_pos[0] += 500
            elif i == self.number_of_boxes - 1:
                self.boxes.append(MultiplierBox(self.space, self.screen, self.layers, 40 + 500, 20, local_pos.copy(), i, True))
            else:
                self.boxes.append(MultiplierBox(self.space, self.screen, self.layers, 40, 20, local_pos.copy(), i + 1, False))
            
            
            local_pos[0] +=  spacing
            
        self.calculate_multipliers()
            
            
            
    def calculate_multipliers(self):#REMEMBER TO PUT DOUBL OUTER MULTIPLIERS CAUSE OF INVISIBLE BOXES
        if self.layers == 8:
            if self.risk_level == 'low':
                multipliers = [5.6, 5.6, 2.1, 1.1, 1, 0.5, 1, 1.1, 2.1, 5.6, 5.6]
                for value, box in zip(multipliers, self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                multipliers = [13, 13, 3, 1.3, 0.7, 0.4, 0.7, 1.3, 3, 13, 13]
                for value, box in zip(multipliers, self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                multipliers = [29, 29, 4, 1.5, 0.3, 0.2, 0.3, 1.5, 4, 29, 29]
                for value, box in zip(multipliers, self.boxes):
                    box.set_multiplier(value)
            else:
                multipliers = [5.6, 5.6, 2.1, 1.1, 1, 0.5, 1, 1.1, 2.1, 5.6, 5.6]
                for value, box in zip(multipliers, self.boxes):
                    box.set_multiplier(value)

        elif self.layers == 16:
            if self.risk_level == 'low':
                multipliers = [16, 16, 9, 2, 1.4, 1.4, 1.2, 1.1, 1, 0.5, 1, 1.1, 1.2, 1.4, 1.4, 2, 9, 16, 16]
                for value, box in zip(multipliers, self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                multipliers = [110, 110, 41, 10, 5, 3, 1.5, 1, 0.5, 0.3, 0.5, 1, 1.5, 3, 5, 10, 41, 110, 110]
                for value, box in zip(multipliers, self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                multipliers = [1000, 1000, 130, 26, 9, 4, 2, 0.2, 0.2, 0.2, 0.2, 0.2, 2, 4, 9, 26, 130, 1000, 1000]
                for value, box in zip(multipliers, self.boxes):
                    box.set_multiplier(value)
            else:
                multipliers = [16, 16, 9, 2, 1.4, 1.4, 1.2, 1.1, 1, 0.5, 1, 1.1, 1.2, 1.4, 1.4, 2, 9, 16, 16]
                for value, box in zip(multipliers, self.boxes):
                    box.set_multiplier(value)