import pygame
import random 

pygame.init()
WIDTH=800
HEIGHT=900
screen=pygame.display.set_mode((WIDTH,HEIGHT))
background=pygame.image.load('bg.jpg')
pygame.display.set_caption("Virus")
population=20
disease=2
playerImage=pygame.image.load('pla1.png')
enemyImage=pygame.image.load('pla.png')
    
class player():
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.present=True
        self.frame=12
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
    def draw(self,screen):
        self.move()
        screen.blit(playerImage,(self.x,self.y))


class virus():
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.present=True
        self.frame=12
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
    def draw(self,screen):
        self.move()
        screen.blit(enemyImage,(self.x,self.y))

players=[]
Diseases=[]
running=True
def Update():
    for player in players:
        player.draw(screen)
    for dis in Diseases:
        dis.draw(screen)
    pygame.display.update()

EDGE=32
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if len(Diseases)<disease:
        diseasex=random.randint(EDGE,WIDTH-EDGE)
        diseasey=random.randint(EDGE,HEIGHT-EDGE)
        diseasevx=random.uniform(0.4,0.8)
        diseasevy=random.uniform(0.4,0.8)
        Diseases.append(virus(diseasex,diseasey,diseasevx,diseasevy))
    if len(players)<population:
        playerx=random.randint(EDGE,WIDTH-EDGE)
        playery=random.randint(EDGE,HEIGHT-EDGE)
        playervx=random.uniform(0.4,0.8)
        playervy=random.uniform(0.4,0.8)
        players.append(player(playerx,playery,playervx,playervy))
    for D in Diseases:
        if D.x<EDGE or D.x>WIDTH-EDGE:
            D.vx*=-1
        if D.y<EDGE or D.y>HEIGHT-EDGE:
            D.vy*=-1
    for P in players:
        '''if P.x<0 or P.x>WIDTH or P.y<0 or P.y>HEIGHT:
            players.pop(players.index(P))'''
        if P.x<EDGE or P.x>WIDTH-EDGE:
            P.vx*=-1
        if P.y<EDGE or P.y>HEIGHT-EDGE:
            P.vy*=-1
        for p in players:
            if p!=P:
                if P.x<p.x+p.frame and P.x>p.x-p.frame:
                    P.vx*=-1
                if P.y<p.y+p.frame and P.y>p.y-p.frame:
                    P.vy*=-1
    Update()