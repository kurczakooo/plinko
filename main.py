from ball import pygame, pymunk, Ball
from board import GameBoard
from multiplier_boxes import MultiplierBoxesLayer
from wallet import Wallet
from win_history_display import WinHistoryDisplay
from bet_value_controller import BetValueController
import sys 

"""    
TO DO:
    - figure out calculate multipliers function, needd boxes pos, and find proportions be
    tween neighbouring boxes multipliers, i need to differ the boxes with a value signed to
    each other
    - give player ability to change number of layers in game
    - make a display and button for controlling balls worth
TUTORIAL ON COLLISIONS:
https://www.youtube.com/watch?v=cCiXqK9c18g&t
15.40
""" 

layers = int(sys.argv[1])

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('PLINKO')
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 900)

draw_options = pymunk.pygame_util.DrawOptions(screen)
#draw_options.shape_outline_color = draw_options.collision_point_color
#draw_options.shape_kinematic_color = (0, 255, 0, 255)

board = GameBoard(screen, layers, space)
board.create_board()

boxes = MultiplierBoxesLayer(space, screen, layers)
boxes.create_bottom_layer(board.pins_pos)

win_history = WinHistoryDisplay(space, screen, 300, 500)

ball_value_controller = BetValueController(screen, [1055, 675], 1000)



def collide(arbiter, space, data) -> bool: 
    
    ball_shape, box_shape = arbiter.shapes
    ball_body = ball_shape.body
    box_body = box_shape.body
    
    space.remove(ball_body, ball_shape)
    
    for box in boxes.boxes:
        if box.shape.collision_type == box_shape.collision_type:
            print(box.multiplier, end=" ")
    
    return True





def main():
  
    balls = []
    balls_worth = 10
    
    #vars for holding space spawning balls
    last_ball_time = 0
    ball_interval = 200
    
    wallet = Wallet(screen, 1000)
    
    for i in range(boxes.number_of_boxes):
        handler = space.add_collision_handler(1, i + 2) 
        handler.begin = collide


    running = True
    while running:
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         
        #holding space        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and wallet.balance >= balls_worth:
            if current_time - last_ball_time >= ball_interval:
                balls.append(Ball(12, (640, 50), space))
                wallet.buy_ball(balls_worth)   
                last_ball_time = current_time         
               
                
        for ball in balls:
            if ball.body.position.y > 720:
                balls.remove(ball)

        
        screen.fill((0, 0, 0))
        space.debug_draw(draw_options)
        wallet.display_wallet()
        win_history.display()
        ball_value_controller.display()
        for box in boxes.boxes:
            box.display_multiplier()
        
        
        pygame.display.flip()
        space.step(1/60.0)
        clock.tick(60)
        
    pygame.quit()
    
if __name__ == '__main__':
    main()