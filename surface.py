import pygame
import random

pygame.init()
running =True
WIDTH=1400
HEIGHT=1000
red = (255,0,0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (50, 150, 50)
PURPLE = (130, 0, 130)
GREY = (230, 230, 230)
HORRIBLE_YELLOW = (190, 175, 50)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
stats = pygame.Surface((WIDTH // 4, HEIGHT // 4))
stats.fill(WHITE)
stats.set_alpha(230)
stats_pos = (WIDTH // 40, HEIGHT // 40)
stats_height = stats.get_height()
stats_width = stats.get_width()
i=0
j=0
T=200
for time in range(T):
    i+=1
    j=i**2+2
    stats_graph = pygame.PixelArray(stats)
    stats_graph[int(i/T)*stats_width,:int(j/T)*stats_height]=pygame.Color('aquamarine1')

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            break
    del stats_graph
    stats.unlock()
    screen.blit(stats, stats_pos)
    pygame.display.update()
