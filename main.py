from math import sqrt
import random
import pygame

#intialize pygame
pygame.init()
#Adjust to resize screen
maxW,maxH=900,500   
screen= pygame.display.set_mode((maxW,maxH))

#Background
background= pygame.image.load("img/starbg.jpg")


#Title and background
pygame.display.set_caption("Hello World")
icon= pygame.image.load('img/logo.png')
pygame.display.set_icon(icon)
gameover= pygame.image.load('img/gameover.png')

#Animation
explode = pygame.image.load('img/explode.png')

#Laser
laserImg=pygame.image.load("img/medical.png")
laserState=0
laserX,laserY=0,0
disX,disY,dis=0,0,0
laserA,laserB =0,0
diLaserX,diLaserY=0,0
laserEdge=24
#Player
playerImg=pygame.image.load("img/worldwide.png")
playerX,playerY= 268,250
changeX,changeY=0,0
playerEdge=24
alive=1
#enemies
enemiesImg=pygame.image.load("img/ufo.png")
eX,eY,diX,diY,speedY=300,0,1,1,0
enemyEdge=64

def player(State,x,y):
    screen.blit(State,(x,y))

def enemy(x,y):
    screen.blit(enemiesImg,(x,y))

def laser(x,y):

    screen.blit(laserImg,(x,y))

def fire():
    global playerX,playerY,eX,eY,laserA,laserB,laserX,laserY,laserState,diLaserX,diLaserY,dis,disX,disY
    laserState=1
    diLaserX= abs(playerX-eX)/(playerX-eX)
    diLaserY= abs(playerY-eY)/(playerY-eY)
    dis=sqrt((playerY-eY)*(playerY-eY)+(playerX-eX)*(playerX-eX))

    a=(playerY-eY)/(playerX-eX) 
    b=playerY- a*playerX
    
    laserA,laserB=a,b
    disX,disY=abs(playerX-eX),abs(playerY-eY)
    laserX,laserY= eX,eY

def crt():
    global eX,eY,diX,diY
    # eX=random.choice([0,568])
    # eY=random.randint(0,468)
    if eX<=0:
        diX=random.uniform(1,1.3)
    if eX>=maxW-enemyEdge:
        diX=-random.uniform(1,1.3)
    if eY<=0:
        diY=random.uniform(1,1.3)
    if eY>=maxH-enemyEdge:
        diY=-random.uniform(1,1.3)

def isCollide(a,b,x,y):
    if sqrt((a-x)*(a-x)+(b-y)*(b-y))< 20:
        return 1
    return 0

#Game Loop
running= True
while running:
    screen.fill((4,4,4))
    screen.blit(background,(0,0))
        
    if isCollide(playerX,playerY,eX,eY) or isCollide(playerX,playerY,laserX,laserY) and alive==1:
        alive=0
        laserState=0
        # screen.blit(gameover,(maxW/2-180,maxH/2-180))
         
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running=False
        if event.type== pygame.VIDEORESIZE:
            screen=pygame.display.set_mode((event.h,event.w),pygame.VIDEORESIZE)
        if alive==1 and event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                changeX-=0.5*(maxW/600)
            if event.key== pygame.K_RIGHT:
                changeX+=0.5*(maxW/600)
            if event.key== pygame.K_DOWN:
                changeY+=0.5*(maxW/600)
            if event.key== pygame.K_UP:
                changeY-=0.5*(maxW/600)
        
        if event.type== pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key== pygame.K_RIGHT:
                changeX=0
            if event.key==pygame.K_DOWN or event.key== pygame.K_UP:
                changeY=0
    
     #Enenmy
    crt()
    eX += 0.1*(maxW/600)*diX
    eY += 0.1*(maxW/600)*diY

    # Laser
    if laserState == 0 and alive==1 :
        fire()
    if laserX<-laserEdge or laserX>maxW or laserY<-laserEdge or laserY>maxH:
        laserState=0
    # laserX+= 0.25*diLaserX
    # laserY= laserA*laserX+ laserB
    if laserState==1:
        laserX+= 0.45*(maxW/600)*disX/dis * diLaserX
        laserY+= 0.45*(maxW/600)*disY/dis * diLaserY
    #Player
    if 0<playerX+changeX<maxW-laserEdge:
        playerX+=changeX
    if 0<playerY+changeY<maxH-laserEdge:
        playerY+=changeY

    enemy(eX,eY)
    laser(laserX,laserY)
    if alive==1:
        player(playerImg,playerX,playerY)
    else :
        player(explode,playerX-48,playerY-48)
        screen.blit(gameover,(270,70))
    pygame.display.update()
    # break

