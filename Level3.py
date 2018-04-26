import pygame
import random
import os

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


def newGhost():
    m = Ghost()
    all_sprites.add(m)
    Ghosts.add(m)

def draw_shield_bar(surface,x,y,pect):
    if pect < 0:
        pect = 0
    BAR_Length = 100
    BAR_Height = 10
    fill = (pect/100)*BAR_Length
    outline_rect = pygame.Rect(x,y,BAR_Length,BAR_Height)
    fill_rect = pygame.Rect(x,y,fill,BAR_Height)
    pygame.draw.rect(surface,red,fill_rect)
    pygame.draw.rect(surface,white,outline_rect,2)
# player
class Player(pygame.sprite.Sprite):
    # sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,15))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.radius = 7
        #pygame.draw.circle(self.image,red,self.rect.center,self.radius)
        self.rect.centerx = 50
        self.rect.bottom = height - 10
        self.speedx = 0
        self.speedy = 0
        self.shield = 100

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
        self.image_orig = pygame.image.load(os.path.join(img_folder,"Ghost2.png")).convert()
        self.image_orig.set_colorkey(black)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width* 0.8/2)
        #pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(3,8)
        self.speedx = random.randrange(-3,3)
        self.rot = 0
        self.rot_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed)%360

            new_image = pygame.transform.rotate(self.image_orig,self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((10,10))
        #self.image.fill((255,255,0))
        self.image = Bullets
        self.image.set_colorkey(black)
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
    newGhost()

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
                player.shoot()
            if event.key == pygame.K_ESCAPE:
                running = False

    all_sprites.update()

    # check collision with ghost
    hits = pygame.sprite.groupcollide(Ghosts,bullets,True,True)
    for hit in hits:
        newGhost()
    hits2 = pygame.sprite.groupcollide(Enemys,bullets,True,True)
    for hitt in hits2:
        l = Enemy()
        all_sprites.add(l)
        Enemys.add(l)

    #check collision
    hits1 = pygame.sprite.spritecollide(player,Ghosts,True,pygame.sprite.collide_circle)
    for hit in hits1:
        player.shield -= hit.radius*2
        newGhost()
        if player.shield <= 0:
            running = False

    screen.fill(darkred)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_shield_bar(screen,5,5,player.shield)


    pygame.display.flip()

pygame.quit()
