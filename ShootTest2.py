import pygame
import random
import os
import math

height = 500
width = 500
FPS = 60

# color
white = (255, 255, 255)
black = (0, 0, 0)
darkred = (100, 0 ,0)
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
        bullet = Bullet(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height, 0)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def aoe(self):
        b1 = Bullet(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height, 0,)
        b2 = Bullet(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height, 15  )
        b3 = Bullet(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height, 30)
        b4 = Bullet(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height, 45)
        b5 = Bullet(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height, 315)
        b6 = Bullet(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height, 330)
        b7 = Bullet(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height, 345)
        all_sprites.add(b1,b2,b3,b4,b5,b6,b7)
        bullets.add(b1,b2,b3,b4,b5,b6,b7)
    def attack_pos(self):
        return self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height

class Enemy(pygame.sprite.Sprite):
    # sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"Ghost2.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.y_speed = random.randrange(1,6)

    def update(self):
        self.rect.x += random.randrange(2,6)
        self.rect.y += self.y_speed
        if self.rect.bottom > height - 200:
            self.y_speed = -self.y_speed
        if self.rect.top < 200:
            self.y_speed = -self.y_speed
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
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((10,10))
        #self.image.fill((255,255,0))
        self.angle = angle
        self.image = Bullets
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        radian = self.angle / 180.0 * math.pi
        self.rect.move_ip(math.sin(radian) * -10, \
                          -10 * math.cos(radian))
        if self.rect.x + self.rect.width < 0 or \
                self.rect.x > width or \
                self.rect.y + self.rect.height < 0 or \
                self.rect.y > height:
            self.kill()





# initialize window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("level 3")
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join(img_folder,"back2.png")).convert()
background = pygame.transform.scale(background,(500,500))
background_rect = background.get_rect()
Bullets = pygame.image.load(os.path.join(img_folder, "laserGreen.png")).convert()


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
Enemys = pygame.sprite.Group()
Ghosts = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(10):
    m = Ghost()
    Ghosts.add(m)
    all_sprites.add(m)

for j in range(3):
    k = Enemy()
    Enemys.add(k)
    all_sprites.add(k)
# game loop

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.aoe()
            if event.key == pygame.K_ESCAPE:
                running = False

    all_sprites.update()

    # check collision with ghost
    hits = pygame.sprite.groupcollide(Ghosts,bullets,True,True)
    for hit in hits:
        m = Ghost()
        all_sprites.add(m)
        Ghosts.add(m)
    hits2 = pygame.sprite.groupcollide(Enemys,bullets,True,True)
    for hit in hits2:
        l = Enemy()
        all_sprites.add(l)
        Enemys.add(l)

    #check collision
    #hits1 = pygame.sprite.spritecollide(player,Ghosts,False)
    #if hits1:
        #running = False

    screen.fill(darkred)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()