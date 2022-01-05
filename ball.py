import time
from init import *
from random import randint
class Ball(pygame.sprite.Sprite):
    #init
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([6, 6])
        self.image.fill(WHITE)
        #This creates the circle and its hitbox
        pygame.draw.circle(self.image,WHITE, (6 // 2, 6 //2), 6)
        self.rect = self.image.get_rect()
    #This is the code ran after a point is scored
    def reset(self, winner):
        #Generate a random number
        num = randint(0,1)
        #Decision tree depending on random num and winner
        if winner == 'l' and num == 0:
            self.rect.x = 340
            self.rect.y = 20
        elif winner == 'l' and num == 1:
            self.rect.x = 340
            self.rect.y = 440

        elif winner == 'r' and num == 0:
            self.rect.x = 300
            self.rect.y = 20

        else:
            self.rect.x = 300
            self.rect.y = 440
        #Wait after every point to reset
        time.sleep(2)