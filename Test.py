import sys,pygame
pygame.init()
size = 200,200
screen = pygame.display.set_mode(size)
image = pygame.image.load('Geoffrey_Challen.jpg')
background = pygame.image.load('black.PNG')
screen.blit(image, (0, 0))
done = False
positionY = 0
positionX = 0
delta = 50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                positionX = positionX + delta
                screen.blit(background, (0, 0))
                screen.blit(image, (positionX, positionY))
            elif (event.key == pygame.K_RIGHT):
                positionX = positionX - delta
                screen.blit(background, (0, 0))
                screen.blit(image, (positionX, positionY))
                
            elif (event.key == pygame.K_UP):
                positionY = positionY + delta
                screen.blit(background, (0, 0))
                screen.blit(image, (positionX, positionY))
            elif (event.key == pygame.K_DOWN):
                positionY = positionY - delta
                screen.blit(background, (0, 0))
                screen.blit(image, (positionX, positionY))
    pygame.display.flip()

