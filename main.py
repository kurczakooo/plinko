from ball import pygame, pymunk, Ball
from collision_handler import collide
from board import GameBoard
from multiplier_boxes import MultiplierBoxes
from wallet import Wallet
import sys 

"""    
TO DO:
    - make it so holding space spams balls
    - make layer with mulitipliers
        - figure out calculate multipliers function, needd boxes pos, and find proportions be
        tween neighbouring boxes multipliers, i need to differ the boxes with a value signed to
        each other
TUTORIAL ON COLLISIONS:
https://www.youtube.com/watch?v=cCiXqK9c18g&t
""" 

def main():
    
    layers = int(sys.argv[1])

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('PLINKO')
    clock = pygame.time.Clock()
    running = True

    space = pymunk.Space()
    space.gravity = (0, 900)

    draw_options = pymunk.pygame_util.DrawOptions(screen)
    #draw_options.shape_outline_color = draw_options.collision_point_color
    #draw_options.shape_kinematic_color = (0, 255, 0, 255)
  
    balls = []

    board = GameBoard(screen, layers, space)
    board.create_board()
    
    boxes = MultiplierBoxes(space, screen, layers)
    boxes.create_bottom_layer(board.pins_pos)
    
    #handlers = [space.add_collision_handler(1, i+2) for i in range(1)]
    #for i, handler in enumerate(handlers):
    #    handler.separate = balls[i].collide

    wallet = Wallet(screen, (50, 50), 1000)

    balls_worth = 10

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and wallet.balance >= balls_worth:
                balls.append(Ball(12, (640, 50), space))
                wallet.buy_ball(balls_worth)
                
        for ball in balls:
            if ball.body.position.y > 720:
                balls.remove(ball)
                wallet.update_balance(balls_worth, 20)
        
        #print(f'balls: {len(balls)}')
        
        screen.fill((0, 0, 0))
        space.debug_draw(draw_options)
        wallet.display_wallet()
        
        
        pygame.display.flip()
        space.step(1/60.0)
        clock.tick(60)
        
    pygame.quit()
    boxes.calculate_multipliers()
    print(boxes.multipliers)
    
if __name__ == '__main__':
    main()