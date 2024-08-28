from ball import pymunk, pygame
import datetime as dt

class WinHistoryDisplay:
    def __init__(self, space, screen, width, height):
        self.space = space
        self.screen = screen
        self.width = width
        self.height = height
        self.color = pygame.Color(50, 50, 50)
        
        self.win_history_entries = []
        
        
    def update(self, balls_worth, multiplier, win_amount):
        time = dt.datetime.ctime()
        
        entry = [time, balls_worth, multiplier, win_amount]
        
        self.win_history_entries.append(entry)
        
        
    def display(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(0, 0, self.width, self.height))