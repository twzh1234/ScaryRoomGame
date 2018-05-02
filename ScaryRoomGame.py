# import sys.pygame
import pygame
import random
import os


# dead_sound = pygame.mixer.Sound("dead.mp3")

def stop1(rct, obstacles):
    xx, yy = obstacles.size
    if (rct.colliderect(obstacles)):
        if (rct.centerx > obstacles.x + xx and obstacles.y < rct.centery + 5):
            rct.move_ip(3, 0)
        if (rct.centerx < obstacles.x and obstacles.y < rct.centery + 5):
            rct.move_ip(-3, 0)
        if (rct.centery > obstacles.y + yy and obstacles.x < rct.centerx + 5):
            rct.move_ip(0, 3)
        if (rct.centery < obstacles.y and obstacles.x < rct.centerx + 5):
            rct.move_ip(0, -3)


def stop(rct, obstacles):
    xx, yy = obstacles.size
    if (rct.colliderect(obstacles)):
        if (rct.centerx > obstacles.x + xx and obstacles.y < rct.centery + 5):
            rct.move_ip(3, 0)
        if (rct.centerx < obstacles.x and obstacles.y < rct.centery + 5):
            rct.move_ip(-3, 0)
        if (rct.centery > obstacles.y + yy and obstacles.x < rct.centerx + 5):
            rct.move_ip(0, 3)
        if (rct.centery < obstacles.y and obstacles.x < rct.centerx + 5):
            rct.move_ip(0, -3)


def bouncing(rct, a, b, c, d, e, f, x, y):
    if (rct.colliderect(wall3)):
        x = a
    if (rct.colliderect(boderup)):
        y = b
    if (rct.colliderect(door2)):
        x = c
    if (rct.colliderect(boderrig)):
        x = d
    if (rct.colliderect(wall1)):
        y = e
    if (rct.colliderect(door1)):
        y = f
    return x, y


font_name = pygame.font.match_font('arial')


