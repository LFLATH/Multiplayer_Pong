import pygame
from pygame.locals import *
import sys
from random import *
import time
import pygame.freetype
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
#Create and define our font
font = pygame.font.Font('Font.ttf', 36)
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
#Init the sprites
P1 = Player1()
P1.rect.x = 20
P1.rect.y = 20
P2 = Player2()
P2.rect.x = 620
P2.rect.y = 150
ball = Ball()
ball.rect.x = 225
ball.rect.y = 150
#Init the ball's path
ball_path = [2,2]
#Create Sprite List
player_sprites_list = pygame.sprite.Group()
player_sprites_list.add(P1)
player_sprites_list.add(P2)
ball_sprite_list = pygame.sprite.Group()
ball_sprite_list.add(ball)


#Inits the scores
current_scores = [0,0]

#Opening Screen Method
def gameState1():
    #Create Variable to check if the person clicked the play button
    clicked = False
    #Loop for the menu
    while clicked == False:
        #Find the Mouse Position
        mousePOS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Check to see if the person clicked on the button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 240 <= mousePOS[0] <= 240 + 140 and 250 <= mousePOS[1] <= 250 + 40:
                    clicked = True


        screen.fill(BLACK) 
        #Added a function to underline the button if someone hovers over it
        if 240 <= mousePOS[0] <= 240 + 140 and 250 <= mousePOS[1] <= 250 + 40:
            pygame.draw.rect(screen, WHITE, [240, 300, 140, 5])
        #Define our two fonts
        font = pygame.font.Font('Font.ttf', 64)
        font2 = pygame.font.Font('Font.ttf', 32)
        #Render the text for these fonts
        text = font.render("PONG", 1, WHITE)
        text2 = font2.render("PLAY", 1, BLACK)
        #Create a rect for the title
        text_rect = text.get_rect(center = (320, 100))
        #Create the texts and the button
        screen.blit(text, text_rect)
        pygame.draw.rect(screen, WHITE, [240, 250, 140, 40])
        screen.blit(text2,(255,245))

        pygame.display.update()
        
   

#Main Game Screen Method
def gameState2():
    #Program loop
    while True:
        FPS.tick(FramesPerSecond)
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
            current_scores[1] += 1
            ball.reset(current_winner)
        if ball.rect.x < 0:
            current_winner = 'l'
            current_scores[0] += 1
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
        pygame.draw.rect(screen, WHITE, (320,0,5,480))
        pygame.display.update()

            
#run the game states in order
gameState1()
gameState2()
    
