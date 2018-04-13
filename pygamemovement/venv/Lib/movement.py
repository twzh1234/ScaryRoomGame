import pygame
import os
import pygame.mixer
pygame.init()

sound = pygame.mixer.Sound('bgm.wav')

window = pygame.display.set_mode((800,600))
jia = pygame.image.load("image1.png")
jia1 = pygame.transform.scale(jia,(50,50))
pygame.display.set_caption("game")
black = (0,0,0)
white = (255,255,255)

x,y,r = 0,0,0
moveX = 0
moveY = 0

clock = pygame.time.Clock()

gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            sound.play()
            x,y = pygame.mouse.get_pos()
        if (event.type == pygame.KEYDOWN):
            #sound.play()
            if (event.key == pygame.K_ESCAPE) :
                gameLoop = False
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                moveX = -5
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                moveX = 5   
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                moveY = -5
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                moveY = 5
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                moveX = 0
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                moveX = 0
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                moveY = 0
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                moveY = 0


    window.fill((r,0,0))
    if x+moveX <= 800:
        x += moveX

    if y+moveY <= 600:
        y += moveY


    window.blit(jia1,(x,y))
    clock.tick(50)
    pygame.display.flip()
    if (r == 0):
        r1 = 1
    elif (r == 255):
        r1 = -1
    r = r + r1
pygame.quit()