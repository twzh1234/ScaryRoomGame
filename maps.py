import pygame
import random


class Image():
    def __init__(self, red=0, green=0, blue=0):
        self.image = pygame.Surface((500, 500))
        self.image.fill((red, green, blue))
        self.rect = self.image.get_rect()

    def show(self):
        return self.image

    def change(self, red=0, green=0, blue=0):
        self.image.fill((red, green, blue))

    colorful = (255, 255, 255)


def collision(source, player):
    if not source.cooliderect(target):
        return None
    overlap = source.clip(target)
    if overlap.width > overlap.height:
        pass
    else:
        pass


check1 = Image(138, 51, 3)
check2 = Image(138, 51, 36)
check3 = Image(138, 51, 36)
check4 = Image(138, 51, 36)
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((100, 0, 0))
ima = 4 * [4 * [0]]
gameActivate = True
number = 1
clock = pygame.time.Clock()
###all the objects and their property####
# **player**#
rct = pygame.Rect((0, 0), (10, 10))
###wall###
wall1 = pygame.Rect((80, 300), (200, 6))
wall2 = pygame.Rect((0, 400), (360, 6))
wall3 = pygame.Rect((360, 50), (6, 350))
wall = pygame.Rect((80, 0), (6, 300))
obstacles = pygame.Rect((40, 40), (40, 40))
###wall###
###boder###
boderup = pygame.Rect((0, 0), (500, 1))
boderlef = pygame.Rect((0, 0), (1, 500))
boderrig = pygame.Rect((499, 0), (1, 500))
boderdown = pygame.Rect((0, 499), (500, 1))
###boder###
###traps###
speedstone = 0
speedstone2 = 0
speedstone3 = 0
speedstone4 = 0
speedstone5 = 0
speedstoney = 0
speedstoney2 = 0
speedstoney3 = 0
speedstoney4 = 0
speedstoney5 = 0


