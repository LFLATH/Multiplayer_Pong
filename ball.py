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
            current_scores[0] += 1

        elif winner == 'l' and num == 1:
            self.rect.x = 340
            self.rect.y = 440
            current_scores[0] += 1


        elif winner == 'r' and num == 0:
            self.rect.x = 300
            self.rect.y = 20
            current_scores[1] += 1


        else:
            self.rect.x = 300
            self.rect.y = 440
            current_scores[1] += 1

        #Wait after every point to reset
         
        font = pygame.font.Font('Font.ttf', 64)
        text1 = font.render(str(current_scores[0]), 1, WHITE)
        text2 = font.render(str(current_scores[1]), 1, WHITE)
        screen.blit(text1, (213, 30))
        screen.blit(text2, (426, 30))
        pygame.display.update()
        time.sleep(2)