from ball import pymunk, pygame


class Wallet:
    def __init__(self, screen, pos, balance):
        self.screen = screen
        self.pos = pos
        self.balance = balance

    def display_wallet(self):
        font = pygame.font.SysFont("Times New Roman", 40, True, False)
        
        surface = font.render(str(self.balance), True, (255, 255, 255))

        self.screen.blit(surface, self.pos)
        
    def buy_ball(self, bals_worth):
        self.balance -= bals_worth