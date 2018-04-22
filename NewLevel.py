import pygame
import random
import math
pygame.init()
GREEN = (20, 255, 140)
red  = (255,  0,  0)
height = 800
width = 800
screen = pygame.display.set_mode((800, 800))
zombie = pygame.image.load('Geoffrey_Challen.jpg')
zombie = pygame.transform.scale(zombie, (50, 50))


class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = zombie
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self, time_passed_seconds=0.0):
        self.move_curve(time_passed_seconds)

    def move_line(self, time_passed_seconds):
        self.rect.move_ip(10, 20 * time_passed_seconds)

    def move_circle(self, time_passed_seconds):
        if not hasattr(self, 'angle'):
            self.angle = 180
        else:
            self.angle = self.angle + time_passed_seconds * 360
        if not hasattr(self, 'radius'):
            self.radius = 60
        if not hasattr(self, 'center'):
            x = self.rect.x + self.radius if self.rect.x < self.radius else self.rect.x - self.radius
            self.center = [x, 0 + self.radius]
        self.center[1] += 2
        new_pos = self.__circle_next(self.center, self.radius, self.angle)
        # self.rect.move_ip(new_pos[0], new_pos[1])
        self.rect.x, self.rect.y = new_pos[0], new_pos[1]

    def __circle_next(self, center, radius, angle):
        x = math.sin(angle / 180.0 * math.pi) * radius + center[0]
        y = math.cos(angle / 180.0 * math.pi) * radius + center[1]
        return x, y

    def move_curve(self, time_passed_seconds):
        if not hasattr(self, 'ray'):
            self.ray = self.rect.x
        if not hasattr(self, 'angle'):
            self.angle = 0
        else:
            self.angle = self.angle + time_passed_seconds * 360
        if not hasattr(self, 'curve_width'):
            self.curve_width = 50
        x = math.sin(self.angle / 180 * math.pi) * self.curve_width + self.ray
        y = self.rect.y + 10 * time_passed_seconds
        self.rect.x, self.rect.y = x, y





all_things_list = pygame.sprite.RenderPlain()

player = Boss(400, 400)

all_things_list.add(player)

done = False

clock = pygame.time.Clock()

while done is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.

    screen.fill(GREEN)



    all_things_list.draw((screen))
    player.update(time_passed_seconds)
    clock.tick(50)

    pygame.display.flip()
