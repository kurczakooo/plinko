from ball import pymunk
from multiplier_box import MultiplierBox
from multipliers import multipliers
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
            
        self.set_multipliers()
            
            
            
    def set_multipliers(self):#REMEMBER TO PUT DOUBL OUTER MULTIPLIERS CAUSE OF INVISIBLE BOXE
        global multipliers
        
        if self.layers == 8:
            if self.risk_level == 'low':
                for value, box in zip(multipliers[8]['low'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                for value, box in zip(multipliers[8]['medium'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                for value, box in zip(multipliers[8]['high'], self.boxes):
                    box.set_multiplier(value)
            else:
                for value, box in zip(multipliers[8]['low'], self.boxes):
                    box.set_multiplier(value) 
                    
        elif self.layers == 9:
            if self.risk_level == 'low':
                for value, box in zip(multipliers[9]['low'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                for value, box in zip(multipliers[9]['medium'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                for value, box in zip(multipliers[9]['high'], self.boxes):
                    box.set_multiplier(value)
            else:
                for value, box in zip(multipliers[9]['low'], self.boxes):
                    box.set_multiplier(value)

        elif self.layers == 10:
            if self.risk_level == 'low':
                for value, box in zip(multipliers[10]['low'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                for value, box in zip(multipliers[10]['medium'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                for value, box in zip(multipliers[10]['high'], self.boxes):
                    box.set_multiplier(value)
            else:
                for value, box in zip(multipliers[10]['low'], self.boxes):
                    box.set_multiplier(value)
                    
        elif self.layers == 11:
            if self.risk_level == 'low':
                for value, box in zip(multipliers[11]['low'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                for value, box in zip(multipliers[11]['medium'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                for value, box in zip(multipliers[11]['high'], self.boxes):
                    box.set_multiplier(value)
            else:
                for value, box in zip(multipliers[11]['low'], self.boxes):
                    box.set_multiplier(value)
                    
        elif self.layers == 12:
            if self.risk_level == 'low':
                for value, box in zip(multipliers[12]['low'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                for value, box in zip(multipliers[12]['medium'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                for value, box in zip(multipliers[12]['high'], self.boxes):
                    box.set_multiplier(value)
            else:
                for value, box in zip(multipliers[12]['low'], self.boxes):
                    box.set_multiplier(value)
                    
        elif self.layers == 13:
            if self.risk_level == 'low':
                for value, box in zip(multipliers[13]['low'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                for value, box in zip(multipliers[13]['medium'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                for value, box in zip(multipliers[13]['high'], self.boxes):
                    box.set_multiplier(value)
            else:
                for value, box in zip(multipliers[13]['low'], self.boxes):
                    box.set_multiplier(value)
                    
        elif self.layers == 14:
            if self.risk_level == 'low':
                for value, box in zip(multipliers[14]['low'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                for value, box in zip(multipliers[14]['medium'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                for value, box in zip(multipliers[14]['high'], self.boxes):
                    box.set_multiplier(value)
            else:
                for value, box in zip(multipliers[14]['low'], self.boxes):
                    box.set_multiplier(value)
                    
        elif self.layers == 15:
            if self.risk_level == 'low':
                for value, box in zip(multipliers[15]['low'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                for value, box in zip(multipliers[15]['medium'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                for value, box in zip(multipliers[15]['high'], self.boxes):
                    box.set_multiplier(value)
            else:
                for value, box in zip(multipliers[15]['low'], self.boxes):
                    box.set_multiplier(value)
                    
        elif self.layers == 16:
            if self.risk_level == 'low':
                for value, box in zip(multipliers[16]['low'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'medium':
                for value, box in zip(multipliers[16]['medium'], self.boxes):
                    box.set_multiplier(value)
            elif self.risk_level == 'high':
                for value, box in zip(multipliers[16]['high'], self.boxes):
                    box.set_multiplier(value)
            else:
                for value, box in zip(multipliers[16]['low'], self.boxes):
                    box.set_multiplier(value)
                    
        else:
            raise ValueError('Wrong number of layers!')