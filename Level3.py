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

font_name = pygame.font.match_font('arial')
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface,text_rect)


def show_go_screen():
    draw_text(screen, "you dead",64 , width/2, height /4)
    draw_text(screen, "Esc to quit",22,width/2, width/2)
    draw_text(screen,"press a key to restart", 18, width/2,height*3/4)
    pygame.display.flip()
    waiting = True
    clock.tick(1)
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def show_begin_screen():
    draw_text(screen, "ScaryRoom Game!",64 , width/2, height /4)
    draw_text(screen, "You have three lives", 45, width / 2, 200)
    draw_text(screen, "Arrow keys move, Space to fire",22,width/2, width/2 + 80)
    draw_text(screen,"press any key to begin", 18, width/2,height*3/4)
    pygame.display.flip()
    waiting = True
    clock.tick(1)
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def show_youwin_screen():
    draw_text(screen, "Congratulations !", 64, width / 2, height / 4)
    draw_text(screen, "You win the game", 45, width / 2, 200)
    #draw_text(screen, "Arrow keys move, Space to fire", 22, width / 2, width / 2 + 80)
    draw_text(screen, "press any key to restart", 18, width / 2, height * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
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
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self):
        # unhide if hidden
        #if self.hidden and pygame.time.get_ticks() - self.hide_timer > 3000:
            #self.hidden = False
            #self.rect.bottom = height - 10
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
        if keystate[pygame.K_SPACE]:
            self.shoot()
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
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
        bullet = Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (50, 490)
class Enemy(pygame.sprite.Sprite):
    # sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"Ghost2.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.8 / 2)
        self.rect.center = (-20, random.randrange(100,400))
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

score = 0
round(score,2)
message = "        your goal is 10000 points !"

game_not_start = True
game_over =True
# game loop

running = True

while running:
    if game_not_start:
        clock.tick(1)
        show_begin_screen()
        clock.tick(1)

        score = 0
        game_not_start = False

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
        score += 5 + hit.rect.y*0.5
        newGhost()
    hits2 = pygame.sprite.groupcollide(Enemys,bullets,True,True)
    for hitt in hits2:
        score += 5 + hitt.rect.y*0.1
        l = Enemy()
        all_sprites.add(l)
        Enemys.add(l)

    #check collision
    hits1 = pygame.sprite.spritecollide(player,Ghosts,True,pygame.sprite.collide_circle)
    for hit in hits1:
        player.shield -= hit.radius*2
        newGhost()
        if player.shield <= 0:
            player.hide()
            player.lives -= 1
            player.shield = 100

    hits3 = pygame.sprite.spritecollide(player, Enemys, True, pygame.sprite.collide_circle)
    for hit in hits3:
        player.shield -= hit.radius * 2
        newGhost()
        if player.shield <= 0:
            player.hide()
            player.lives -= 1
            player.shield = 100
    if player.lives == 0:
        game_over = True
        clock.tick(1)
        show_go_screen()
        clock.tick(1)
        game_not_start = True

    if score >= 10000:
        clock.tick(1)
        show_youwin_screen()
        clock.tick(1)
        game_not_start = True


    screen.fill(darkred)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_text(screen, "score:     " +  str(round(score,2)) + message, 18, width/2, 10)
    draw_shield_bar(screen,5,5,player.shield)


    pygame.display.flip()

pygame.quit()
