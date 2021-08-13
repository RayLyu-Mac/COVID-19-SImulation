import pygame
import random
from os import path

#initialize
pygame.init()
screen=pygame.display.set_mode((800,600))
running=True

#Background
background=pygame.image.load('bg.jpg')

#title and icon
pygame.display.set_caption("Space Invader")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#player
playerImage=pygame.image.load('pla.png')
playerx=0
playery=500
playerxChange=5
def player(playerx,playery):
    screen.blit(playerImage,(playerx,playery))

#enemy
enemyImage=pygame.image.load('ufo.png')
enemyx=random.randint(0,800)
enemyy=random.randint(50,150)
enemyxchange=3
enemyychange=-5

#bullet
bulletImage=pygame.image.load('bullet.png')
bulletY=500
bulletX=0
bulletYchange=20
bullet_state='ready'


def enemy(x,y):
    screen.blit(enemyImage,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImage,(x+16,y+10))
    
    
#Game Loop
while running:
    screen.fill((255,0,0))
    screen.blit(background,(0,0))
    player(playerx,playery)
    enemy(enemyx,enemyy)
    enemyx+=enemyxchange
    playerx+=playerxChange
    #checking the boundaries
    if playerx<=0:
        playerx=0
    elif playerx>=740:
        playerx=740 

    if enemyx<=0:
        enemyx=0
        enemyxchange*=-1
        enemyy+=enemyychange
    elif enemyx>=740:
        enemyx=740 
        enemyxchange*=-1
        enemyy-=enemyychange
    #bullet movement 
    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletYchange
    if bulletY<=0:
        bulletY=480
        bullet_state='ready'

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #if keystroke is pressed check whether its right or left
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerxChange=-5
            if event.key==pygame.K_RIGHT:
                playerxChange=5
            if event.key==pygame.K_SPACE:
                #after push the space, it will check if there is a bullet already
                if bullet_state is "ready":
                    bulletX=playerx
                    fire_bullet(bulletX,bulletY)
                    
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerxChange=0

        
    pygame.display.update()

#RGB

