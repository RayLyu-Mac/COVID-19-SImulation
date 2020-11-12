import pygame
import random 
import time
RE=False
red = (255,0,0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (50, 150, 50)
PURPLE = (130, 0, 130)
GREY = (230, 230, 230)
HORRIBLE_YELLOW = (190, 175, 50)


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()
def message(text,a,b,Font_size,screen):
    largeText = pygame.font.Font('freesansbold.ttf',Font_size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (a,b)
    screen.blit(TextSurf, TextRect)

    
# Chance Function 
def chance (kind, probabilitys):
    #input check 
    if kind != len(probabilitys):
        return('check the input!')
    elif sum(probabilitys) !=1:
        return('The probablity is not correct')
    
    Type=[]
    for j in range(kind):
        Type.append(chr(97+j))
    base=40
    sets=[]
    k=0
    for i in probabilitys:
        times=int(i*base)
        for _ in range (times):
            sets.append(Type[k])
        k=k+1
    choice=sets[random.randint(0,base)-1]
    return (choice)

WIDTH=1400
HEIGHT=1000
Ready=False
click=False
side=40
def intro_memu():
    R=True
    pygame.init()
    global population
    global disease
    global T
    global Start_population
    global Start_infection
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Start Menu")
    global Ready
    while R:
        click=False
        screen.fill((255,255,255))

        mouse_x,mouse_y=pygame.mouse.get_pos()

        message('Simulation of COVID-19',WIDTH/2,HEIGHT/2-120,70,screen)
        message('By:Ray Lyu',WIDTH-side,HEIGHT-side/2-20,10,screen)
        message('Press Space to Start',WIDTH/2,HEIGHT/2+40,40,screen)

        Button_1=pygame.Rect(WIDTH/2-420,HEIGHT/2+110,200,50)
        Button_2=pygame.Rect(WIDTH/2-100,HEIGHT/2+110,200,50)
        Button_3=pygame.Rect(WIDTH/2+220,HEIGHT/2+110,200,50)
        message('Small Population',WIDTH/2-330,HEIGHT/2+180,20,screen)
        message('Medium Population',WIDTH/2-10,HEIGHT/2+180,20,screen)
        message('Large Population',WIDTH/2+330,HEIGHT/2+180,20,screen)

        if Button_1.collidepoint((mouse_x,mouse_y)):
            population=30
            Start_population=30
            pygame.draw.rect(screen,(200,200,200),Button_1)
        else:
            pygame.draw.rect(screen,(55,255,55),Button_1)
    

        if Button_2.collidepoint((mouse_x,mouse_y)):
            population=40
            Start_population=40
            pygame.draw.rect(screen,(200,200,200),Button_2)
        else:
            pygame.draw.rect(screen,(55,205,55),Button_2)
            

        
        if Button_3.collidepoint((mouse_x,mouse_y)):
            population=75
            Start_population=75
            pygame.draw.rect(screen,(200,200,200),Button_3)
        else:
            pygame.draw.rect(screen,(55,155,55),Button_3)



        Button_4=pygame.Rect(WIDTH/2-420,HEIGHT/2+230,200,50)
        Button_5=pygame.Rect(WIDTH/2-100,HEIGHT/2+230,200,50)
        Button_6=pygame.Rect(WIDTH/2+220,HEIGHT/2+230,200,50)
        message('Disease=2',WIDTH/2-330,HEIGHT/2+300,20,screen)
        message('Disease=3',WIDTH/2-10,HEIGHT/2+300,20,screen)
        message('Disease=4',WIDTH/2+330,HEIGHT/2+300,20,screen)

        if Button_4.collidepoint((mouse_x,mouse_y)):
            disease=2
            Start_infection=2
            pygame.draw.rect(screen,(200,200,200),Button_4)
        else:
            pygame.draw.rect(screen,(255,55,55),Button_4)
        if Button_5.collidepoint((mouse_x,mouse_y)):
            disease=3
            Start_infection=3
            pygame.draw.rect(screen,(200,200,200),Button_5)
        else:
            pygame.draw.rect(screen,(205,55,55),Button_5)
        if Button_6.collidepoint((mouse_x,mouse_y)):
            disease=4
            Start_infection=4
            pygame.draw.rect(screen,(200,200,200),Button_6)
        else:
            pygame.draw.rect(screen,(155,55,55),Button_6)

    

        Button_7=pygame.Rect(WIDTH/2-420,HEIGHT/2+345,200,50)
        Button_8=pygame.Rect(WIDTH/2-100,HEIGHT/2+345,200,50)
        Button_9=pygame.Rect(WIDTH/2+220,HEIGHT/2+345,200,50)
        message('Time=1500 Days',WIDTH/2-330,HEIGHT/2+415,20,screen)
        message('Time=2000 Days',WIDTH/2-10,HEIGHT/2+415,20,screen)
        message('Time=2500 Days',WIDTH/2+330,HEIGHT/2+415,20,screen)
    
    
        
        if Button_7.collidepoint((mouse_x,mouse_y)):
            T=500
            pygame.draw.rect(screen,(200,200,200),Button_7)
        else:
            pygame.draw.rect(screen,(55,55,255),Button_7)
        if Button_8.collidepoint((mouse_x,mouse_y)):
            T=2000
            pygame.draw.rect(screen,(200,200,200),Button_8)
        else:
            pygame.draw.rect(screen,(55,55,205),Button_8)
        if Button_9.collidepoint((mouse_x,mouse_y)):
            T=2700
            pygame.draw.rect(screen,(200,200,200),Button_9)
        else:
            pygame.draw.rect(screen,(55,55,155),Button_9)



        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                R=False
                pygame.quit()
                Ready=False
                break
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    Ready=True
                    R=False
                    pygame.quit()
                    break
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True

intro_memu()



#Basic Setting 


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Virus")
    
crazy=0
mask=0
De=0
immune=0

players=[]
Diseases=[]
Crazys=[]
Masks=[]
Deads=[]
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
stats = pygame.Surface((WIDTH // 4, HEIGHT // 4))
stats.fill(WHITE)
stats.set_alpha(230)
stats_pos = (WIDTH // 40, HEIGHT // 40)
stats_height = stats.get_height()
stats_width = stats.get_width()

#Load in player Image 
playerImage=pygame.image.load('pla1.png')
enemyImage=pygame.image.load('virus.png')
ufoImage=pygame.image.load('party.png')
sportImage=pygame.image.load('house.png')
SiImage=pygame.image.load('Po.png')
StrongImage=pygame.image.load('health.png')
social_distance=1
#five class of objects 
class player():
    def __init__(self,x,y,vx,vy,health,S):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.present=True
        self.frame=10+social_distance
        self.health=health
        self.S=S
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
    def draw(self,screen):
        if self.present:
            self.move()
            if not self.S:
                screen.blit(playerImage,(self.x,self.y))
            else:
                screen.blit(StrongImage,(self.x,self.y))

class Crazy_1():
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.present=True
        self.frame=6+social_distance
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
    def draw(self,screen):
        if self.present:
            self.move()
            screen.blit(ufoImage,(self.x,self.y))

class Si():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self,screen):
        screen.blit(SiImage,(self.x,self.y))

class Mask_1():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.frame=8+social_distance
        self.defense=25
    def draw(self,screen):
        screen.blit(sportImage,(self.x,self.y))

class virus():
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.present=True
        self.frame=5+social_distance
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
    def draw(self,screen):
        self.move()
        screen.blit(enemyImage,(self.x,self.y))


# Update the image
def Update():
    for player in players:
        player.draw(screen)
    for dis in Diseases:
        dis.draw(screen)
    for cra in Crazys:
        cra.draw(screen)
    for mak in Masks:
        mak.draw(screen)
    for DE in Deads:
        DE.draw(screen)

    #Pygame Surface Part
    stats_graph = pygame.PixelArray(stats)
    t=int(time/T*stats_width)
    Dis=int(disease/totalP*stats_height)
    heal=int(population/totalP*stats_height)
    mas=int(mask/totalP*stats_height)
    craz=int(crazy/totalP*stats_height)
    dead=int(De/totalP*stats_height)
    stats_graph[t,:Dis] = pygame.Color('orange1')
    stats_graph[t,Dis:mas+Dis]=pygame.Color('tomato4')
    stats_graph[t,mas+Dis:craz+mas+Dis]=pygame.Color('red3')
    stats_graph[t,craz+mas+Dis:craz+mas+Dis+heal] = pygame.Color('royalblue')
    stats_graph[t,craz+mas+Dis+heal:craz+mas+Dis+heal+dead] = pygame.Color('darkseagreen3')
    stats_graph[t,craz+mas+Dis+heal+dead:] = pygame.Color('green4')

    del stats_graph
    stats.unlock()
    screen.blit(stats, stats_pos)
    pygame.display.update()

#Text Box


times=[]
adjustment=0.9
timecollection=[]
SiTs=[]
Disease_dead=[]
event_sdate=[200,650,1150,1600,2000]
event_edate=[550,1000,1500,1900,2450]
#Main Loop
#game_intro()
K=False
EDGE=18
Stay_athome=False
Policy_Control=False
totalP=population+disease+crazy+mask+De+immune
pygame.init()
try:
    if Ready:
        print('start')
        for time in range(T):
            if (time>event_sdate[0] and time <event_edate[0]) or (time>event_sdate[1] and time <event_edate[1])or (time>event_sdate[2] and time <event_edate[2])or (time>event_sdate[3] and time <event_edate[3]):
                Disease_period=170
                if time==event_sdate[0]+1 or time==event_sdate[1]+1 or time==event_sdate[2]+1 or time==event_sdate[3]+1:
                    K=True 
                if K:
                    event=chance(3,[0.4,0.3,0.3])
                    K=False
                if event=='a':
                    screen.fill((100,100,255))
                    message('Intermediate Control',WIDTH/2,EDGE*2,40,screen)
                    social_distance=10
                    SpeedL=2
                    SpeedU=2.1
                    PartyChance=0.25
                    QuaratineChance=0.35
                    DisaseChance=0.4
                    Disease_DeadChance=0.05
                    Disease_ImmuneChance=0.5
                    Disease_n=0.45
                    Policy_Control=True
                elif event=='b':
                    Policy_Control=False
                    screen.fill((255,100,100))
                    message('No Control',WIDTH/2,50,40,screen)
                    social_distance=-5
                    SpeedL=4
                    SpeedU=4.4
                    PartyChance=0.7
                    QuaratineChance=0.1
                    DisaseChance=0.2
                    Disease_DeadChance=0.3
                    Disease_ImmuneChance=0.2
                    Disease_n=0.5
                elif event=='c':
                    screen.fill((100,255,100))
                    message('Social Distance',WIDTH/2,50,40,screen)
                    social_distance=25
                    SpeedL=0.6
                    SpeedU=0.8
                    Stay_athome=True
                    PartyChance=0.1
                    QuaratineChance=0.8
                    DisaseChance=0.1
                    Disease_DeadChance=0.025
                    Disease_ImmuneChance=0.625
                    Disease_n=0.35
                    Policy_Control=True
            else:
                screen.fill((255,255,255))
                social_distance=0
                message('Normal Situation',WIDTH/2,50,40,screen)
                PartyChance=0.3
                QuaratineChance=0.2
                DisaseChance=0.5
                Disease_DeadChance=0.1
                Disease_ImmuneChance=0.5
                Disease_n=0.4
                EDGE=24
                SpeedL=3
                SpeedU=3.1
                Disease_period=380
                Policy_Control=True

            #Plottting Section
            if len(Diseases)<disease:
                diseasex=random.randint(EDGE,WIDTH-EDGE)
                diseasey=random.randint(EDGE,HEIGHT-EDGE)
                diseasevx=random.uniform(SpeedL,SpeedU)
                diseasevy=random.uniform(SpeedL,SpeedU)
                Diseases.append(virus(diseasex,diseasey,diseasevx,diseasevy))

            if len(players)<population:
                playerx=random.randint(EDGE,WIDTH-EDGE)
                playery=random.randint(EDGE,HEIGHT-EDGE)
                playervx=random.uniform(SpeedL,SpeedU)
                playervy=random.uniform(SpeedL,SpeedU)
                if RE:
                    players.append(player(playerx,playery,playervx,playervy,200,True))
                    RE=False
                else:
                    players.append(player(playerx,playery,playervx,playervy,40,False))
            
            if len(Crazys)<crazy:
                crazyx=random.randint(EDGE,WIDTH-EDGE)
                crazyy=random.randint(EDGE,HEIGHT-EDGE)
                crazyvx=random.uniform(SpeedL+adjustment,SpeedU+adjustment)
                crazyvy=random.uniform(SpeedL+adjustment,SpeedU+adjustment)
                Crazys.append(Crazy_1(crazyx,crazyy,crazyvx,crazyvy))

            if len(Masks)<mask:
                a=random.randint(EDGE,EDGE*4)
                b=random.randint(WIDTH-4*EDGE,WIDTH-EDGE)
                pos=[a,b]
                maskx=random.choice(pos)
                masky=random.choice(pos)
                Masks.append(Mask_1(maskx,masky))
            
            if len(Deads)<De:
                Deads.append(Si(Deadsx,Deadsy))
                        
            for C in Crazys:
                if C.x<EDGE or C.x>WIDTH-EDGE:
                    C.vx*=-1
                if C.y<EDGE or C.y>HEIGHT-EDGE:
                    C.vy*=-1
                for m in Masks:
                    if (C.x<m.x+m.defense and C.x>m.x-m.defense):
                        C.vx*=-1
                    if (C.y<m.y+m.defense and C.y>m.y-m.defense):
                        C.vy*=-1 

            for D in Diseases:
                if D.x<EDGE or D.x>WIDTH-EDGE:
                    D.vx*=-1
                if D.y<EDGE or D.y>HEIGHT-EDGE:
                    D.vy*=-1
                for m in Masks:
                    if (D.x<m.x+m.defense and D.x>m.x-m.defense):
                        D.vx*=-1
                    if (D.y<m.y+m.defense and D.y>m.y-m.defense):
                        D.vy*=-1 
                if Policy_Control:
                    
                    for d in Diseases:
                        if d!=D:
                            if D.x<d.x+d.frame and D.x>d.x-d.frame:
                                D.vx*=-1
                            if D.y<d.y+d.frame and D.y>d.y-d.frame:
                                D.vy*=-1
                
            for P in players:
                '''if P.x<0 or P.x>WIDTH or P.y<0 or P.y>HEIGHT:
                    players.pop(players.index(P))'''
                if P.x<EDGE or P.x>WIDTH-EDGE:
                    P.vx*=-1
                if P.y<EDGE or P.y>HEIGHT-EDGE:
                    P.vy*=-1
                if Policy_Control:
                    
                    for p in players:
                        if p!=P:
                            if P.x<p.x+p.frame and P.x>p.x-p.frame:
                                P.vx*=-1
                            if P.y<p.y+p.frame and P.y>p.y-p.frame:
                                P.vy*=-1
                else:
                    pass
            
                for d in Diseases:
                    if (P.x<d.x+d.frame and P.x>d.x-d.frame) or (P.y<d.y+d.frame and P.y>d.y-d.frame):
                        P.health-=1
                for m in Masks:
                    if (P.x<m.x+m.defense and P.x>m.x-m.defense):
                        P.vx*=-1
                    if (P.y<m.y+m.defense and P.y>m.y-m.defense):
                        P.vy*=-1
                for c in Crazys:
                    if (P.x<c.x+c.frame and P.x>c.x-c.frame) or (P.y<c.y+c.frame and P.y>c.y-c.frame):
                        P.health-=5
                if Stay_athome:
                    P.health+=80
                    Stay_athome=False

                if P.health==0 or P.health<0:
                    P.present=False
                    players.pop(players.index(P))
                    Probablity=chance(3,[PartyChance,QuaratineChance,DisaseChance])
                    if Probablity=='a':
                        crazy+=1
                        population-=1
                        SiTs.append(time)
                    elif Probablity=='b':
                        mask+=1
                        population-=1
                        timecollection.append(time)
                    else:
                        disease+=1
                        population-=1
                        Disease_dead.append(time)

            #People Stay at home has 80% become immune, 10% Dead, 10% No change 
            for recover in timecollection:
                if (time-recover)>Disease_period:
                    if len(Masks)!=0:
                        prob=chance(3,[0.8,0.1,0.1])
                        if prob=='a':
                            Masks.pop(0)
                            mask-=1
                            RE=True
                            timecollection.pop(timecollection.index(recover))
                            population+=1
                            immune+=1
                        elif prob=='b':
                            Deadsx=Masks[0].x
                            Deadsy=Masks[0].y
                            Masks.pop(0)
                            mask-=1
                            timecollection.pop(timecollection.index(recover))
                            De+=1

                        else:
                            pass
            
            #People parties, has 80% chance dead, 10% immune, 10% no change
            for Dead in SiTs:
                if (time-Dead)>Disease_period:
                    if len(Crazys)!=0:
                        prob=chance(3,[0.4,0.3,0.3])
                        if prob=='a':
                            Deadsx=Crazys[0].x
                            Deadsy=Crazys[0].y
                            SiTs.pop(SiTs.index(Dead))
                            Crazys.pop(0)
                            crazy-=1
                            De+=1
                        elif prob=='b':
                            SiTs.pop(SiTs.index(Dead))
                            Crazys.pop(0)
                            crazy-=1
                            population+=1
        
                        else:
                            pass
                                                   
            #People ar disease has 20% Dead, 50% become immune, 30% stay at same 
            for dd in Disease_dead:
                if (time-dd)>Disease_period:
                    if disease!=0:
                        prob=chance(3,[Disease_DeadChance,Disease_ImmuneChance,Disease_n])
                        if prob=='a':
                            Deadsx=Diseases[0].x
                            Deadsy=Diseases[0].y
                            Diseases.pop(0)
                            Disease_dead.pop(Disease_dead.index(dd))
                            disease-=1
                            De+=1
                        elif prob=='b':
                            Diseases.pop(0)
                            Disease_dead.pop(Disease_dead.index(dd))
                            disease-=1
                            population+=1
                            RE=True
                            immune+=1
                        else:
                            Diseases.pop(0)
                            Disease_dead.pop(Disease_dead.index(dd))
                            disease-=1
                            population+=1

            message('Surviver:'+str(len(players)),WIDTH-3*EDGE,HEIGHT-5*EDGE,15,screen)
            message('Infected:'+str(len(Diseases)),WIDTH-3*EDGE,HEIGHT-4*EDGE,15,screen)
            message('Quaratine:'+str(mask),WIDTH-3*EDGE,HEIGHT-3*EDGE,15,screen)
            message('Party People:'+str(crazy),WIDTH-3*EDGE,HEIGHT-2*EDGE,15,screen)
            message('Dead:'+str(De),WIDTH-3*EDGE,HEIGHT-1*EDGE,15,screen)
            Update()
except Exception as e:
    print('Please provide input!')
    pass
def result():
    pygame.init()
    running=True
    try:
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
            screen.fill((255,255,255))
            message('Final Result',WIDTH/2,HEIGHT/2-200,100,screen)
            message('Suriver:'+str(population),WIDTH/2,HEIGHT/2+50,50,screen)
            message('Infected:'+str(len(Diseases)),WIDTH/2,HEIGHT/2+100,50,screen)
            message('Quaratine:'+str(mask),WIDTH/2,HEIGHT/2+150,50,screen)
            message('Party People:'+str(crazy),WIDTH/2,HEIGHT/2+200,50,screen)
            message('Dead:'+str(De),WIDTH/2,HEIGHT/2+260,50,screen)
            message('Starting Population:'+str(Start_population),WIDTH/2,HEIGHT/2-50,50,screen)
            message('Starting Infection:'+str(Start_infection),WIDTH/2,HEIGHT/2,50,screen)
            message('Time Period:{} Days'.format(str(T)),WIDTH/2,HEIGHT/2-100,50,screen)
            pygame.display.update()
    except Exception as e:
        print('No input')
        pass

result()