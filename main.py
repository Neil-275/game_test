import random
import pygame


#intialize pygame
pygame.init()
screen= pygame.display.set_mode((600,500))

#Background
background= pygame.image.load("bg.jpg")

#Title and background
pygame.display.set_caption("Hello World")
icon= pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#Laser
laserImg=pygame.image.load("medical.png")
laserState=0
laserX,laserY=0,0
laserA,laserB =0,0
diLaser=0

#Player
playerImg=pygame.image.load("worldwide.png")
playerX,playerY= 268,250
changeX,changeY=0,0

#enemies
enemiesImg=pygame.image.load("ufo.png")
eX,eY,diX,diY,speedY=0,0,1,1,0


def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemiesImg,(x,y))

def laser(x,y):
    screen.blit(laserImg,(x,y))

def fire():
    global playerX,playerY,eX,eY,laserA,laserB,laserX,laserY,laserState,diLaser
    laserState=1
    diLaser= abs(playerX-eX)/(playerX-eX)
    a=(playerY-eY)/(playerX-eX) 
    b=playerY- a*playerX
   
    laserA,laserB=a,b
    laserX,laserY= eX,eY

def crt():
    global eX,eY,diX,diY
    # eX=random.choice([0,568])
    # eY=random.randint(0,468)
    if eX<=0:
        diX=1
    if eX>=536:
        diX=-1
    if eY<=0:
        diY=1
    if eY>=436:
        diY=-1

#Game Loop
running= True
while running:
    screen.fill((4,4,4))
    screen.blit(background,(0,0))
   
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running=False
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                changeX-=0.5
            if event.key== pygame.K_RIGHT:
                changeX+=0.5
            if event.key== pygame.K_DOWN:
                changeY+=0.5
            if event.key== pygame.K_UP:
                changeY-=0.5
        
        if event.type== pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key== pygame.K_RIGHT:
                changeX=0
            if event.key==pygame.K_DOWN or event.key== pygame.K_UP:
                changeY=0
    
     #Enenmy
    crt()
    eX += 0.1 *diX
    eY += 0.1 *diY

    # Laser
    if laserState == 0 :
        fire()
    if laserX<-25 or laserX>600:
        laserState=0
    laserX+= 0.25*diLaser
    laserY= laserA*laserX+ laserB
    
    #Player
    if 0<playerX+changeX<568:
        playerX+=changeX
    if 0<playerY+changeY<468:
        playerY+=changeY

    enemy(eX,eY)
    laser(laserX,laserY)
    player(playerX,playerY)
    pygame.display.update()
    # break
