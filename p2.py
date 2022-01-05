from init import *
class Player2(pygame.sprite.Sprite):
    #Init
    def __init__(self):
        super().__init__()
        #Creates the player and sets its starting point
        self.image = pygame.Surface([4, 28])
        self.image.fill(WHITE)
        pygame.draw.rect(self.image,WHITE,pygame.Rect(5, 5, 4, 28))
        self.rect = self.image.get_rect()
    #Movement of the player
    def update(self):
        #Gets the key stroke
        key = pygame.key.get_pressed()
        dist = 2 # distance moved in 1 frame,
        if key[pygame.K_s] and self.rect.y  < 480 - 28 : # down key
            self.rect.y += dist # move down
        elif key[pygame.K_w] and self.rect.y > 0: # up key
            self.rect.y -= dist # move up

