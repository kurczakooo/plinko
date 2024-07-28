from ball import pygame, pymunk, Ball
from board import GameBoard
from boundaries import Boundaries
from multiplier_boxes import MultiplierBoxesLayer
from wallet import Wallet, update_bet_value
from win_history_display import WinHistoryDisplay
from gui_manager import GUImanager

import sys 
import betting_data_analisys.betting_data_analisys as bda
import pygame_gui as gui

"""    
TO DO:
    - give player ability to change number of layers in game
        -
    - fix the fucking game so that not every player becomes a milionare
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

boundaries = Boundaries(space)

risk = ['low', 'medium', 'high']

boxes = MultiplierBoxesLayer(space, screen, layers, risk[2])
boxes.create_bottom_layer(board.pins_pos)

win_history = WinHistoryDisplay(space, screen, 300, 500)

#ball_value_controller = BetValueController(screen, [1055, 600], 1000)
wallet = Wallet(screen, 100) #SET STARTING CASH  
balls_worth = wallet.balance/10

balls = []

def collide(arbiter, space, data) -> bool: 
    
    ball_shape, box_shape = arbiter.shapes
    ball_body = ball_shape.body
    box_body = box_shape.body
    
    space.remove(ball_body, ball_shape)
    balls.remove(ball_shape)
    
    for box in boxes.boxes:
        if box.shape.collision_type == box_shape.collision_type:
            #print(box.multiplier, end=" ")
            hist[box.multiplier] += 1
            wallet.update_balance(ball_value=balls_worth, multiplier=box.multiplier)
    
    return True



gui_manager = GUImanager(screen, str(wallet.balance/10))


hist = {}
for box in boxes.boxes:
    hist[box.multiplier] = 0

def main():

    global balls_worth
    
    #vars for holding space spawning balls
    last_ball_time = 0
    ball_interval = 2 #200   
    
    for i in range(boxes.number_of_boxes):
        handler = space.add_collision_handler(1, i + 2) 
        handler.begin = collide

    time_delta = clock.tick(30) / 1000.0

    running = True
    while running:
        current_time = pygame.time.get_ticks()
    

        if len(balls) != 0: gui_manager.bet_submit_button.disable()
        else: gui_manager.bet_submit_button.enable()
    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == gui.UI_BUTTON_PRESSED:
                if event.ui_element == gui_manager.bet_submit_button:
                    balls_worth, display_text = update_bet_value(balls_worth, gui_manager.bet_input_box.get_text(), wallet.balance, len(balls))
                    gui_manager.bet_input_box.set_text(display_text)
                    
            gui_manager.manager.process_events(event)

        gui_manager.manager.update(time_delta)
############################################################################################
        #holding space        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and wallet.balance >= balls_worth:
            if current_time - last_ball_time >= ball_interval:
                balls.append(Ball(12, (640, 50), space).shape)
                wallet.buy_ball(balls_worth)   
                last_ball_time = current_time         
               
                
        #for ball in balls:
        #    if ball.body.position.y > 500:
        #        balls.remove(ball)

        
        screen.fill((0, 0, 0))
        space.debug_draw(draw_options)
        wallet.display_wallet()
        gui_manager.manager.draw_ui(screen)#########################################################
        #win_history.display()
        for box in boxes.boxes:
            box.display_multiplier()
        
        
        pygame.display.flip()
        space.step(1/60.0)
        clock.tick(60)
        
    pygame.quit()
    #bda.put_hist_in_csv(hist)
    #bda.generate_hist()
    
if __name__ == '__main__':
    main()