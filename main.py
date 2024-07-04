from ball import pygame, pymunk, random, Ball, create_board, create_bottom_layer, display_wallet
from collision_handler import collide
from board import GameBoard
    
"""    
TO DO:
    - make ball not collide woth each other
    - make it so holding space spams balls
    - make layer with mulitipliers
TUTORIAL ON COLLISIONS:
https://www.youtube.com/watch?v=cCiXqK9c18g&t
""" 
import sys 
def main():
    
    money = 1000
    
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
    #pins, pins_pos = create_board(space, layers)
    board = 
    
    boxes = create_bottom_layer(screen, space, layers=layers, pins_pos=pins_pos)
    
    #handlers = [space.add_collision_handler(1, i+2) for i in range(1)]
    #for i, handler in enumerate(handlers):
    #    handler.separate = balls[i].collide

    balls_worth = 10

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and money >= 10:
                balls.append(Ball(12, (640, 50), space))
                money -= balls_worth
                
        for ball in balls:
            if ball.body.position.y > 720:
                balls.remove(ball)
                money += 20 * balls_worth
        
        #print(f'balls: {len(balls)}')
        
        screen.fill((0, 0, 0))
        display_wallet(screen, (100, 100), str(money))

        space.step(1/60.0)
        space.debug_draw(draw_options)
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    
    
if __name__ == '__main__':
    main()