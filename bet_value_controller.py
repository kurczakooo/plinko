from ball import pymunk, pygame

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
            
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


class BetValueController:
    def __init__(self, pos, initial_bet_value):
        self.pos = pos
        self.lower_button = Button([100, 100, 100], self.pos[0], self.pos[1], 100, 70,"-")
        self.raise_button = Button([100, 100, 100], self.pos[0], self.pos[1], 100, 70,"+")
        self.bet_value = initial_bet_value
        
    def display(self):
        font = pygame.font.SysFont("Arial", 40, True, False)
        surface = font.render(str(self.balance) + "$", True, (255, 255, 255))
        self.screen.blit(surface, self.pos)