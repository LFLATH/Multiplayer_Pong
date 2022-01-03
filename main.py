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
class Player(object):
    #Init
    def __init__(self):
        super().__init__()
        #Creates the player and sets its starting point
        self.rect = pygame.draw.rect(screen, WHITE, (20, 20, 4, 28))
        self.x = 20
        self.y = 20
    #Movement of the player
    def update_position(self):
        #Gets the key stroke
        key = pygame.key.get_pressed()
        dist = 2 # distance moved in 1 frame,
        if key[pygame.K_DOWN] and self.y  < 480 - 28 : # down key
            self.y += dist # move down
        elif key[pygame.K_UP] and self.y > 0: # up key
            self.y -= dist # move up
        
    #To display the player
    def draw(self, surface):
        #Draws the player on the screen with color white at the correct points, with a size of 4x28
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 4, 28))

        
        



#Init the  object
P1 = Player()
#Program loop
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    #Updates the position of the player
    P1.update_position()
    

    #Makes the backround black
    screen.fill(BLACK) 
    #Draws our player
    P1.draw(screen) 
   
          
    
    
    #Needs to be at the end of the loop so it updates
    pygame.display.update()
    #Ticks the fram forward
    FPS.tick(FramesPerSecond)
    
