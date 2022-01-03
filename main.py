import pygame
from pygame.locals import *
from random import randint
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
#Game loop

#Player Class
class Player(object):
    #Init
    def __init__(self):
        super().__init__()
        self.rect = pygame.draw.rect(screen, WHITE, (20, 20, 4, 28))
        self.x = 20
        self.y = 20
    #Movement of the player
    def update_position(self):
        #Gets the key stroke
        key = pygame.key.get_pressed()
        dist = 2 # distance moved in 1 frame,
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
    #To display the player
    def draw(self, surface):
        #Draws the player on the screen with color white at the correct points, with a size of 4x28
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 4, 28))
#The Ball Class
class Ball(object):
    #init
    def __init__(self):
        super().__init__()
        self.x = 25
        self.y = 25
        self.rect = pygame.Rect(6, 6, 12, 12)
        generator = randint(0,1)
        last_point_won = 'r'
        if last_point_won == 'r':
            if generator == 1:
                self.x = 225
                self.y = 20
            else:
                self.x = 225
                self.y = 460
        if last_point_won == 'l':
            if generator == 1:
                self.x = 215
                self.y = 20
            else:
                self.x = 215
                self.y = 460
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
#Function to calculate the movement of the ball
    def ball_position(self, collisionP1):
        slopex = 1
        slopey = 1
        if self.x == 640 or self.x == 0:
            self.kill()

        if self.y == 0 or self.y == 480:
            slopey *= -1
        if collisionP1 == True:
            slopex *= -1
        if collisionP1 == False:
            self.x += (4 * slopex)
            self.y += (4 * slopey)

        
        



#Draws the ball on the screen. There an inital list of points to use.
    def draw(self, surface):
        # Draw the ball
        pygame.draw.circle(screen, WHITE, self.rect.center, 6)
#Init the two objects
P1 = Player()
ball = Ball()
#Program loop
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    P1.update_position()
    pointP1 = P1.rect.colliderect()
    if pointP1 == True:
        collision = True
    else:
        collision = False
    ball.ball_position(collision)

    #Makes the backround black
    screen.fill(BLACK) 
    #Draws our player
    P1.draw(screen) 
    ball.draw(screen)
    for i in range(0,480):
     pygame.draw.line(screen, WHITE,(220, i), (220, i + 20))
     i += 20
          
    
    
    #Needs to be at the end of the loop so it updates
    pygame.display.update()
    #Ticks the fram forward
    FPS.tick(FramesPerSecond)
    
