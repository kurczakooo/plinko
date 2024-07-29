from ball import pymunk, pygame
import pygame_gui as gui


class GUImanager:
    def __init__(self, screen, initial_bet_value:str):
        self.screen = screen
        
        self.manager = gui.UIManager((self.screen.width, self.screen.height))
        
        self.bet_input_rect = pygame.Rect(1010, 680, 140, 32)    
        self.bet_input_box = gui.elements.UITextEntryLine(relative_rect=self.bet_input_rect, manager=self.manager, initial_text=initial_bet_value)
        self.bet_submit_button = gui.elements.UIButton(relative_rect=pygame.Rect(1150, 680, 120, 32), text='SET BET VALUE', manager=self.manager)
        
        self.amount_of_layers_buttons = []
        for i in range(8, 17):
            self.amount_of_layers_buttons.append(gui.elements.UIButton(relative_rect=pygame.Rect(1230, 50*(i-7)+50, 50, 50), text=str(i), manager=self.manager))

        self.configure_gui_elements()

    def configure_gui_elements(self):
        self.bet_input_box.allowed_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        self.bet_input_box.blink_cursor_time = 1  
        