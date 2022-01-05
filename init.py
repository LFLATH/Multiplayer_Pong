import pygame

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