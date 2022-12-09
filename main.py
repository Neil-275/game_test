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
laserImg=pygame.image.load("laser.png")
laserState=0
laserX,laserY=0,0
diLaserX, diLaserY=0,0

#Player
playerImg=pygame.image.load("cloud.png")
playerX,playerY= 268,250
changeX,changeY=0,0

#enemies
enemiesImg=pygame.image.load("ufo.png")
eX,eY,diX,diY,speedY=-129,0,1,1,0


def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemiesImg,(x,y))

def laser(x,y):
    screen.blit(laserImg,(x,y))

def fire():
    global playerX,playerY,eX,eY,diLaserX,diLaserY,laserX,laserY,laserState
    laserState=1
    a=(playerY-eY)/(playerX-eX)
    b=playerY- a*playerX
    # b/=(a/0.2)
    # a/=(a/0.2)
    diLaserX,diLaserY=a,b
    print (a,b)
    laserX,laserY= eX,eY

def crt():
    global eX,eY,diX,diY,speedY,laserState
    eX=random.choice([0,568])
    eY=random.randint(0,468)
    if eX==0:
        diX=1
    if eX==568:
        diX=-1
    diY=random.choice([1,-1])
    speedY=random.uniform(0.1,0.3)
    laserState=0

# print (random.choice([0,568]))

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
    
    #Laser
    # if laserState ==0 :
    #     fire()
    # if laserX<-25 or laserX>600:
    #     laserState=0
    # laserX+= diLaserX*0.2
    # laserY+= diLaserY*0.02

    # #Enenmy
    # if eX<-128 or eX>600:
    #     crt()
    # eX += 0.3 *diX
    # eY += speedY *diY
    # #Player
    # if 0<playerX+changeX<568:
    #     playerX+=changeX
    # if 0<playerY+changeY<468:
    #     playerY+=changeY

    enemy(eX,eY)
    laser(laserX,laserY)
    player(playerX,playerY)
    crt()
    print (eX,eY)
    print (playerX,playerY)
    fire()
    pygame.display.update()
    break
