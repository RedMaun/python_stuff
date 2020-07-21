import pygame
import random as rand
import time

#define
FPS = 75
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)
GREEN = (124, 252, 0)
FOOD_EXIST = 0
x = 1
y = 0

def reqt_coor(a):
    b = []
    for i in range(0, a.size_y):
        for g in range(0, a.size_x):
            b.append([a.x+g, a.y+i])
    return b

class AbstractObject:
    def __init__(self, x = None, y = None, size_x = None, size_y = None):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

class Snake(AbstractObject):
    def __init__(self):
        super().__init__(x = 0, y = 0, size_x = 20, size_y = 20)
    
    def cross(self, food):
        a = reqt_coor(Snake())
        b = reqt_coor(food)
        for i in range(0, 640):
            for g in range(0, len(a)):
                for h in range(0, len(b)):
                    if a[g][0] == b[h][0] == i: 
                        if a[g][1] == b[h][1]:
                            return True
                        else:
                            continue
        return False


class Food(AbstractObject):
    def __init__(self):
        super().__init__(size_x = 10, size_y = 10)

#initialisating
pygame.init()
sc = pygame.display.set_mode((640, 560), pygame.RESIZABLE)
clock = pygame.time.Clock()
snake = Snake()
food = Food()

def draw_snake(object, x, y):
    pygame.draw.rect(sc, BLACK, (object.x, object.y, object.size_x, object.size_y))
    pygame.draw.rect(sc, ORANGE, (object.x + x, object.y + y, object.size_x, object.size_y))
    object.x += x
    object.y += y
    pygame.display.update()
    
def draw_food(object):
    rand_x = rand.randint(10, 610)
    rand_y = rand.randint(10, 530)
    object.x = rand_x
    object.y = rand_y
    pygame.draw.rect(sc, GREEN, (object.x, object.y, object.size_x, object.size_y))
    pygame.display.update()
    global FOOD_EXIST
    FOOD_EXIST = 1

while True:
    clock.tick(FPS)

    draw_snake(snake, x, y)
    if FOOD_EXIST == 0:
        draw_food(food)

    print(snake.cross(food))
    time.sleep(5)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = -1
        y = 0
    elif keys[pygame.K_RIGHT]:
        x = 1
        y = 0
    elif keys[pygame.K_UP]:
        y = -1
        x = 0
    elif keys[pygame.K_DOWN]:
        y = 1
        x = 0