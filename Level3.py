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
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

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
            self.y_speed = 6
        if self.rect.left > width:
            self.rect.right = 0



class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"Ghost2.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(3,8)
        self.speedx = random.randrange(-3,3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100,40)
            self.speedy = random.randrange(3,8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()




# initialize window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("level 3")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
enemy = Enemy()
all_sprites.add(player)
all_sprites.add(enemy)

Ghosts = pygame.sprite.Group()
Ghost.add(enemy)
for i in range(8):
    m = Ghost()
    Ghosts.add(m)
    all_sprites.add(m)
# game loop

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            if event.key == pygame.K_ESCAPE:
                running = False

    all_sprites.update()

    # check collision with ghost
    hits = pygame.sprite.groupcollide(Ghosts,bullets,True,True)
    for hit in hits:
        m = Ghost()
        all_sprites.add(m)
        Ghosts.add(m)
    #check collision
    #hits1 = pygame.sprite.spritecollide(player,Ghosts,False)
    #if hits1:
        #running = False

    screen.fill(darkred)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
