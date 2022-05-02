from pygame import display
from init import *
import time
class endScreen():
    def __init__(self, winner):
        self.winner = winner
    def gameState3(self):
        wintxt = str(self.winner)
        winner = wintxt + " WINS"
        if wintxt == "Right":
            font = pygame.font.Font('Font.ttf', 56)
        else:
            font = pygame.font.Font('Font.ttf', 64)
        text = font.render("GAME OVER", 1, WHITE)
        text2 = font.render(winner, 1, WHITE)
        screen.blit(text, (50, 100))
        screen.blit(text2, (50, 300) )
        pygame.display.update()
        time.sleep(4)
