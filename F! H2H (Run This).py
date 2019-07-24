#import statements and initializers
import pygame
from time import sleep
from random import randint
pygame.init()
pygame.font.init()
pygame.mixer.init()
print("Initialized!")

#initialize the display parameters
display_width = 850
display_height = 900

#Creates the display and heading
DISPLAY = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Frogger: Head 2 Head!')

#Entire game loops within this while loop
def play_game():
    #pre define colors
    background=(167,47,69)
    road = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    grass=(143,210,17)
    lake = (2,102,233)

    #store state of end holes for both players, when all are True, the game is over.
    h1=False;h2=False;h3=False;h4=False;h5=False;
    s1=False;s2=False;s3=False;s4=False;s5=False;

    #stores winner text when any 5 holes are completed
    winner = ""

    #stores charge values for attack
    charge=0
    charge_red=0

    #load colors and end holes
    end = pygame.image.load('end.png')
    markers =  pygame.image.load('markers.png')

    #Each list is a lane of cars or logs. the values inside are the starting x positions of the car/log
    cars=[25, 300, 600, 900]
    cars2=[100, 460, 820]
    cars3=[0, 225, 450, 675, 900]
    cars4=[0, 180, 360, 540, 720, 900]

    logs=[0, 225, 450, 675, 900]
    logs2=[0, 450, 900]
    logs3=[0, 300, 600, 900]
    logs4=[0, 225, 450, 675, 900]

    #Directionn variables keep track of player orientation
    dir_1 = 0
    dir_2 = 0
    
    #Starting position for Player 1 (Green Frog)
    x=403
    y=display_height-90

    #Starting position for Player 2 (Red Frog)
    x2=403
    y2=60

    #as long as this is False game will run
    gameExit = False
    
    pygame.mixer.music.set_volume(0.1)
    ingame = pygame.mixer.Sound('ingame.wav')
    ingame.play(-1, fade_ms=3000)
    while gameExit == False:
            sleep(0.003)
            #Checks all python events for quit statements and then quits
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    pygame.quit()
                    quit()

                #Creates a Sprite for Player 1 and 2. Then creates a rect object for each player to define hitbox   
                p1_r=pygame.sprite.Sprite()
                p2_r=pygame.sprite.Sprite()
                p1_r.rect = pygame.Rect(x,y,50,50)
                p2_r.rect = pygame.Rect(x2,y2,50,50)

                #checks all events for keydown
                if event.type == pygame.KEYDOWN:
                    print("X:",x,"Y:",y,"  |  X2:", x2, "Y2:", y2)
                    #checks for player 1 input. up, down, left, or right arrow will initialize a collision check.
                    if event.key == pygame.K_UP and y>0:
                        
                        #Will allow movement as long as there is no collision between players, the block is not grass and the block is not lake.
                        p1_r.rect = pygame.Rect(x,y-42,50,50)
                        if pygame.sprite.collide_rect(p1_r,p2_r) == 0 and DISPLAY.get_at((int(round(x+20)),int(round(y-40))))[0]!=grass[0]:
                            #If the block is a lake, respawn player 1
                            if DISPLAY.get_at((int(round(x+20)),int(round(y-20))))[0]==lake[0]:
                                splash = pygame.mixer.Sound('SPLASH3.wav')
                                splash.play()
                                x=403
                                y=display_height-90
                                
                            else:
                                #Allows movement, sets direction variable and moves character
                                pygame.mixer.music.set_volume(0.1)
                                jump = pygame.mixer.Sound('jump.wav')
                                jump.play()
                                dir_1=1
                                y-=50
                                
                    if event.key == pygame.K_DOWN and y<display_height-50:
                        p1_r.rect = pygame.Rect(x,y+42,50,50)
                        if pygame.sprite.collide_rect(p1_r,p2_r) == 0 and DISPLAY.get_at((int(round(x+10)),int(round(y+50))))[0]!=grass[0]:

                            if DISPLAY.get_at((int(round(x+10)),int(round(y+50))))[0]==lake[0]:
                                splash = pygame.mixer.Sound('SPLASH3.wav')
                                splash.play()
                                x=403
                                y=display_height-90

                            else:
                                pygame.mixer.music.set_volume(0.1)
                                jump = pygame.mixer.Sound('jump.wav')
                                jump.play()
                                dir_1=2
                                y+=50
                                
                    if event.key == pygame.K_LEFT and x>40:
                        p1_r.rect = pygame.Rect(x-42,y,50,50)
                        if pygame.sprite.collide_rect(p1_r,p2_r) == 0 and DISPLAY.get_at((int(round(x-10)),int(round(y+1))))[0]!=grass[0]:
                            if DISPLAY.get_at((int(round(x-10)),int(round(y+10))))[0]==lake[0]:
                                splash = pygame.mixer.Sound('SPLASH3.wav')
                                splash.play()
                                x=403
                                y=display_height-90

                            else:
                                pygame.mixer.music.set_volume(0.1)
                                jump = pygame.mixer.Sound('jump.wav')
                                jump.play()
                                dir_1=3
                                x-=50

                    if event.key == pygame.K_RIGHT and x<display_width-60:
                        p1_r.rect = pygame.Rect(x+42,y,50,50)
                        if pygame.sprite.collide_rect(p1_r,p2_r) == 0 and DISPLAY.get_at((int(round(x+50)),int(round(y+1))))[0]!=grass[0]:
                            if DISPLAY.get_at((int(round(x+50)),int(round(y+10))))[0]==lake[0]:
                                splash = pygame.mixer.Sound('SPLASH3.wav')
                                splash.play()
                                x=403
                                y=display_height-90

                            else:
                                pygame.mixer.music.set_volume(0.1)
                                jump = pygame.mixer.Sound('jump.wav')
                                jump.play()
                                dir_1=4
                                x+=50
                            
                    #Player 2 Movement same concepts are Player 1 movement
                    if event.key == pygame.K_w and y2>10:
                        p2_r.rect = pygame.Rect(x2,y2-42,50,50)
                        if pygame.sprite.collide_rect(p1_r,p2_r) == 0 and DISPLAY.get_at(((int(round(x2+25)),(int(round(y2-25))))))[0]!=grass[0]:

                            #Plays a splash sound if they land in water
                            if DISPLAY.get_at(((int(round(x2+25)),(int(round(y2-25))))))[0]==lake[0]:
                                splash = pygame.mixer.Sound('SPLASH3.wav')
                                splash.play()
                                x2=403
                                y2=60
                                
                            #Plays a jump sound when they move
                            else:
                                pygame.mixer.music.set_volume(0.1)
                                jump = pygame.mixer.Sound('jump.wav')
                                jump.play()
                                dir_2=1
                                y2-=50

                    ##MOVEMENT##
                    if event.key == pygame.K_s and y2<display_height-40:
                        p2_r.rect = pygame.Rect(x2,y2+42,50,50)
                        if pygame.sprite.collide_rect(p1_r,p2_r) == 0 and DISPLAY.get_at(((int(round(x2+10)),(int(round(y2+50))))))[0]!=grass[0]:
                            if DISPLAY.get_at(((int(round(x2+10)),(int(round(y2+50))))))[0]==lake[0]:
                                splash = pygame.mixer.Sound('SPLASH3.wav')
                                splash.play()
                                x2=403
                                y2=60

                            else:
                                pygame.mixer.music.set_volume(0.1)
                                jump = pygame.mixer.Sound('jump.wav')
                                jump.play()
                                dir_2=2
                                y2+=50

                    if event.key == pygame.K_a and x2>5:
                        p2_r.rect = pygame.Rect(x2-42,y2,50,50)
                        if pygame.sprite.collide_rect(p1_r,p2_r) == 0 and DISPLAY.get_at(((int(round(x2-10)),(int(round(y2+10))))))[0]!=grass[0]:
                            if DISPLAY.get_at(((int(round(x2-10)),(int(round(y2+10))))))[0]==lake[0]:
                                splash = pygame.mixer.Sound('SPLASH3.wav')
                                splash.play()
                                x2=403
                                y2=60

                            else:
                                pygame.mixer.music.set_volume(0.1)
                                jump = pygame.mixer.Sound('jump.wav')
                                jump.play()
                                dir_2=3
                                x2-=50

                    if event.key == pygame.K_d and x2<display_width-50:
                        p2_r.rect = pygame.Rect(x2+42,y2,50,50)
                        if pygame.sprite.collide_rect(p1_r,p2_r) == 0 and DISPLAY.get_at(((int(round(x2+50)),(int(round(y2+10))))))[0]!=grass[0]:
                            if DISPLAY.get_at(((int(round(x2+50)),(int(round(y2+10))))))[0]==lake[0]:
                                splash = pygame.mixer.Sound('SPLASH3.wav')
                                splash.play()
                                x2=403
                                y2=60

                            else:
                                pygame.mixer.music.set_volume(0.1)
                                jump = pygame.mixer.Sound('jump.wav')
                                jump.play()
                                dir_2=4
                                x2+=50

            #checks player 1's y value. if it is 10 (the 5 end holes), it will check for collision between player and any end hole.
            #if there is collision, it will change the respective hole variables at the top to True.
            if y==10:
                #Following creates Sprite and Hitboxes for the Player and each hole on Player 2's side.
                p1=pygame.sprite.Sprite()
                p1.rect = pygame.Rect(x,y,50,50)
                
                hole1=pygame.sprite.Sprite()
                hole1.rect = pygame.Rect(103,0,50,50)

                hole2 =pygame.sprite.Sprite()
                hole2.rect = pygame.Rect(253,0,50,50)

                hole3 =pygame.sprite.Sprite()
                hole3.rect = pygame.Rect(403,0,50,50)

                hole4 =pygame.sprite.Sprite()
                hole4.rect = pygame.Rect(553,0,50,50)

                hole5 =pygame.sprite.Sprite()
                hole5.rect = pygame.Rect(703,0,50,50)

                #if Player 1 collides with the end hole, fill it and then respawn the player.
                if pygame.sprite.collide_rect(p1,hole1) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x=403
                        y=display_height-90
                        h1=True
                elif pygame.sprite.collide_rect(p1,hole2) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x=403
                        y=display_height-90
                        h2=True
                elif pygame.sprite.collide_rect(p1,hole3) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x=403
                        y=display_height-90
                        h3=True
                elif pygame.sprite.collide_rect(p1,hole4) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x=403
                        y=display_height-90
                        h4=True
                elif pygame.sprite.collide_rect(p1,hole5) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x=403
                        y=display_height-90
                        h5=True

            #Same hole check but for player 2.
            if y2==860:
                p2=pygame.sprite.Sprite()
                p2.rect = pygame.Rect(x2,y2,50,50)
                
                hole1=pygame.sprite.Sprite()
                hole1.rect = pygame.Rect(103,850,50,50)

                hole2 =pygame.sprite.Sprite()
                hole2.rect = pygame.Rect(253,850,50,50)

                hole3 =pygame.sprite.Sprite()
                hole3.rect = pygame.Rect(403,850,50,50)

                hole4 =pygame.sprite.Sprite()
                hole4.rect = pygame.Rect(553,850,50,50)

                hole5 =pygame.sprite.Sprite()
                hole5.rect = pygame.Rect(703,850,50,50)
                
                if pygame.sprite.collide_rect(p2,hole1) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x2=403
                        y2=60
                        s1=True
                elif pygame.sprite.collide_rect(p2,hole2) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x2=403
                        y2=60
                        s2=True
                elif pygame.sprite.collide_rect(p2,hole3) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x2=403
                        y2=60
                        s3=True
                elif pygame.sprite.collide_rect(p2,hole4) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x2=403
                        y2=60
                        s4=True
                elif pygame.sprite.collide_rect(p2,hole5) == 1:
                        hole = pygame.mixer.Sound('hole.wav')
                        hole.play()
                        x2=403
                        y2=60
                        s5=True
                        
            #Redraws the entire display including lakes, lanes, lane markers, end holes.
            DISPLAY.fill((0,0,0))
            DISPLAY.blit(end,(0,0))
            DISPLAY.blit(end, (0,850))
            
            pygame.draw.rect(DISPLAY, (34,177,83), (0,50,display_width,50))
            pygame.draw.rect(DISPLAY, (34,177,83), (0,300,display_width,50))
            pygame.draw.rect(DISPLAY, (34,177,83), (0,550,display_width,50))
            pygame.draw.rect(DISPLAY, (34,177,83), (0,800,display_width,50))
            pygame.draw.rect(DISPLAY, lake, (0,350,display_width, 200))
            
            DISPLAY.blit(markers, (-12,150))
            DISPLAY.blit(markers, (-12,200))
            DISPLAY.blit(markers, (-12,250))
            DISPLAY.blit(markers, (-12,650))
            DISPLAY.blit(markers, (-12,700))
            DISPLAY.blit(markers, (-12,750))

            #checks hole variables and fill in the ones that are True
            if h1==True:
                pygame.draw.rect(DISPLAY, grass, (103,0,90,50))
            if h2==True:
                pygame.draw.rect(DISPLAY, grass, (253,0,90,50))
            if h3==True:
                pygame.draw.rect(DISPLAY, grass, (403,0,90,50))
            if h4==True:
                pygame.draw.rect(DISPLAY, grass, (550,0,90,50))
            if h5==True:
                pygame.draw.rect(DISPLAY, grass, (700,0,90,50))
          
            if s1==True:
                pygame.draw.rect(DISPLAY, grass, (103,850,90,50))
            if s2==True:
                pygame.draw.rect(DISPLAY, grass, (253,850,90,50))
            if s3==True:
                pygame.draw.rect(DISPLAY, grass, (403,850,90,50))
            if s4==True:
                pygame.draw.rect(DISPLAY, grass, (550,850,90,50))
            if s5==True:
                pygame.draw.rect(DISPLAY, grass, (700,850,90,50))

            #This function is responsible for the movement of logs and cars.
            def lane(x3, lanenum):
                #creates the Sprite and Hitbox for both players and 2 variables for cars. This is because each lane for cars is repeated on the other side.
                p1_r=pygame.sprite.Sprite()
                p1_r.rect = pygame.Rect(x,y,50,50)
                p2_r=pygame.sprite.Sprite()
                p2_r.rect = pygame.Rect(x2,y2,50,50)
                car=pygame.sprite.Sprite()
                car2=pygame.sprite.Sprite()

                #Lane 1-4 handles car movement.
                if lanenum == 1:
                    #Draws the car
                    pygame.draw.rect(DISPLAY, (23, 45, 198), (x3, 115, 105, 20))
                    pygame.draw.rect(DISPLAY, (23, 45, 198), (x3, 765, 105, 20))
                    #for as many cars in the car lists at the top of the program, sets its hitbox to the lanes it is responsible for.
                    for i in range(len(cars)):
                        car.rect=pygame.Rect(cars[i],115,105,20)
                        car2.rect=pygame.Rect(cars[i],765,105,20)
                        #if the player collides in any of the lanes the car is responsible for, return 1 or 2 depending on the player.
                        if pygame.sprite.collide_rect(car,p1_r) == 1 or pygame.sprite.collide_rect(car2,p1_r) == 1:
                            return 1
                        elif pygame.sprite.collide_rect(car,p2_r)==1 or pygame.sprite.collide_rect(car2,p2_r) == 1:
                            return 2

                #Different car lane    
                elif lanenum == 2:
                    pygame.draw.rect(DISPLAY, (250,37,21), (x3, 170, 80, 20))
                    pygame.draw.rect(DISPLAY, (250,37,21), (x3, 720, 80, 20))
                    for i in range(len(cars2)):
                        car.rect=pygame.Rect(cars2[i],170,80,20)
                        car2.rect=pygame.Rect(cars2[i],720,80,20)
                        if pygame.sprite.collide_rect(car,p1_r) == 1 or pygame.sprite.collide_rect(car2,p1_r) == 1:
                            return 1
                        elif pygame.sprite.collide_rect(car,p2_r)==1 or pygame.sprite.collide_rect(car2,p2_r) == 1:
                            return 2

                #Different car lane
                elif lanenum == 3:
                    pygame.draw.rect(DISPLAY, (244, 111, 7), (x3, 215, 50, 25))
                    pygame.draw.rect(DISPLAY, (244, 111, 7), (x3, 665, 50, 25))
                    for i in range(len(cars3)):
                        car.rect=pygame.Rect(cars3[i],215,50,25)
                        car2.rect=pygame.Rect(cars3[i],665,50,25)
                        if pygame.sprite.collide_rect(car,p1_r) == 1 or pygame.sprite.collide_rect(car2,p1_r) == 1:
                            return 1
                        elif pygame.sprite.collide_rect(car,p2_r)==1 or pygame.sprite.collide_rect(car2,p2_r) == 1:
                            return 2
                        
                #Different car lane
                elif lanenum == 4:
                    pygame.draw.rect(DISPLAY, (49, 205, 17), (x3, 265, 70, 25))
                    pygame.draw.rect(DISPLAY, (49, 205, 17), (x3, 615, 70, 25))
                    for i in range(len(cars4)):
                        car.rect=pygame.Rect(cars4[i],265,70,25)
                        car2.rect=pygame.Rect(cars4[i],615,70,25)
                        if pygame.sprite.collide_rect(car,p1_r) == 1 or pygame.sprite.collide_rect(car2,p1_r) == 1:
                            return 1
                        elif pygame.sprite.collide_rect(car,p2_r)==1 or pygame.sprite.collide_rect(car2,p2_r) == 1:
                            return 2

                #First log lane
                elif lanenum == 5:
                    #draws the log
                    pygame.draw.rect(DISPLAY, (66, 43, 17), (x3, 355, 150, 40))
                    for i in range(len(logs)):
                        #creates log hitbox
                        car.rect=pygame.Rect(logs[i],365,150,40)
                        if pygame.sprite.collide_rect(car,p1_r) == 1:
                            #handles two players on the same log
                            if y==y2:
                                return 2
                            else:
                                return 3
                        #player 2 collision with log
                        elif pygame.sprite.collide_rect(car,p2_r)==1:
                            if y2==y:
                                return 2
                            else:
                                return 4

                #second log lane
                elif lanenum == 6:
                    pygame.draw.rect(DISPLAY, (66, 43, 17), (x3, 405, 100, 40))
                    for i in range(len(logs2)):
                        car.rect=pygame.Rect(logs2[i],415,100,40)
                        if pygame.sprite.collide_rect(car,p1_r) == 1:
                            if y==y2:
                                return 2
                            else:
                                return 3
                        elif pygame.sprite.collide_rect(car,p2_r)==1:
                            if y2==y:
                                return 2
                            else:
                                return 4
                            
                #third log lane 
                elif lanenum == 7:
                    pygame.draw.rect(DISPLAY, (66, 43, 17), (x3, 455, 100, 40))
                    for i in range(len(logs3)):
                        car.rect=pygame.Rect(logs3[i],465,100,40)
                        if pygame.sprite.collide_rect(car,p1_r) == 1:
                            if y==y2:
                                return 2
                            else:
                                return 3
                        elif pygame.sprite.collide_rect(car,p2_r)==1:
                            if y2==y:
                                return 2
                            else:
                                return 4
                            
                #4th log lane
                elif lanenum == 8:
                    pygame.draw.rect(DISPLAY, (66, 43, 17), (x3, 505, 70, 40))
                    for i in range(len(logs4)):
                        car.rect=pygame.Rect(logs4[i],515,70,40)
                        if pygame.sprite.collide_rect(car,p1_r) == 1:
                            if y==y2:
                                return 2
                            else:
                                return 3
                        elif pygame.sprite.collide_rect(car,p2_r)==1:
                            if y2==y:
                                return 2
                            else:
                                return 4

            #responsible for changing the x values of lane 1/4 cars
            for i in range(len(cars)):
                #essentially the speed of the car
                cars[i]+=0.5
                #if it crosses the edge, it will respawn to create an endless loop
                if cars[i]>display_width+105:
                    cars[i]=-170
                #sends each car x value to the lane() function to handle drawing
                lane(cars[i],1)

                #handles lane()'s return statements. 1 is collison with player 1 and vice versa
                if lane(cars[i],1) == 1:
                    crash = pygame.mixer.Sound('crash.wav')
                    crash.play()
                    #respawn player 1
                    x=403
                    y=display_height-90
                elif lane(cars[i],1)==2:
                    crash = pygame.mixer.Sound('crash.wav')
                    crash.play()
                    #respawn player 2
                    x2=403
                    y2=60

            #handles movement for lane 2/3 cars
            for i in range(len(cars2)):
                cars2[i]-=1.8
                if cars2[i]<-150:
                    cars2[i]=900
                lane(cars2[i],2)
            
                if lane(cars2[i],2) == 1:
                    crash = pygame.mixer.Sound('crash.wav')
                    crash.play()
                    x=403
                    y=display_height-90
                elif lane(cars2[i],2)==2:
                    crash = pygame.mixer.Sound('crash.wav')
                    crash.play()
                    x2=403
                    y2=60

            #handles movement for lane 3/2 cars
            for i in range(len(cars3)):
                cars3[i]+=0.4
                if cars3[i]>display_width+100:
                    cars3[i]=-150
                lane(cars3[i],3)
            
                if lane(cars3[i],3) == 1:
                    crash = pygame.mixer.Sound('crash.wav')
                    crash.play()
                    x=403
                    y=display_height-90
                elif lane(cars3[i],3)==2:
                    crash = pygame.mixer.Sound('crash.wav')
                    crash.play()
                    x2=403
                    y2=60

            #handles movement for lane 4/1 lanes
            for i in range(len(cars4)):
                cars4[i]-=1
                if cars4[i]<-180:
                    cars4[i]=900
                lane(cars4[i],4)
            
                if lane(cars4[i],4) == 1:
                    crash = pygame.mixer.Sound('crash.wav')
                    crash.play()
                    x=403
                    y=display_height-90
                elif lane(cars4[i],4)==2:
                    crash = pygame.mixer.Sound('crash.wav')
                    crash.play()
                    x2=403
                    y2=60

            #handles log 1 movement
            for i in range(len(logs)):
                #speed of log
                logs[i]+=0.9
                #creates the endless loop if it goes offscreen
                if logs[i]>display_width+125:
                    logs[i]=-150
                #sends the log's x value to the drawing functions
                lane(logs[i],5)

                #3 is one player on log, 4 is other player, 2 is two players. Functions moves either 1 or 2 players by set value to move with log
                if lane(logs[i],5) == 3:
                    x+=0.18
                elif lane(logs[i],5)==4:
                    x2+=0.18
                elif lane(logs[i],5)==2:
                    x2+=0.18
                    x+=0.18

            #handles log 2 movement
            for i in range(len(logs2)):
                logs2[i]-=1.5
                if logs2[i]<-125:
                    logs2[i]=1150
                lane(logs2[i],6)
                if lane(logs2[i],6) == 3:
                    x-=0.5
                elif lane(logs2[i],6)==4:
                    x2-=0.5
                elif lane(logs2[i],6) == 2:
                    x-=0.5
                    x2-=0.5

            #handles log 3 movement
            for i in range(len(logs3)):
                logs3[i]+=1.2
                if logs3[i]>display_width+125:
                    logs3[i]=-200
                lane(logs3[i],7)
                if lane(logs3[i],7) == 3:
                    x+=0.3
                elif lane(logs3[i],7)==4:
                    x2+=0.3
                elif lane(logs3[i],7) == 2:
                    x+=0.3
                    x2+=0.3

            #handles log 4 movement
            for i in range(len(logs4)):
                logs4[i]-=1
                if logs4[i]<-125:
                    logs4[i]=980
                lane(logs4[i],8)
                if lane(logs4[i],8) == 3:
                    x-=0.2
                elif lane(logs4[i],8)==4:
                    x2-=0.2
                elif lane(logs4[i],8) == 2:
                    x-=0.2
                    x2-=0.2
                    
            #changes the sprite of the frog depending on the direction it is facing  
            if dir_1==1:
                p1=pygame.image.load('frog.png')
                DISPLAY.blit(p1,(x,y))
            elif dir_1==2:
                p1=pygame.image.load('frogdown.png')
                DISPLAY.blit(p1,(x,y))
            elif dir_1==3:
                p1=pygame.image.load('frogleft.png')
                DISPLAY.blit(p1,(x,y-6))
            elif dir_1==4:
                p1=pygame.image.load('frogright.png')
                DISPLAY.blit(p1,(x,y-6))

            if dir_2==1:
                p2=pygame.image.load('frog2up.png')
                DISPLAY.blit(p2,(x2,y2))
            elif dir_2==2:
                p2=pygame.image.load('frog2.png')
                DISPLAY.blit(p2,(x2,y2))
            elif dir_2==3:
                p2=pygame.image.load('frog2left.png')
                DISPLAY.blit(p2,(x2,y2-6))
            elif dir_2==4:
                p2=pygame.image.load('frog2right.png')
                DISPLAY.blit(p2,(x2,y2-6))

            #if frogs cross either side or screen due to logs, respawn
            if x2>display_width or x2<0:
                    splash = pygame.mixer.Sound('SPLASH3.wav')
                    splash.play()
                    x2=403
                    y2=60
            elif x>display_width or x<0:
                    splash = pygame.mixer.Sound('SPLASH3.wav')
                    splash.play()
                    x=403
                    y=display_height-90

            #handles misallignment when leaving logs. checks all 50px markers and checks which is closest.
            #when it finds out which is closest, it will make its x equal to that to reallign to 50px markers
            if y==560 or y==310:
                snap = [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853]
                subs = []
                for i in snap:
                    subs.append(abs(x-i))
                x=snap[subs.index(min(subs))]

            #handles player 2 reallignment
            elif y2==560 or y2==310:
                snap = [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853]
                subs = []
                for i in snap:
                    subs.append(abs(x2-i))
                x2=snap[subs.index(min(subs))]
                
            #attack handling. checks if player is one block to the left or right of the other
            if x==x2+50 and y==y2 or x==x2-50 and y==y2:
                #checks for keypress
                if event.type == pygame.KEYDOWN:
                    #checks for spacebar
                    if event.key==pygame.K_SPACE:
                        #attack is ready at 500 charge, this sets the speed. takes about 5 seconds for full charge
                        charge+=4
                        
                    #different states of charge. will draw 20, 40, 60, 80 or 100% charge image above the player depending on charge value
                    if charge>0 and charge<201:
                        gc1 = pygame.image.load('gc1.png')
                        DISPLAY.blit(gc1, (x-5, y-25))
                        #creates a red border around to mimic health bar
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                    if charge>200 and charge<301:
                        gc2 = pygame.image.load('gc2.png')
                        DISPLAY.blit(gc2, (x-5, y-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                    if charge>300 and charge<401:
                        gc3 = pygame.image.load('gc3.png')
                        DISPLAY.blit(gc3, (x-5, y-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                    if charge>400 and charge<501:
                        gc4 = pygame.image.load('gc4.png')
                        DISPLAY.blit(gc4, (x-5, y-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                    if charge>500:
                        gc5 = pygame.image.load('gc5.png')
                        DISPLAY.blit(gc5, (x-5, y-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                        
                #when charge is 1000, cap it at 1000, then is attack key is released, set both players charges back to 0 and respawn opponent
                if charge>=500:
                    charge=500
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            #Plays a shooting sound, resets charges and respawns opponent
                            shoot = pygame.mixer.Sound('shoot.wav')
                            shoot.play()
                            charge=0
                            charge_red=0
                            if h1==True and h2==True and h3==False and h4==True and h5==True: 
                                x2=503
                                y2=60
                            else:
                                x2=403
                                y2=60

            #same attack code but checks for one block above or below
            elif y==y2-50 and x==x2 or y==y2+50 and x==x2:
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        charge+=4
                    if charge>0 and charge<101:
                        gc1 = pygame.image.load('gc1.png')
                        DISPLAY.blit(gc1, (x-5, y-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                    if charge>200 and charge<301:
                        gc2 = pygame.image.load('gc2.png')
                        DISPLAY.blit(gc2, (x-5, y-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                    if charge>300 and charge<401:
                        gc3 = pygame.image.load('gc3.png')
                        DISPLAY.blit(gc3, (x-5, y-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                    if charge>400 and charge<501:
                        gc4 = pygame.image.load('gc4.png')
                        DISPLAY.blit(gc4, (x-5, y-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                    if charge>500:
                        gc5 = pygame.image.load('gc5.png')
                        DISPLAY.blit(gc5, (x-5, y-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x-5, y-25, 50, 10), 2)
                if charge>=500:
                    charge=500
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            #Plays a shooting sound, resets charges and respawns opponent
                            shoot = pygame.mixer.Sound('shoot.wav')
                            shoot.play()
                            charge=0
                            charge_red=0
                            if h1==True and h2==True and h3==False and h4==True and h5==True: 
                                x2=503
                                y2=60
                            else:
                                x2=403
                                y2=60
                                
            #same attack code, handles for player 2
            if x2==x+50 and y2==y or x2==x-50 and y==y2:
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        charge_red+=4
                    if charge_red>100 and charge_red<201:
                        rc1 = pygame.image.load('gc1.png')
                        DISPLAY.blit(rc1, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                    if charge_red>200 and charge_red<401:
                        rc2 = pygame.image.load('gc2.png')
                        DISPLAY.blit(rc2, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                    if charge_red>300 and charge_red<401:
                        rc3 = pygame.image.load('gc3.png')
                        DISPLAY.blit(rc3, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                    if charge_red>400 and charge_red<501:
                        rc4 = pygame.image.load('gc4.png')
                        DISPLAY.blit(rc4, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                    if charge_red>500:
                        rc5 = pygame.image.load('gc5.png')
                        DISPLAY.blit(rc5, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                if charge_red>=500:
                    charge_red=500
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_q:
                            shoot = pygame.mixer.Sound('shoot.wav')
                            shoot.play()
                            charge_red=0
                            charge=0
                            if s1==True and s2==True and s3==False and s4==True and s5==True: 
                                x=503
                                y=display_height-90
                            else:
                                x=403
                                y=display_height-90
                            
            elif y2==y-50 and x==x2 or y2==y+50 and x==x2:
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        charge_red+=4
                    if charge_red>100 and charge_red<201:
                        rc1 = pygame.image.load('gc1.png')
                        DISPLAY.blit(rc1, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                    if charge_red>200 and charge_red<301:
                        rc2 = pygame.image.load('gc2.png')
                        DISPLAY.blit(rc2, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                    if charge_red>300 and charge_red<401:
                        rc3 = pygame.image.load('gc3.png')
                        DISPLAY.blit(rc3, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                    if charge_red>400 and charge_red<501:
                        rc4 = pygame.image.load('gc4.png')
                        DISPLAY.blit(rc4, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                    if charge_red>500:
                        rc5 = pygame.image.load('gc5.png')
                        DISPLAY.blit(rc5, (x2-5, y2-25))
                        pygame.draw.rect(DISPLAY, (255, 0, 0), (x2-5, y2-25, 50, 10), 2)
                if charge_red>=500:
                    charge_red=500
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_q:
                            shoot = pygame.mixer.Sound('shoot.wav')
                            shoot.play()
                            charge_red=0
                            charge=0
                            x=403
                            y=display_height-90

            # if all of player 1's holes are filled, exit game loop, display win page.
            if s1==True and s2==True and s3==True and s4==True and s5==True:
                    gameExit=True
                    #Fades out the ingame msic
                    ingame.fadeout(2000)
                    #Loads the victory theme
                    victory = pygame.mixer.Sound('victory.wav')
                    #Plays the victory theme
                    victory.play(-1, fade_ms=2000)
                    
                   #Creates hitboxes for exit and menu buttons for clicking
                    exit_hitbox = pygame.draw.rect(DISPLAY, (255, 255, 255, 0), (110, 670, 200, 100))
                    menu_hitbox = pygame.draw.rect(DISPLAY, (255, 255, 255, 0), (530, 670, 200, 100))

                    #Load the winscreen and blit to the display
                    endscreen = pygame.image.load("redwin.png")
                    DISPLAY.blit(endscreen, (0,0))

                    #Show the new contents
                    pygame.display.update()

                    #Waits on winscreen until a click on menu or exit
                    quitting = False
                    while not quitting:
                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    pos = pygame.mouse.get_pos()
                                    #Checks if they clicked the exit box, then closes pygame and the shell.
                                    if exit_hitbox.collidepoint(pos):
                                        pygame.quit()
                                        exit()
                                    #Calls the menu function and fades out the victory theme.
                                    elif menu_hitbox.collidepoint(pos):
                                        victory.fadeout(1500)
                                        menu()
                    
            #if all of player 2's holes are filles, exit game loop and display win page.
            elif h1==True and h2==True and h3==True and h4==True and h5==True:
                    gameExit=True
                    #Fades out the ingame msic
                    ingame.fadeout(2000)
                    #Loads the victory theme
                    victory = pygame.mixer.Sound('victory.wav')
                    #Plays the victory theme
                    victory.play(-1, fade_ms=2000)
                    
                    #Creates hitboxes for exit and menu buttons for clicking
                    exit_hitbox = pygame.draw.rect(DISPLAY, (255, 255, 255, 0), (110, 670, 200, 100))
                    menu_hitbox = pygame.draw.rect(DISPLAY, (255, 255, 255, 0), (530, 670, 200, 100))

                    #Load the winscreen and blit to the display
                    endscreen = pygame.image.load("greenwin.png")
                    DISPLAY.blit(endscreen, (0,0))

                    #Show the new contents
                    pygame.display.update()

                    #Waits on winscreen until a click on menu or exit
                    quitting = False
                    while not quitting:
                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    pos = pygame.mouse.get_pos()
                                    #Checks if they clicked the exit box, then closes pygame and the shell.
                                    if exit_hitbox.collidepoint(pos):
                                        pygame.quit()
                                        exit()
                                    #Calls the menu function and fades out the victory theme.
                                    elif menu_hitbox.collidepoint(pos):
                                        victory.fadeout(1500)
                                        menu()
            if x==x2 and y==y2:
                x2+=50
                
            #updates display
            pygame.display.update()

def menu():
        #loads the background menu picture
        bg=pygame.image.load("menubg.jpg")
        #loads the controls page image
        instructions = pygame.image.load("controls.png")
        #loads the return to menu button and scales it to a smaller size
        back = pygame.image.load("back.png")
        back = pygame.transform.scale(back, (45, 45))

        #Loads the title logo
        title = pygame.image.load('logo.png')

        #initializes the menu song andd plays it with a 3 second fade-in
        pygame.mixer.music.set_volume(0.8)
        menumusic = pygame.mixer.Sound('menumusic.wav')
        menumusic.play(-1, fade_ms=3000)

        #Sets up all text for Playing, controls, and exit
        myfont = pygame.font.SysFont('Trebuchet MS', 60)
        play_text = myfont.render('PLAY', False, (42, 222, 43))
        controls_text = myfont.render('CONTROLS', False, (42, 222, 43))
        exit_text = myfont.render('EXIT', False, (42, 222, 43))

        #Draws the background
        DISPLAY.blit(bg, (0,0))
        
        s = pygame.Surface((200,70))
        s.set_alpha(150)
        s.fill((0,0,0))
        
        s2 = pygame.Surface((300,70))
        s2.set_alpha(150)
        s2.fill((0,0,0))
        
        s3 = pygame.Surface((850,377))
        s3.set_alpha(150)
        s3.fill((178,228,112))
        
        DISPLAY.blit(s, (325,480))
        DISPLAY.blit(s2, (275,600))
        DISPLAY.blit(s, (325,720))
        DISPLAY.blit(s3, (0,0))

        #Draws the title
        DISPLAY.blit(title, (75, 30))
        
        #Draws the 3 buttons
        play = pygame.draw.rect(DISPLAY, (153, 24, 5), (325, 480, 200, 70), 8)
        controls = pygame.draw.rect(DISPLAY, (153, 24, 5), (275, 600, 300, 70), 8)
        exitgame = pygame.draw.rect(DISPLAY, (153, 24, 5), (325, 720, 200, 70), 8)

        #Draws text for play, controls and exit.
        DISPLAY.blit(play_text,(360,480))
        DISPLAY.blit(controls_text,(285,600))
        DISPLAY.blit(exit_text,(365,720))

        #Waits on menu until a click
        quitting=False
        while not quitting:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        
                        #If they click play, fade out menu music and start the game
                        if play.collidepoint(pos):
                            menumusic.fadeout(1500)
                            play_game()
                            
                        #if they click controls, load the controls page
                        elif controls.collidepoint(pos):
                            #gives the back to menu button a hitbox for clicking
                            back_hitbox = pygame.draw.rect(DISPLAY, (255, 255, 255, 0), (400, 2, 45, 45))

                            #Draws the instructions and back button
                            DISPLAY.fill((35,138,129))
                            DISPLAY.blit(instructions, (25,50))
                            DISPLAY.blit(back, (400,2))
                            
                            pygame.display.update()

                            #Waits for a click
                            quitting = False
                            while not quitting:
                                for event in pygame.event.get():
                                     if event.type == pygame.MOUSEBUTTONUP:
                                         pos = pygame.mouse.get_pos()
                                         #If they click back, fade out the music and return to menu.
                                         if back_hitbox.collidepoint(pos):
                                             menumusic.fadeout(1500)
                                             menu()
                                             
                        #if they click exit, close pygame and quit the python shell.
                        elif exitgame.collidepoint(pos):
                            pygame.quit()
                            exit()
menu()
