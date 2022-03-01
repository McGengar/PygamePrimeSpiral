import sys
import pygame
from pygame.math import Vector2
from primePy import primes
import math

pygame.init()
clock = pygame.time.Clock()
cell_size = 4
cell_number = 250
screen_width = cell_size*cell_number
screen_height = cell_size*cell_number
screen =pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('primes')


bg_color =pygame.Color('grey12')
light_gray = (50,50,50)
light_gray2 = (60,60,60)
green = (0,200,0)
red = (255,0,0)


class SNAKE:
    def __init__(self):
        self.start= Vector2(125,124)
        self.head = self.start
        self.body = [Vector2(125,124)]
        self.direction = Vector2(1,0)
        self.new_block = False
        self.gag = 0
        self.len = -1
        self.prime = False
        self.maxlen = cell_number**2
    def draw_snake(self):
        for index,block in enumerate(self.body):
            x_pos = block.x*cell_size
            y_pos = block.y*cell_size
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            x = (len(self.body)-index)
            if x==1:
                pygame.draw.rect(screen, green, block_rect)
            else:
                if index <= 10 and x < self.maxlen-10:
                    pygame.draw.rect(screen, red, block_rect)
                else:
                    if primes.check(x) == True and x!=1:
                        pygame.draw.rect(screen, (abs(math.sin(x))*92+50,192-191*x/self.maxlen,164*x/self.maxlen+64), block_rect)
                    else:
                        if x%2 == 1:
                            pygame.draw.rect(screen, light_gray, block_rect)
                        else:
                            pygame.draw.rect(screen, light_gray2, block_rect)
    def move_snake(self):
        if len(self.body) < self.maxlen:
            body_copy = self.body[:]
            if self.gag >= self.len:
                if self.direction == (1, 0):
                    self.direction = (0, 1)
                    self.gag = 1
                    self.len += 1
                else:
                    if self.direction == (0, 1):
                        self.direction = (-1, 0)
                        self.gag = 1
                        self.len += 1
                    else:
                        if self.direction == (-1, 0):
                            self.direction = (0, -1)
                            self.gag = 1
                            self.len += 1
                        else:
                            if self.direction == (0, -1):
                                self.direction = (1, 0)
                                self.gag = 1
                                self.len += 1
            else:
                self.gag +=2
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            #print(f"{self.gag} and {len(self.body)} and {self.direction}")
    def add_block(self):
        self.new_block = True
    def reset(self):
        self.body = [Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)]
        self.direction = Vector2(1, 0)
        self.new_block = False
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
    def draw_elements(self):
        self.snake.draw_snake()
    def check_collision(self):
        if len(self.snake.body)<self.snake.maxlen:
            self.snake.add_block()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 1)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        main_game.update()


    screen.fill(bg_color)
    main_game.draw_elements()
    pygame.display.flip()
    clock.tick(120)