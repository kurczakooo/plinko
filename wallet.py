from ball import pymunk, pygame


class Wallet:
    def __init__(self, screen, balance):
        self.screen = screen
        self.pos = [1200, 10]
        self.balance = balance


    def display_wallet(self):
        font = pygame.font.SysFont("Arial", 30, True, False)
        
        surface = font.render(str(self.balance) + "$", True, (255, 255, 255))

        self.pos = self.calculate_pos()

        self.screen.blit(surface, self.pos)
  
        
    def buy_ball(self, ball_value):
        self.balance -= ball_value
        
    
    def update_balance(self, ball_value, multiplier):
        self.balance += ball_value * multiplier
     
        
    def calculate_pos(self):
        num_of_chars = len(str(self.balance)) + 1

        screen_width = self.screen.get_width()
        pos = [screen_width - num_of_chars * 20, 10]
        return pos