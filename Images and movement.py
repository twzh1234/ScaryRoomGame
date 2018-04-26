import pygame
import random
pygame.init()
GREEN = (20, 255, 140)
red  = (255,  0,  0)
height = 800
width = 800
screen = pygame.display.set_mode((800, 800))
zombie = pygame.image.load('Geoffrey_Challen.jpg')
zombie = pygame.transform.scale(zombie, (50, 50))


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = zombie

        self.rect = self.image.get_rect()

        self.rect.topleft = [x, y]

    def changespeed(self, x, y):
        self.change_x += x

        self.change_y += y

    def update(self):
        self.rect.move_ip(0,self.change_y)

        self.rect.move_ip(self.change_x,0)
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0


all_things_list = pygame.sprite.RenderPlain()

player = Player(0, 0)

all_things_list.add(player)

done = False

clock = pygame.time.Clock()

while done is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)



            if event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)



            if event.key == pygame.K_UP:
                player.changespeed(0, -3)



            if event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)

            if event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)

            if event.key == pygame.K_UP:
                player.changespeed(0, 3)

            if event.key == pygame.K_DOWN:
                player.changespeed(0, -3)



    screen.fill(GREEN)

    player.update()
    all_things_list.draw((screen))

    clock.tick(50)

    pygame.display.flip()
