# import sys.pygame
import pygame

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
def update(rct):
    speedx = 0
    speedy = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT]:
        speedx = 3
    if keystate[pygame.K_LEFT]:
        speedx = -3
    if keystate[pygame.K_UP]:
        speedy = -3
    if keystate[pygame.K_DOWN]:
        speedy = 3
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


size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((100, 0, 0))
ima = 4 * [4 * [0]]
gameActivate = True
number = 1
clock = pygame.time.Clock()
##########################################
while gameActivate:
    # **player**#
    rct = pygame.Rect((50, 350), (10, 10))
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
    trigger2 = pygame.Rect((400, 320), (100, 30))
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
    realblade = pygame.transform.scale(blade, (50, 90)).convert_alpha()
    blade11 = pygame.Rect((500, 350), (10, 90))
    # blade11.x = 500
    # blade11.y = 350
    speed = 0
    ########
    realblade1 = pygame.transform.scale(blade, (50, 40)).convert_alpha()
    blade1 = pygame.Rect((500, 350), (10, 40))
    realblade12 = pygame.transform.scale(blad, (50, 40)).convert_alpha()
    blade12 = pygame.Rect((500, 450), (10, 40))
    speed1 = 0
    #######
    realblade2 = pygame.transform.scale(blad, (50, 90)).convert_alpha()
    blade2 = pygame.Rect((500, 380), (10, 90))
    speed2 = 0
    #############
    realblade3 = pygame.transform.scale(blade, (50, 30))
    blade3 = pygame.Rect((500, 370), (10, 30))
    realblade32 = pygame.transform.scale(blad, (50, 30))
    blade32 = pygame.Rect((500, 440), (10, 30))
    blade32.x = 500
    blade32.y = 440
    speed3 = 0
    #####trapRoom1 closing room
    ghost = pygame.image.load("ghost.gif")
    realghost = pygame.transform.scale(ghost, (40, 40)).convert_alpha()
    ghost1 = realghost.get_rect(center=(280, 11))
    ghost2 = realghost.get_rect(center=(280, 11))
    ghost3 = realghost.get_rect(center=(280, 11))
    ghost4 = realghost.get_rect(center=(280, 11))
    ghost5 = realghost.get_rect(center=(280, 11))
    ghost6 = realghost.get_rect(center=(280, 11))
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
    endingpoints = pygame.Rect((0, 0), (20, 20))

    #####dead notice####
    dead = pygame.image.load("dead.png")
    dead1 = realblade3.get_rect(center=(250, 250))
    while number == 1:
        dx = 0
        dy = 0
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActivate = False
                number = 0

        update(rct)
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
            screen.blit(dead, dead1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (blade1.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (blade12.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (blade2.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (blade3.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (blade32.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (ghost1.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (ghost2.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (ghost3.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (ghost4.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (ghost5.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (ghost6.colliderect(rct)):
            screen.fill((0, 0, 0))
            screen.blit(dead, dead1)
            clock.tick(1)
            pygame.display.update()
            clock.tick(1)
            break;
        if (rct.colliderect(endingpoints)):
            number = 1
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
        pygame.draw.rect(screen, (100, 50, 200), endingpoints)
        screen.blit(realblade, (blade11.x - 20,blade11.y))
        screen.blit(realblade1, (blade1.x - 20, blade1.y))
        screen.blit(realblade12, (blade12.x - 20,blade12.y))
        screen.blit(realblade2, (blade2.x -20,blade2.y))
        screen.blit(realblade3, (blade3.x -20,blade3.y))
        screen.blit(realblade32, (blade32.x -20,blade32.y))
        screen.blit(realghost, ghost1)
        screen.blit(realghost, ghost2)
        screen.blit(realghost, ghost3)
        screen.blit(realghost, ghost4)
        screen.blit(realghost, ghost5)
        screen.blit(realghost, ghost6)

        pygame.draw.rect(screen, (150, 150, 250), rct)

        if (rct.colliderect(endingpoints)):
            number = 1
        clock.tick(50)
        pygame.display.update()
