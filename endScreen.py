from pygame import display
from init import *
from mainGame import *
import time
prevGamestate = mainGameClass()
class endScreen():
    def gameState3(self):
        wintxt = str(prevGamestate.getWinner())
        winner = wintxt + " WINS"
        font = pygame.font.Font('Font.ttf', 64)
        text = font.render("GAME OVER", 1, WHITE)
        text2 = font.render(winner, 1, WHITE)
        screen.blit(text, (50, 100))
        screen.blit(text2, (50, 300) )
        pygame.display.update()
        time.sleep(4)
