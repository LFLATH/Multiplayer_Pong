import pygame
from pygame.locals import *
import sys
from random import *
#Starts pygame
pygame.init()
#Creates the display with a width of 640 by 480 pixles
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



#Player1 Class
class Player1(pygame.sprite.Sprite):
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
        if key[pygame.K_DOWN] and self.rect.y  < 480 - 28 : # down key
            self.rect.y += dist # move down
        elif key[pygame.K_UP] and self.rect.y > 0: # up key
            self.rect.y -= dist # move up

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




class Ball(pygame.sprite.Sprite):
    #init
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([6, 6])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image,WHITE, (6 // 2, 6 //2), 6)
        self.rect = self.image.get_rect()
    def reset(self, winner):
        num = randint(0,1)
        if winner == 'l' and num == 0:
            self.rect.x = 320
            self.rect.y = 20
        elif winner == 'l' and num == 1:
            self.rect.x = 320
            self.rect.y = 440

        elif winner == 'r' and num == 0:
            self.rect.x = 320
            self.rect.y = 20

        else:
            self.rect.x = 320
            self.rect.y = 440
       


       















#Init the sprite
P1 = Player1()
P1.rect.x = 20
P1.rect.y = 20
P2 = Player2()
P2.rect.x = 620
P2.rect.y = 20
ball = Ball()
ball.rect.x = 225
ball.rect.y = 20
global ball_path
ball_path = [2,2]
#Create Sprite List
player_sprites_list = pygame.sprite.Group()
player_sprites_list.add(P1)
player_sprites_list.add(P2)
ball_sprite_list = pygame.sprite.Group()
ball_sprite_list.add(ball)
#Program loop
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    #Updates the position of the player
    player_sprites_list.update()
    #Collision Detection
    ball.rect.move_ip(ball_path)
    if ball.rect.x > 640:
        current_winner = 'r'
        ball.reset(current_winner)
    if ball.rect.x < 0:
        current_winner = 'l'
        ball.reset(current_winner)

    if ball.rect.y < 0 or ball.rect.y > 480:
        ball_path[1] = -ball_path[1]
    if P1.rect.colliderect(ball.rect)== 1 or P2.rect.colliderect(ball.rect) == 1:
        ball_path[0] = -ball_path[0]
        


    #Makes the backround black
    screen.fill(BLACK) 
    #Draws our player
    player_sprites_list.draw(screen) 
    ball_sprite_list.draw(screen)
          
    
    
    #Needs to be at the end of the loop so it updates
    pygame.display.update()
    #Ticks the fram forward
    FPS.tick(FramesPerSecond)
    
