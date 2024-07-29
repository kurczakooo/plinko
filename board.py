from ball import pymunk

class GameBoard:
    def __init__(self, screen,  number_of_layers, space):
        self.screen = screen
        self.radius = 5
        self.layers = number_of_layers
        self.space = space
        self.pins_pos = []
        self.pins = []

    def create_static_circle(self, space, position, radius):
        body = pymunk.Body(body_type = pymunk.Body.STATIC)
        body.position = position
        shape = pymunk.Circle(body, radius)
        shape.elasticity = 0.5
        shape.friction = 0.5
        shape.color = (255, 255, 255, 255)
        self.space.add(body, shape)
        return shape
    
    
    def create_board(self, layers):
        if layers < 8 or layers > 16:
            raise ValueError("Number of layers must be between 8 and 16")
        
        pin_num_per_layer = 3
        initial_pos = [640, 80]
        spacing = 40
        
        for layer in range(layers):
            start_x = initial_pos[0] - (pin_num_per_layer - 1) * (spacing / 2)
            for i in range(pin_num_per_layer):
                pos = (start_x + i * spacing, initial_pos[1])
                self.pins_pos.append(pos)
                self.pins.append(self.create_static_circle(self.space, pos, 5))
            initial_pos[1] += spacing
            pin_num_per_layer += 1
       
