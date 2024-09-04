from ball import pygame


class Wallet:
    def __init__(self, screen, balance):
        self.screen = screen
        self.pos = [1200, 10]
        self.balance = balance


    def display_wallet(self):
        font = pygame.font.SysFont("Arial", 30, True, False)
        
        surface = font.render(str(round(self.balance, 2)) + "$", True, (255, 255, 255))

        self.pos = self.calculate_pos()

        self.screen.blit(surface, self.pos)
  
        
    def buy_ball(self, ball_value):
        self.balance -= ball_value
        
    
    def update_balance(self, ball_value, multiplier):
        self.balance += ball_value * multiplier
     
        
    def calculate_pos(self):
        num_of_chars = len(str(round(self.balance, 2))) + 1

        screen_width = self.screen.get_width()
        pos = [screen_width - num_of_chars * 20, 10]
        return pos
    
    

def update_bet_value(balls_worth, input, balance, number_of_balls):
    
    try: 
        new_value = float(input)
        if number_of_balls == 0 and balls_worth != new_value and new_value <= balance and new_value != 0:
            #print(f'bet value changed to: {new_value}')
            return new_value, str(new_value)
        else: return balls_worth, str(balls_worth)
    
    except (ValueError, TypeError):
        return balls_worth, str(balls_worth)