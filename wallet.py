from ball import pymunk, pygame


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
    print(f'number of balls on the baord = {number_of_balls}')
    if number_of_balls == 0 and balls_worth != float(input):
        print(f'zmieniam wartosc kulki na {float(input)}')
        return float(input)
    else: return balls_worth
"""   
try:
    value = float(input)
    if value > balance:
        return balls_worth
    else:
        print(f'zmieniam wartosc kulki na {value}')
        return value
except Exception:
    return balls_worth
"""