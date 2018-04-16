import pygame
import random
import os

height = 500
width = 500
FPS = 60

# color
white = (255, 255, 255)
black = (0, 0, 0)
darkred = (188, 0 ,0)
red = (255,0,0)


# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"image")

# player
class Player(pygame.sprite.Sprite):
    # sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,15))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = height - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Enemy(pygame.sprite.Sprite):
    # sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"Ghost2.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.y_speed = 6

    def update(self):
        self.rect.x += 6
        self.rect.y += self.y_speed
        if self.rect.bottom > height - 200:
            self.y_speed = -6
        if self.rect.top < 200:
            self.y_speed = 8
        if self.rect.left > width:
            self.rect.right = 0

# initialize window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("level 3")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy()
all_sprites.add(player)
all_sprites.add(enemy)
# game loop

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(darkred)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