stone = pygame.Rect((150,1),(20,20))
stone2 = pygame.Rect((200,1),(20,20))
stone3 = pygame.Rect((250,1),(20,20))
stone4 = pygame.Rect((330,1),(20,20))
stone5 = pygame.Rect((130,1),(20,20))
color1 = (0,0,0)
trap6 = pygame.Rect((360,0),(6,50))
trigger2 = pygame.Rect((330,0),(12,50))
color = (100,0,0)
trigger = pygame.Rect((280, 288), (80, 12))
trap5 = pygame.Rect((280, 300), (80, 6))
trap1 = pygame.Rect((0, 90), (10, 10))
trap2 = pygame.Rect((0, 120), (20, 20))
trap3 = pygame.Rect((0, 160), (20, 20))
trap4 = pygame.Rect((0, 200), (20, 20))
dx1 = 1
dx2 = 2
dx3 = 3
dx4 = 4
###traps###
###door###
open = False
close = False
#####
###ending points###
endingpoints = pygame.Rect((50,450),(20,20))
##########################################
while gameActivate:
    while number == 1 :
        dx = 0
        dy = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActivate = False
                number = 0
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RIGHT):
                    dx = 3
                if (event.key == pygame.K_LEFT):
                    dx = -3
                if (event.key == pygame.K_UP):
                    dy = -3
                if (event.key == pygame.K_DOWN):
                    dy = 3

        rct.move_ip(dx, dy)
        screen.fill((100, 0, 0))
        xx = rct.centerx
        yy = rct.centery
        ######## the border
        if (rct.colliderect(obstacles)):
            if (rct.centerx > obstacles.x + 40 and obstacles.y < rct.centery + 5):
                rct.move_ip(3, 0)
            if (rct.centerx < obstacles.x and obstacles.y < rct.centery + 5):
                rct.move_ip(-3, 0)
            if (rct.centery > obstacles.y + 40 and obstacles.x < rct.centerx + 5):
                rct.move_ip(0, 3)
            if (rct.centery < obstacles.y and obstacles.x < rct.centerx + 5):
                rct.move_ip(0, -3)
        if (rct.colliderect(wall)):
            if (rct.centerx > wall.x + 6 and wall.y < rct.centery + 5):
                rct.move_ip(3, 0)
                print("collide")
            if (rct.centerx < wall.x and wall.y < rct.centery + 5):
                print("collide")
                rct.move_ip(-3, 0)
            if (rct.centery > wall.y + 300 and wall.x < rct.centerx + 5):
                print("collide")
                rct.move_ip(0, 3)
        if (rct.colliderect(wall1)):
            if (rct.centery > wall1.y + 6 and wall1.x < rct.centerx + 5):
                rct.move_ip(0, 3)
            if (rct.centery < wall1.y and wall1.x < rct.centerx + 5):
                rct.move_ip(0, -3)
            if (rct.centerx > wall1.x + 200 and wall1.y < rct.centery + 5):
                rct.move_ip(3, 0)
        if (rct.colliderect(wall2)):
            if (rct.centery > wall2.y + 6 and wall2.x < rct.centerx + 5):
                rct.move_ip(0, 3)
            if (rct.centery < wall2.y and wall1.x < rct.centerx + 5):
                rct.move_ip(0, -3)
            if (rct.centerx > wall2.x + 360 and wall2.y < rct.centery + 5):
                rct.move_ip(3, 0)
        if (rct.colliderect(wall3)):
            if (rct.centerx > wall3.x + 6 and wall3.y < rct.centery + 5):
                rct.move_ip(3, 0)
            if (rct.centerx < wall3.x and wall3.y < rct.centery + 5):
                rct.move_ip(-3, 0)
            if (rct.centery > wall3.y + 350 and wall3.x < rct.centerx + 5):
                rct.move_ip(0, 3)
            if (rct.centery < wall3.y and wall3.x < rct.centerx + 5):
                rct.move_ip(0, -3)
        if (rct.colliderect(trigger)):
            close = True
            color = (0, 0, 0)
            speedstone = 4
            speedstone2 = 0
            speedstone3 = 0
            speedstone4 = 0
            speedstone5 = 0
            speedstoney = 1
            speedstoney2 = 0
            speedstoney3 = 0
            speedstoney4 = 0
            speedstoney5 = 0

        if (close):
            if (rct.colliderect(trap5)):
                if (rct.centery > trap5.y + 6 and trap5.x < rct.centerx + 5):
                    rct.move_ip(0, 3)
                if (rct.centery < trap5.y and trap5.x < rct.centerx + 5):
                    rct.move_ip(0, -3)
        if (rct.colliderect(trigger2)):
            open = True
            color1 = (100, 0, 0)
            speedstone = 0
        if (open == False):
            if (rct.colliderect(trap6)):
                if (rct.centerx > trap6.x + 6 and trap6.y < rct.centery + 5):
                    rct.move_ip(3, 0)
                if (rct.centerx < trap6.x and trap6.y < rct.centery + 5):
                    rct.move_ip(-3, 0)
        if (stone.colliderect(wall1)):
            speedstone = -4
        if (stone.colliderect(boderup)):
            speedstone = 4

        if (rct.colliderect(boderup)):
            rct.move_ip(0, 3)
        if (rct.colliderect(boderdown)):
            rct.move_ip(0, -3)
        if (rct.colliderect(boderlef)):
            rct.move_ip(3, 0)
        if (rct.colliderect(boderrig)):
            rct.move_ip(-3, 0)
        if (trap1.colliderect(boderlef)):
            dx1 = 2
        elif (trap1.colliderect(wall)):
            dx1 = -2
        if (trap2.colliderect(boderlef)):
            dx2 = 2
        elif (trap2.colliderect(wall)):
            dx2 = -2
        if (trap3.colliderect(boderlef)):
            dx3 = 3
        elif (trap3.colliderect(wall)):
            dx3 = -3
        if (trap4.colliderect(boderlef)):
            dx4 = 4
        elif (trap4.colliderect(wall)):
            dx4 = -4
        ###################
        trap1.move_ip(dx1, 0)
        trap2.move_ip(dx2, 0)
        trap3.move_ip(dx3, 0)
        trap4.move_ip(dx4, 0)
        # test if the ball collides with trap determine the lose and success.
        if (rct.colliderect(trap1)):
            break
        elif (rct.colliderect(trap2)):
            break
        elif (rct.colliderect(trap3)):
            break
        elif (rct.colliderect(trap4)):
            break
        elif (rct.colliderect(stone)):
            break
        elif (rct.colliderect(stone2)):
            break
        elif (rct.colliderect(stone3)):
            break
        elif (rct.colliderect(stone4)):
            break
        elif (rct.colliderect(stone5)):
            break
        stone.move_ip(0, speedstone)
        stone2.move_ip(0, speedstone)
        stone3.move_ip(0, speedstone)
        stone4.move_ip(0, speedstone)
        stone5.move_ip(0, speedstone)

        pygame.draw.rect(screen, (200, 200, 100), obstacles)
        pygame.draw.rect(screen, (0, 0, 0), wall)
        pygame.draw.rect(screen, (0, 0, 0), wall1)
        pygame.draw.rect(screen, (0, 0, 0), wall2)
        pygame.draw.rect(screen, (0, 0, 0), wall3)
        pygame.draw.rect(screen, (0, 0, 0), boderdown)
        pygame.draw.rect(screen, (0, 0, 0), boderlef)
        pygame.draw.rect(screen, (0, 0, 0), boderrig)
        pygame.draw.rect(screen, (0, 0, 0), boderup)
        pygame.draw.ellipse(screen, (255, 0, 0), trap1)
        pygame.draw.ellipse(screen, (0, 255, 0), trap2)
        pygame.draw.ellipse(screen, (0, 0, 255), trap3)
        pygame.draw.ellipse(screen, (100, 150, 240), trap4)
        pygame.draw.rect(screen, color, trap5)
        pygame.draw.rect(screen, (100, 0, 0), trigger)
        pygame.draw.rect(screen, (0, 100, 0), trigger2)
        pygame.draw.rect(screen, color1, trap6)
        pygame.draw.ellipse(screen, (0, 100, 0), stone)
        pygame.draw.ellipse(screen, (0, 100, 0), stone2)
        pygame.draw.ellipse(screen, (0, 100, 0), stone3)
        pygame.draw.ellipse(screen, (0, 100, 0), stone4)
        pygame.draw.ellipse(screen, (0, 100, 0), stone5)
        pygame.draw.rect(screen, (0, 100, 0), endingpoints)
        pygame.draw.ellipse(screen, (255, 0, 255), rct)
        if(rct.colliderect(endingpoints)):
            number = 2

        # message_to_screen("you lose",colorful)

        pygame.display.update()
        clock.tick(10)
    while number == 2:
        screen.fill((100, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActivate = False
                number = 0
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RIGHT):
                    dx = 3
                if (event.key == pygame.K_LEFT):
                    dx = -3
                if (event.key == pygame.K_UP):
                    dy = -3
                if (event.key == pygame.K_DOWN):
                    dy = 3
        pygame.draw.ellipse(screen,(255,0,255),rct)
        pygame.display.update()



