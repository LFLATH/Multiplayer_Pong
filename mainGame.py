from openingScreen import *
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
        pygame.draw.rect(screen, WHITE, (320,0,5,480))
        pygame.display.update()