# import sys.pygame
import pygame


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
    rct = pygame.Rect((0, 0), (10, 10))
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

    #####trapRoom1 corridor
    trigger1 = pygame.Rect((400, 350), (6, 150))
    trap = pygame.Rect((500, 350), (6, 130))
    speed = 0
    trap1 = pygame.Rect((500, 350), (6, 80))
    trap12 = pygame.Rect((500, 450), (6, 50))
    speed1 = 0
    trap2 = pygame.Rect((500, 380), (6, 120))
    speed2 = 0
    trap3 = pygame.Rect((500, 370), (6, 50))
    trap32 = pygame.Rect((500, 440), (6, 60))
    speed3 = 0
    #####trapRoom1 closing room
    ball1 = pygame.Rect((270, 1), (20, 20))
    ball2 = pygame.Rect((270, 1), (20, 20))
    ball3 = pygame.Rect((270, 1), (20, 20))
    ball4 = pygame.Rect((270, 1), (20, 20))
    ball5 = pygame.Rect((270, 1), (20, 20))
    ball6 = pygame.Rect((270, 1), (20, 20))
    x1, y1 = 3, 3
    x2, y2 = -2, 7
    x3, y3 = -4, 3
    x4, y4 = -3, 6
    x5, y5 = 3, -9
    x6, y6 = 3, -3
    ###ending points###
    endingpoints = pygame.Rect((0, 0), (20, 20))
    while number == 1:
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
        trap.move_ip(speed, 0)
        trap1.move_ip(speed1, 0)
        trap12.move_ip(speed1, 0)
        trap2.move_ip(speed2, 0)
        trap3.move_ip(speed3, 0)
        trap32.move_ip(speed3, 0)
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
            ball1.move_ip(x1, y1)
            ball2.move_ip(x2, y2)
            ball3.move_ip(x3, y3)
            ball4.move_ip(x4, y4)
            ball5.move_ip(x5, y5)
            ball6.move_ip(x6, y6)

        if (rct.colliderect(trigger3)):
            color2 = (100, 0, 0)
            open = True
        if (open is not True):
            stop(rct, door1)

        if (ball1.colliderect(wall3)):
            x1 = 4
        if (ball1.colliderect(boderup)):
            y1 = 7
        if (ball1.colliderect(door2)):
            x1 = 4
        if (ball1.colliderect(boderrig)):
            x1 = -6
        if (ball1.colliderect(wall1)):
            y1 = -3
        if (ball1.colliderect(door1)):
            y1 = -3

        if (ball2.colliderect(wall3)):
            x2 = 4
        if (ball2.colliderect(boderup)):
            y2 = 7
        if (ball2.colliderect(door2)):
            x2 = 4
        if (ball2.colliderect(boderrig)):
            x2 = -6
        if (ball2.colliderect(wall1)):
            y2 = -3
        if (ball2.colliderect(door1)):
            y2 = -3

        if (ball3.colliderect(wall3)):
            x3 = 5
        if (ball3.colliderect(boderup)):
            y3 = 2
        if (ball3.colliderect(door2)):
            x3 = 8
        if (ball3.colliderect(boderrig)):
            x3 = -1
        if (ball3.colliderect(wall1)):
            y3 = -7
        if (ball3.colliderect(door1)):
            y3 = -3

        if (ball4.colliderect(wall3)):
            x4 = 5
        if (ball4.colliderect(boderup)):
            y4 = 2
        if (ball4.colliderect(door2)):
            x4 = 8
        if (ball4.colliderect(boderrig)):
            x4 = -1
        if (ball4.colliderect(wall1)):
            y4 = -7
        if (ball4.colliderect(door1)):
            y4 = -3

        if (ball5.colliderect(wall3)):
            x5 = 5
        if (ball5.colliderect(boderup)):
            y5 = 2
        if (ball5.colliderect(door2)):
            x5 = 8
        if (ball5.colliderect(boderrig)):
            x5 = -1
        if (ball5.colliderect(wall1)):
            y5 = -7
        if (ball5.colliderect(door1)):
            y5 = -3

        if (ball6.colliderect(wall3)):
            x6 = 5
        if (ball6.colliderect(boderup)):
            y6 = 2
        if (ball6.colliderect(door2)):
            x6 = 8
        if (ball6.colliderect(boderrig)):
            x6 = -1
        if (ball6.colliderect(wall1)):
            y6 = -7
        if (ball6.colliderect(door1)):
            y6 = -3

        if (trap.colliderect(trigger1)):
            speed1 = -3
        if (trap1.colliderect(trigger1)):
            speed2 = -3
        if (trap2.colliderect(trigger1)):
            speed3 = -3
        if (trap.colliderect(wall2)):
            speed = 0
        if (trap1.colliderect(wall2)):
            speed1 = 0
        if (trap2.colliderect(wall2)):
            speed2 = 0
        if (trap3.colliderect(wall2)):
            speed3 = 0

        if (trap.colliderect(rct)):
            break;
        if (trap1.colliderect(rct)):
            break;
        if (trap12.colliderect(rct)):
            break;
        if (trap2.colliderect(rct)):
            break;
        if (trap3.colliderect(rct)):
            break;
        if (trap32.colliderect(rct)):
            break;
        # if (ball1.colliderect(rct)):
        #     break;
        # if (ball2.colliderect(rct)):
        #     break;
        # if (ball3.colliderect(rct)):
        #     break;
        # if (ball4.colliderect(rct)):
        #     break;
        # if (ball5.colliderect(rct)):
        #     break;
        # if (ball6.colliderect(rct)):
        #     break;
        if (rct.colliderect(endingpoints)):
            number = 1

        pygame.draw.rect(screen, (0, 0, 0), wall1)
        pygame.draw.rect(screen, (0, 0, 0), wall2)
        pygame.draw.rect(screen, (0, 0, 0), wall3)
        pygame.draw.rect(screen, (0, 0, 0), boderlef)
        pygame.draw.rect(screen, (0, 0, 0), boderrig)
        pygame.draw.rect(screen, (0, 0, 0), boderdown)
        pygame.draw.rect(screen, (0, 0, 0), boderup)
        pygame.draw.rect(screen, color, door)
        pygame.draw.rect(screen, (100, 0, 0), trigger)
        pygame.draw.rect(screen, color1, door1)
        pygame.draw.rect(screen, (100, 0, 0), trigger2)
        pygame.draw.rect(screen, color2, door2)
        pygame.draw.rect(screen, (100, 100, 100), trigger3)
        pygame.draw.rect(screen, (0, 0, 0), trap)
        pygame.draw.rect(screen, (0, 0, 0), trap1)
        pygame.draw.rect(screen, (0, 0, 0), trap12)
        pygame.draw.rect(screen, (0, 0, 0), trap2)
        pygame.draw.rect(screen, (0, 0, 0), trap32)
        pygame.draw.rect(screen, (0, 0, 0), trap3)
        pygame.draw.ellipse(screen, (0, 0, 0), ball1)
        pygame.draw.ellipse(screen, (0, 0, 0), ball2)
        pygame.draw.ellipse(screen, (0, 0, 0), ball3)
        pygame.draw.ellipse(screen, (0, 0, 0), ball4)
        pygame.draw.ellipse(screen, (0, 0, 0), ball5)
        pygame.draw.ellipse(screen, (0, 0, 0), ball6)
        pygame.draw.rect(screen, (100, 50, 200), endingpoints)

        pygame.draw.rect(screen, (150, 150, 250), rct)

        if (rct.colliderect(endingpoints)):
            number = 1

        # message_to_screen("you lose",colorful)

        pygame.display.update()
    # while number == 2:
    #     screen.fill((100, 0, 0))
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             gameActivate = False
    #             number = 0
    #         if event.type == pygame.KEYDOWN:
    #             if (event.key == pygame.K_RIGHT):
    #                 dx = 3
    #             if (event.key == pygame.K_LEFT):
    #                 dx = -3
    #             if (event.key == pygame.K_UP):
    #                 dy = -3
    #             if (event.key == pygame.K_DOWN):
    #                 dy = 3
    #     pygame.draw.ellipse(screen, (255, 0, 255), rct)
    #     pygame.display.update()
    #
    #     ball = pygame.image.load("ball.bmp").convert_Alpha
    #     ballrect = ball.get_rect((200,200))

