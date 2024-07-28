from ball import pymunk, pygame
import pygame_gui


class GUImanager:
    def __init__(self, screen, pos, initial_bet_value):
        self.screen = screen
        self.pos = pos
        #self.lower_button = Button([100, 100, 100], self.pos[0], self.pos[1], 50, 30,"-")
        #self.raise_button = Button([100, 100, 100], self.pos[0] + 150, self.pos[1], 50, 30,"+")

        self.bet_value = initial_bet_value
        self.max_bet = 1000
        
    def display(self):
        num_of_chars = len(str(self.bet_value))
        gap = 1
        if num_of_chars == 1:
            gap = 85
        elif num_of_chars == 2:
            gap = 80
        elif num_of_chars == 3:
            gap = 70
        elif num_of_chars == 4:
            gap = 65
        else:
            raise ValueError("Max Bet Amount exceeded")
        
        font = pygame.font.SysFont("Arial", 25, True, False)
        surface = font.render(str(self.bet_value) + "$", True, (255, 255, 255))
        self.screen.blit(surface, [self.pos[0] + gap, self.pos[1]])
        
        self.lower_button.draw(self.screen)
        self.raise_button.draw(self.screen)
        