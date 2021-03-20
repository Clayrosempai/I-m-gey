import pygame
pygame.init()
display_width = 1000
display_height = 700

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SPAWN')
black = (0,0,0)

white = (255,255,255) 
PersomImg = pygame.image.load('fon.jpg')
fon = pygame.image.load("fon.jpg")
bullet_Img = pygame.image.load('fon.png')

# fon_top = gameDisplay.get_height() - fon.get_height()
# fon_left = gameDisplay.get_width()/2 - fon.get_width()/2
x =  (display_width * 0.45)
y = (display_height * 0.8)	#1
x_bullet =[]
y_bullet =[]
x_change = 0
spawn = False
# PersomImg_speed = 0
# bullet_speed = 0

gameDisplay.blit(fon, (123,100))

def Persom(x,y): 
    gameDisplay.blit(PersomImg, (x,y))

def bullet(x,y):
    gameDisplay.blit(bullet_Img, (x,y))

clock = pygame.time.Clock()

crashed = False

while not crashed: 
    for event in pygame.event.get():
    ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif ebent.key == pygame.K_SPACE:
               spawn = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ######################
    if spawn == True:
        x_bullet.append(x) 
        y_bullet.append(y)
        spawn = False 
    x=x+x_change
    Persom(x,y)
    for i in range(len (y_bullet)):
        y_bullet[i] -=2 
        if y_bullet[i]< 0:
            del(y_bullet [i])
            del(x_bullet [i])
        else:
            bullet(x_bullet[i],y_bullet[i]) 
    pygame.display.update()
    clock.tick(60)