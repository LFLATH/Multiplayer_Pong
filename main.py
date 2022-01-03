import pygame
from pygame.locals import *
import sys
#Starts pygame
pygame.init()
#Creates the display with a width of 300 by 300 pixles
screen = pygame.display.set_mode((640,480))
#Defines FPS as our game clock
FramesPerSecond = 60
#Sets the framrate to 60
FPS = pygame.time.Clock()
#Defining our two colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Changes the name our window to Pong
pygame.display.set_caption("Pong")

#Player Class
class Player(pygame.sprite.Sprite):
    #Init
    def __init__(self):
        super().__init__()
        #Creates the player and sets its starting point
        self.image = pygame.Surface([4, 28])
        self.image.fill(WHITE)
        pygame.draw.rect(self.image,WHITE,pygame.Rect(5, 5, 4, 28))
        self.rect = self.image.get_rect()
        self.x = 20
        self.y = 20
    #Movement of the player
    def update(self):
        #Gets the key stroke
        key = pygame.key.get_pressed()
        dist = 2 # distance moved in 1 frame,
        if key[pygame.K_DOWN] and self.rect.y  < 480 - 28 : # down key
            self.rect.y += dist # move down
        elif key[pygame.K_UP] and self.rect.y > 0: # up key
            self.rect.y -= dist # move up

#Init the sprite
P1 = Player()
P1.rect.x = 20
P1.rect.y = 20
#Create Sprite List
player_sprites_list = pygame.sprite.Group()
player_sprites_list.add(P1)
#Program loop
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    #Updates the position of the player
    player_sprites_list.update()
    

    #Makes the backround black
    screen.fill(BLACK) 
    #Draws our player
    player_sprites_list.draw(screen) 
   
          
    
    
    #Needs to be at the end of the loop so it updates
    pygame.display.update()
    #Ticks the fram forward
    FPS.tick(FramesPerSecond)
    
