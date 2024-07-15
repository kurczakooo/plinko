

def collide(arbiter, space, data) -> bool: 
    
    ball_shape, box_shape = arbiter.shapes
    ball_body = ball_shape.body
    box_body = box_shape.body
    
    space.remove(ball_body, ball_shape)
    
    return True