def draw_text(surface, text, size, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((100, 0, 0))
ima = 4 * [4 * [0]]
gameActivate = True
number = 0
clock = pygame.time.Clock()
left1 = pygame.image.load("left1.png")
realleft1 = pygame.transform.scale(left1, (10, 20)).convert_alpha()
left2 = pygame.image.load("left2.png")
realleft2 = pygame.transform.scale(left2, (10, 20)).convert_alpha()
left3 = pygame.image.load("left3.png")
realleft3 = pygame.transform.scale(left3, (10, 20)).convert_alpha()
right1 = pygame.image.load("right1.png")
realright1 = pygame.transform.scale(right1, (10, 20)).convert_alpha()
right2 = pygame.image.load("right2.png")
realright2 = pygame.transform.scale(right2, (10, 20)).convert_alpha()
right3 = pygame.image.load("right3.png")
realright3 = pygame.transform.scale(right3, (10, 20)).convert_alpha()
back = pygame.image.load("back.png")
realback = pygame.transform.scale(back, (10, 20)).convert_alpha()
front = pygame.image.load("front.png")
realfront = pygame.transform.scale(front, (15, 20)).convert_alpha()
a = 1

game_not_start = True
game_over = True
FPS = 60
# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "image")
# color
white = (255, 255, 255)
black = (0, 0, 0)
darkred = (100, 0, 0)
red = (255, 0, 0)


def newGhost():
    m = Ghost()
    all_sprites.add(m)
    Ghosts.add(m)


def show_go_screen():
    draw_text(screen, "you die", 64, width / 2, height / 4)
    # draw_text(screen, "Esc to quit", 22, width / 2, width / 2)
    draw_text(screen, "press a key to restart", 18, width / 2, height * 3 / 4)
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


def show_begin_screen():
    draw_text(screen, "ScaryRoom Game!", 64, width / 2, height / 4)
    draw_text(screen, "You have three lives", 45, width / 2, 200)
    draw_text(screen, "Arrow keys move, Space to fire", 22, width / 2, width / 2 + 80)
    draw_text(screen, "press any key to begin", 18, width / 2, height * 3 / 4)

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


def draw_shield_bar(surface, x, y, pect):
    if pect < 0:
        pect = 0
    BAR_Length = 100
    BAR_Height = 10
    fill = (pect / 100) * BAR_Length
    outline_rect = pygame.Rect(x, y, BAR_Length, BAR_Height)
    fill_rect = pygame.Rect(x, y, fill, BAR_Height)
    pygame.draw.rect(surface, red, fill_rect)
    pygame.draw.rect(surface, white, outline_rect, 2)


class Player(pygame.sprite.Sprite):
    # sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((15,15))
        # self.image.fill((0,255,0))
        play = pygame.image.load(os.path.join(img_folder, "car.png")).convert()
        self.image = pygame.transform.scale(play, (20, 40))

        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.radius = 2
        # pygame.draw.circle(self.image,red,self.rect.center,self.radius)
        self.rect.centerx = 50
        self.rect.bottom = height - 10
        self.speedx = 0
        self.speedy = 0
        self.shield = 100
        self.shoot_delay = 500
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self):
        # unhide if hidden
        # if self.hidden and pygame.time.get_ticks() - self.hide_timer > 3000:
        # self.hidden = False
        # self.rect.bottom = height - 10
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
        bullet = Bullet(self.rect.centerx, self.rect.top)
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
        self.image = pygame.image.load(os.path.join(img_folder, "Ghost2.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.8 / 2)
        self.rect.center = (-20, random.randrange(20, 470))
        self.y_speed = random.randrange(1, 6)

    def update(self):
        self.rect.x += random.randrange(2, 6)
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
        self.image_orig = pygame.image.load(os.path.join(img_folder, "Ghost2.png")).convert()
        self.image_orig.set_colorkey(black)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.8 / 2)
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(7, 10)
        self.speedx = random.randrange(-5, 5)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360

            new_image = pygame.transform.rotate(self.image_orig, self.rot)
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
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((10,10))
        # self.image.fill((255,255,0))
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


def show_youwin_screen():
    draw_text(screen, "Congratulations !", 64, width / 2, height / 4)
    draw_text(screen, "You survive", 45, width / 2, 200)
    # draw_text(screen, "Arrow keys move, Space to fire", 22, width / 2, width / 2 + 80)
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


##########################################
while gameActivate:

    title = pygame.image.load("scarygame.png")
    title = pygame.transform.scale(title, (450, 350))
    carry = title.get_rect(center=(250, 250))
    presskey = pygame.image.load("presskey.png")
    presskey = pygame.transform.scale(presskey, (450, 100))
    carry1 = presskey.get_rect(center=(250, 400))
    background = pygame.image.load("background.jpg")
    carry2 = background.get_rect(center=(250, 250))
    a = 0;
    while number == 0:
        screen.blit(background, carry2)
        screen.blit(title, carry)
        if (a % 2 == 0):
            screen.blit(presskey, carry1)
        a += 1
        pygame.display.update()
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.K_ESCAPE:
                gameActivate = False
                number = 5
                break
            if event.type == pygame.KEYUP:
                number = 1

    car = pygame.image.load("car.png")
    realcar = pygame.transform.scale(car, (40, 80)).convert_alpha()
    carrier = realcar.get_rect(center=(250, 250))
    floor = pygame.image.load("floor.jpg").convert_alpha()
    background = pygame.transform.scale(floor, (500, 500))
    background_rect = background.get_rect()
    rct = pygame.Rect((250, 50), (10, 20))
    screen.blit(realleft2, rct)
    while number == 1:
        carrier.move_ip(0, -1)
        screen.blit(floor, background_rect)
        screen.blit(realcar, carrier)
        screen.blit(realleft2, rct)
        clock.tick(50)
        pygame.display.update()
        if (carrier.colliderect(rct)):
            number = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                number = 5
                gameActivate = False
                break

    # clock.tick(1)

    # **player**#
    rct = pygame.Rect((50, 350), (10, 20))
    ###wall###
    wall1 = pygame.Rect((0, 350), (400, 6))
    wall2 = pygame.Rect((80, 350), (6, 80))
    wall3 = pygame.Rect((250, 0), (6, 300))

    ###wall###
    ###boder###
    boderup = pygame.Rect((0, 0), (500, 1))
    boderlef = pygame.Rect((0, 0), (1, 500))
    boderrig = pygame.Rect((499, 0), (1, 500))
    boderdown = pygame.Rect((0, 499), (500, 1))
    ###boder###

    ###door###
    door = pygame.Rect((80, 430), (6, 70))
    trigger = pygame.Rect((100, 430), (6, 70))
    color = (100, 0, 0)
    close = False
    door1 = pygame.Rect((400, 350), (100, 6))
    trigger2 = pygame.Rect((400, 310), (100, 30))
    color1 = (100, 0, 0)
    close1 = False
    door2 = pygame.Rect((250, 300), (6, 50))
    trigger3 = pygame.Rect((260, 300), (30, 50))
    color2 = (0, 0, 0)
    open = False

    blade = pygame.image.load("blade1.png")
    blad = pygame.image.load("blade.png")
    #####trapRoom1 corridor
    trigger1 = pygame.Rect((400, 350), (6, 150))
    realblade = pygame.transform.scale(blade, (50, 120)).convert_alpha()
    blade11 = pygame.Rect((500, 350), (10, 120))
    # blade11.x = 500
    # blade11.y = 350
    speed = 0
    ########
    realblade1 = pygame.transform.scale(blade, (50, 50)).convert_alpha()
    blade1 = pygame.Rect((500, 350), (10, 50))
    realblade12 = pygame.transform.scale(blad, (50, 80)).convert_alpha()
    blade12 = pygame.Rect((500, 450), (10, 80))
    speed1 = 0
    #######
    realblade2 = pygame.transform.scale(blad, (50, 120)).convert_alpha()
    blade2 = pygame.Rect((500, 380), (10, 130))
    speed2 = 0
    #############
    realblade3 = pygame.transform.scale(blade, (50, 20))
    blade3 = pygame.Rect((500, 370), (10, 20))
    realblade32 = pygame.transform.scale(blad, (50, 70))
    blade32 = pygame.Rect((500, 440), (10, 70))
    blade32.x = 500
    blade32.y = 440
    speed3 = 0
    #####trapRoom1 closing room
    ghost = pygame.image.load("ghost.gif")
    realghost = pygame.transform.scale(ghost, (40, 40)).convert_alpha()
    ghost1 = pygame.Rect((265, -4), (20, 30))
    ghost2 = pygame.Rect((265, -4), (20, 30))
    ghost3 = pygame.Rect((265, -4), (20, 30))
    ghost4 = pygame.Rect((265, -4), (20, 30))
    ghost5 = pygame.Rect((265, -4), (20, 30))
    ghost6 = pygame.Rect((265, -4), (20, 30))
    x1, y1 = 3, 3
    x2, y2 = -2, 7
    x3, y3 = -4, 3
    x4, y4 = -3, 6
    x5, y5 = 3, -9
    x6, y6 = 3, -3
    ########floor########
    floor = pygame.image.load("floor.jpg").convert_alpha()
    floor1 = floor.get_rect(center=(250, 250))
    ###ending points###
    endingpoints = pygame.Rect((50, 50), (40, 80))
    car = pygame.image.load("car.png")
    realcar = pygame.transform.scale(car, (40, 80)).convert_alpha()

    #####dead notice####
    dead = pygame.image.load("dead.png")
    dead1 = realblade3.get_rect(center=(250, 250))
    ###############
    speedx = 0
    #########text#######
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    myfon = pygame.font.SysFont('Comic Sans MS', 30)
    subtitle = True
    subtitle1 = True
    count = 0

    waiting = True
    while number == 2:
        while (subtitle):
            screen.fill((0, 0, 0))
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    number = 5
                    gameActivate = False
                    subtitle = False
                    subtitle1 = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if count >= 2:
                        subtitle = False
                        break
                    if event.key == pygame.K_2:
                        count += 1
            screen.blit(background, background_rect)
            pygame.draw.rect(screen, (0, 0, 0), wall1)
            pygame.draw.rect(screen, (0, 0, 0), wall2)
            pygame.draw.rect(screen, (0, 0, 0), wall3)
            pygame.draw.rect(screen, (0, 0, 0), boderlef)
            pygame.draw.rect(screen, (0, 0, 0), boderrig)
            pygame.draw.rect(screen, (0, 0, 0), boderdown)
            pygame.draw.rect(screen, (0, 0, 0), boderup)
            if (count == 0):
                textsurface = myfont.render('oh,the stupid car hits me,what is this place(press 2 to continue)', True,
                                            (0, 0, 0))
                screen.blit(textsurface, (40, 450))
            if (count == 1):
                textsurface = myfont.render('my leg is bleeding, my gosh(prees 2 to continue)', True, (0, 0, 0))
                screen.blit(textsurface, (40, 450))
            if (count == 2):
                textsurface = myfont.render('oh it is raining, the house is a good place to stay(press 2)', True,
                                            (0, 0, 0))
                screen.blit(textsurface, (40, 450))
            pygame.display.update()
        if (subtitle1 is False):
            continue

        temp = 0
        speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            a += 1
            if (a >= 3):
                a = 0
            temp = 3
        elif keystate[pygame.K_LEFT]:
            a += 1
            if (a >= 6):
                a = 3
            temp = -3
        if temp == 0:
            if (speedx > 0):
                a = 1
            elif (speedx < 0):
                a = 4
        speedx = temp
        if keystate[pygame.K_UP]:
            speedy = -3
            a = 6
        if keystate[pygame.K_DOWN]:
            speedy = 3
            a = 7
        rct.x += speedx
        rct.y += speedy
        if rct.right > 500:
            rct.right = width
        if rct.left < 0:
            rct.left = 0
        if rct.bottom > 500:
            rct.bottom = 500
        if rct.top < 0:
            rct.top = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                number = 5
                gameActivate = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    number = 5
                    gameActivate = False
                    break

        # update(rct)
        blade11.move_ip(speed, 0)
        blade1.move_ip(speed1, 0)
        blade12.move_ip(speed1, 0)
        blade2.move_ip(speed2, 0)
        blade3.move_ip(speed3, 0)
        blade32.move_ip(speed3, 0)
        screen.fill((100, 0, 0))
        xx = rct.centerx
        yy = rct.centery
        ######## the border
        stop(rct, wall1)
        stop(rct, wall2)
        stop(rct, wall3)
        stop(rct, boderlef)
        stop(rct, boderrig)
        stop(rct, boderdown)
        stop(rct, boderup)
        if (rct.colliderect(trigger)):
            close = True
        if (close):
            stop(rct, door)
            color = (0, 0, 0)
            speed = -3
        if (rct.colliderect(trigger2)):
            close1 = True
        if (close1):
            stop(rct, door1)
            color1 = (0, 0, 0)
            ghost1.move_ip(x1, y1)
            ghost2.move_ip(x2, y2)
            ghost3.move_ip(x3, y3)
            ghost4.move_ip(x4, y4)
            ghost5.move_ip(x5, y5)
            ghost6.move_ip(x6, y6)

        if (rct.colliderect(trigger3)):
            color2 = (100, 0, 0)
            open = True
        if (open is not True):
            stop(rct, door2)
        x1, y1 = bouncing(ghost1, 4, 7, 4, -6, -3, -3, x1, y1)
        x2, y2 = bouncing(ghost2, 4, 7, 4, -6, -3, -3, x2, y2)
        x3, y3 = bouncing(ghost3, 5, 2, 8, -1, -7, -3, x3, y3)
        x4, y4 = bouncing(ghost4, 5, 1, 2, -1, -4, -6, x4, y4)
        x5, y5 = bouncing(ghost5, 2, 3, 1, -2, -3, -6, x5, y5)
        x6, y6 = bouncing(ghost6, 4, 3, 5, -2, -1, -5, x6, y6)

        if (blade11.colliderect(trigger1)):
            speed1 = -3
        if (blade1.colliderect(trigger1)):
            speed2 = -3
        if (blade2.colliderect(trigger1)):
            speed3 = -3
        if (blade11.colliderect(wall2)):
            speed = 0
        if (blade1.colliderect(wall2)):
            speed1 = 0
        if (blade2.colliderect(wall2)):
            speed2 = 0
        if (blade3.colliderect(wall2)):
            speed3 = 0

        if (blade11.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (blade1.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (blade12.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (blade2.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (blade3.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (blade32.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (ghost1.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (ghost2.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (ghost3.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (ghost4.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (ghost5.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (ghost6.colliderect(rct)):
            screen.fill((0, 0, 0))
            textsurface = myfon.render("you die", True, (250, 250, 250))
            screen.blit(textsurface, (80, 150))
            textsurface1 = myfon.render("press any keys to restart", True, (250, 250, 250))
            screen.blit(textsurface1, (30, 200))
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        number = 5
                        gameActivate = False
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            break;
        if (gameActivate is False):
            continue
        if (rct.colliderect(endingpoints)):
            number = 3
        pygame.draw.rect(screen, (150, 150, 150), trigger)
        pygame.draw.rect(screen, (100, 0, 0), trigger2)
        pygame.draw.rect(screen, (100, 100, 100), trigger3)
        screen.blit(floor, floor1)
        pygame.draw.rect(screen, (0, 0, 0), wall1)
        pygame.draw.rect(screen, (0, 0, 0), wall2)
        pygame.draw.rect(screen, (0, 0, 0), wall3)
        pygame.draw.rect(screen, (0, 0, 0), boderlef)
        pygame.draw.rect(screen, (0, 0, 0), boderrig)
        pygame.draw.rect(screen, (0, 0, 0), boderdown)
        pygame.draw.rect(screen, (0, 0, 0), boderup)
        pygame.draw.rect(screen, color, door)
        pygame.draw.rect(screen, color1, door1)
        pygame.draw.rect(screen, color2, door2)
        screen.blit(realcar, endingpoints)
        screen.blit(realblade, (blade11.x - 20, blade11.y))
        screen.blit(realblade1, (blade1.x - 20, blade1.y))
        screen.blit(realblade12, (blade12.x - 20, blade12.y))
        screen.blit(realblade2, (blade2.x - 20, blade2.y))
        screen.blit(realblade3, (blade3.x - 20, blade3.y))
        screen.blit(realblade32, (blade32.x - 20, blade32.y))
        screen.blit(realghost, (ghost1.x - 10, ghost1.y))
        screen.blit(realghost, (ghost2.x - 10, ghost2.y))
        screen.blit(realghost, (ghost3.x - 10, ghost3.y))
        screen.blit(realghost, (ghost4.x - 10, ghost4.y))
        screen.blit(realghost, (ghost5.x - 10, ghost5.y))
        screen.blit(realghost, (ghost6.x - 10, ghost6.y))
        if (a == 0):
            screen.blit(realright1, (rct.x + 5, rct.y))
        if (a == 1):
            screen.blit(realright2, (rct.x + 5, rct.y))
        if (a == 2):
            screen.blit(realright3, (rct.x + 5, rct.y))
        if (a == 3):
            screen.blit(realleft1, (rct.x + 5, rct.y))
        if (a == 4):
            screen.blit(realleft2, (rct.x + 5, rct.y))
        if (a == 5):
            screen.blit(realleft3, (rct.x + 5, rct.y))
        if (a == 6):
            screen.blit(realback, (rct.x + 5, rct.y))
        if (a == 7):
            screen.blit(realfront, (rct.x + 5, rct.y))
        if (rct.colliderect(endingpoints)):
            number = 3
        clock.tick(50)
        pygame.display.update()

    # initialize window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))

    background = pygame.image.load(os.path.join(img_folder, "back2.png")).convert()
    background = pygame.transform.scale(background, (500, 500))
    background_rect = background.get_rect()
    Bullets = pygame.image.load(os.path.join(img_folder, "laserGreen.png")).convert()
    clock.tick(1)
    score = 0
    round(score, 2)
    message = "        your goal is 9000 points !"
    subtitle = True
    count = 0
    subtitle1 = True
    while number == 3:
        while (subtitle):
            screen.fill((0, 0, 0))
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    number = 5
                    gameActivate = False
                    subtitle = False
                    subtitle1 = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if count >=2 :
                        subtitle = False
                        break
                    if event.key == pygame.K_2:
                        count += 1
            screen.blit(background, background_rect)
            screen.blit(realcar, (background_rect.x + 200, background_rect.y + 200))
            if (count == 0):
                draw_text(screen, "this evil still keep chasimg me my gosh!!!(press 2 to cotinue)", 20, 250, 450)
            if (count == 1):
                draw_text(screen, "how to get rid of them", 20, 250, 450)
            if (count == 2):
                draw_text(screen, "i found a gun in the car!!!(press space to shoot and press 1 to contunue)", 15, 250,
                          450)

            pygame.display.update()
        if (subtitle1 is False):
            continue
        if game_not_start:
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
                number = 5
                gameActivate = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                if event.key == pygame.K_ESCAPE:
                    number = 5
                    gameActivate = False
                    break

        all_sprites.update()

        # check collision with ghost
        hits = pygame.sprite.groupcollide(Ghosts, bullets, True, True)
        for hit in hits:
            score += 5 + hit.rect.y * 0.5
            newGhost()
        hits2 = pygame.sprite.groupcollide(Enemys, bullets, True, True)
        for hitt in hits2:
            score += 5 + hitt.rect.y * 0.1
            l = Enemy()
            all_sprites.add(l)
            Enemys.add(l)

        # check collision
        hits1 = pygame.sprite.spritecollide(player, Ghosts, True, pygame.sprite.collide_circle)
        for hit in hits1:
            player.shield -= hit.radius * 2
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

        if score >= 9050:
            clock.tick(1)
            show_youwin_screen()
            number = 0
            clock.tick(1)
            game_not_start = True

        screen.fill(darkred)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_text(screen, "score:     " + str(round(score, 2)) + message, 18, width / 2, 10)
        pygame.display.flip()

    car = pygame.image.load("car.png")
    realcar = pygame.transform.scale(car, (40, 80)).convert_alpha()
    carrier = realcar.get_rect(center=(250, 60))
    floor = pygame.image.load("floor.jpg").convert_alpha()
    background = pygame.transform.scale(floor, (500, 500))
    background_rect = background.get_rect()
    rct = pygame.Rect((250, 50), (10, 20))
    rct1 = pygame.Rect((400, 50), (10, 20))
    count = 0
    activate = True
