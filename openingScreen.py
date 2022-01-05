from p1 import *
from p2 import *
from ball import *
import sys
from init import *
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