import pygame
import random
import time
pygame.init()
display_width = 1000
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SPAWN')
black = (0,0,0)

white = (255,255,255) 
PersomImg = pygame.image.load('hero.png')
fon = pygame.image.load("fon.jpg")
bullet_Img = pygame.image.load('bullet.png')
zombi_Img = pygame.image.load('ZOMBI.png')
healthss_Img = pygame.image.load('healthss.png')
healthss_Img = pygame.image.load('healthss.png')
T91_Img = pygame.image.load('T91.png')
T91_Img = pygame.image.load('T91.png')
T91_Img = pygame.image.load('T91.png')


# fon_top = gameDisplay.get_height() - fon.get_height()
# fon_left = gameDisplay.get_width()/2 - fon.get_width()/2
x =  (display_width * 0.45)
y = (display_height * 0.8)	#1
x_bullet =[]
y_bullet =[]
x_zombi = []
y_zombi = []
x_change = 0
spawn = False 
spawn_left = False
# PersomImg_speed = 0
# bullet_speed = 0

health_counter=2
left_T91_counter=3
right_T91_counter=3

gameDisplay.blit(fon, (123,100))

def Persom(x,y): 
    gameDisplay.blit(PersomImg, (x,y))

def bullet(x,y):
    gameDisplay.blit(bullet_Img, (x,y))

def zombi(x,y):
    gameDisplay.blit(zombi_Img, (x,y))

clock = pygame.time.Clock()

crashed = False 
start_time = time.time()

while not crashed: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
            elif event.key == pygame.K_RIGHT:
                x_change = 10
            elif event.key == pygame.K_SPACE:
               spawn = True
            elif event.key == pygame.K_LSHIFT:
                spawn_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ####################
    gameDisplay.fill(white)
    gameDisplay.blit(fon, (display_width * 0.2,0))
    if left_T91_counter>0:
        for i in range(left_T91_counter-1):
            gameDisplay.blit(T91_Img, (display_width * -0.0, display_height * (0.3+0.1*i)))
    else:
        pass
    if right_T91_counter>0:
        for i in range(right_T91_counter-1):
              gameDisplay.blit(T91_Img, (display_width * 0.1, display_height * (0.3+0.1*i)))
    else:
        pass

    if health_counter == 2: 
        gameDisplay.blit(healthss_Img, (display_width * -0.05, display_height * 0.05))
        gameDisplay.blit(healthss_Img, (display_width * 0.04, display_height * 0.05))
    elif health_counter == 1:
        gameDisplay.blit(healthss_Img, (display_width * -0.05, display_height * 0.05))

    if time.time()-start_time >2:
        x_zombi.append(random.randint(0.2 * display_width,display_width * 0.9))
        y_zombi.append(0)
        if left_T91_counter<=3:
            left_T91_counter+=1
        if right_T91_counter<=3:
            right_T91_counter+=1
        start_time = time.time()
    for i in range(len (y_zombi)):
        y_zombi[i] +=2  
        if y_zombi[i]> display_height:
            del(y_zombi [i])
            del(x_zombi [i])
            health_counter-=1
            break
        else:
            zombi(x_zombi[i], y_zombi[i])
        
        
    if spawn == True and right_T91_counter>0:
        x_bullet.append(x+130) 
        y_bullet.append(y)
        right_T91_counter-=1 
        spawn = False 
    if spawn_left == True and left_T91_counter>0:
        x_bullet.append(x+25) 
        y_bullet.append(y)
        spawn_left = False
        left_T91_counter-=1
    
    
    x=x+x_change
    if x < 0.2 * display_width:
        x = 0.2 * display_width
    elif x > 0.9 * display_width:
        x = 0.9 * display_width
    Persom(x,y)
    for i in range(len (y_bullet)):
         y_bullet[i] -=10 
    for i in range(len (y_bullet)):
        if y_bullet[i]< 0:
            del(y_bullet [i])
            del(x_bullet [i])
            break
        else:
            bullet(x_bullet[i],y_bullet[i])
    fed = False
    for c in range(len (y_zombi)):
        for i in range(len (y_bullet)):
            if abs(x_zombi[c]+23-x_bullet[i]-123)<=125+123 and abs(y_zombi[c]+23-y_bullet[i] -100)<=23+123:
                del(y_zombi [c])
                del(x_zombi [c])
                del(y_bullet [i])
                del(x_bullet [i])
                fed = True 
                break
        if fed == True:
            break
    pygame.display.update()
    clock.tick(60)