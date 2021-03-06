#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Group Project - pygame

@author: Zhenghao Hu; Duo Jin; Yixuan He
ID: alyzh4; alydj1; psxyh6

"""
import pygame
import os
import random
import time
# global variables
WIDTH = 900 # window width
HEIGHT = 500 # window height
hero1_hp=100 # healthy point
hero2_hp=200 
enmy_hp=100 
boss_hp=1000 
bullet_speed=10 # attack speed
bossbullet_speed=10 
hero1_speed=10 #speed of moviement
hero2_speed=6 
enemy1_speed=3
enemy2_speed=6
boss_speed=32 
wepon_atk=15 # attack power
wepon2_atk=20
wepon3_atk=8
score = 0 #points
# image
hero_image_name="Isaac.jpg"
hero2_image_name="Thorsten.png"
back_image="background.jpg"
back2_image="menu.png"
weapon_image="boomerang1.png"
weapon2_image="boomerang2.png"
weapon3_image="flame.png"
ENMY_image="monster1.png"
ENMY2_image="monster2.png"
boss_image="boss.png"
boom_image="boom.png"
# background music & effect sound
pygame.init()
pygame.mixer.music.load("bgm.mp3")
boomS = pygame.mixer.Sound("boom.wav")
hurtS = pygame.mixer.Sound("hurt.wav")
fail = pygame.mixer.Sound("fail.wav")
change = pygame.mixer.Sound("change.wav")
win = pygame.mixer.Sound("win.wav")
button = pygame.mixer.Sound("button.wav")
monster = pygame.mixer.Sound("monster.wav")
tree = pygame.mixer.Sound("tree.wav")

#------------------------------First Character----------------------------------------
class Hero(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(hero_image_name).convert_alpha()#load image
        self.image = pygame.transform.scale(self.image, (60, 60))#size
        #position
        self.rect=self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        #speed = 10
        self.vx = hero1_speed
        self.vy = hero1_speed
        self.bullets=pygame.sprite.Group()
        # Health Point = 100
        self.hp = hero1_hp
        
    # Vertcal movement / Boundary control          
    def update(self):
        if self.rect.centerx <= self.rect.width *2/ 3:
            self.rect.centerx = self.rect.width *2/ 3
        elif self.rect.x >= WIDTH- self.rect.width *2/ 3:
            self.rect.x = WIDTH - self.rect.width *2/ 3
        elif self.rect.y <=-self.rect.height *2/ 3:
            self.rect.y = -self.rect.height *2/ 3
        elif self.rect.y >= HEIGHT - self.rect.height *2/ 3:
            self.rect.y = HEIGHT - self.rect.height  *2/ 3
    
    # Healthy Point
    def hurt(self,DAM):
        self.hp-=DAM
    # Movement
    def up(self):
        self.rect.y -= self.vy
    def down(self):
        self.rect.y += self.vy
    def right(self):
        self.rect.x += self.vx
    def left(self):
        self.rect.x -= self.vx
    # Bullet control
    def fire(self,X,Y):
        self.bullet = weapon(X,Y)
        self.bullet.rect.x = self.rect.centerx 
        self.bullet.rect.y = self.rect.y+self.rect.height//2 
        self.bullets.add(self.bullet)
        
#---------------------------Second Character----------------------------------------
class  Hero2(Hero):#inherit hero class
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(hero2_image_name).convert_alpha()#load image
        self.image = pygame.transform.scale(self.image, (65, 70))# control scale
        #position
        self.rect=self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        #speed = 6
        self.vx = hero2_speed
        self.vy = hero2_speed
        self.bullets=pygame.sprite.Group()
        # Health Point = 200
        self.hp = hero2_hp
        
    # Bullet control
    def fire(self,X,Y):
        self.bullet = weapon2(X,Y)
        self.bullet.rect.x = self.rect.centerx 
        self.bullet.rect.y = self.rect.y+self.rect.height//2  
        self.bullets.add(self.bullet)
        
#---------------------------The Enemy of First Display --------------------------     
class Enemy1(pygame.sprite.Sprite):

    def __init__(self):
        self.speed=random.randint(5,20)#monster random show 
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(ENMY_image).convert_alpha()#load image
        self.image = pygame.transform.scale(self.image, (60, 60))#scale control
        # position of random
        self.rect=self.image.get_rect()
        self.rect.x = random.randint(self.rect.width, WIDTH - self.rect.width)
        self.rect.y = random.randint(self.rect.height, HEIGHT - self.rect.height)
        # Health Point = 100
        self.hp=enmy_hp

    def update(self):
        #The timeing of attack
        X=random.randint(-2,2)
        Y=random.randint(-2,2)
        self.rect.y -=enemy1_speed*Y
        self.rect.x -=enemy1_speed*X
        #enemy boundary control
        if self.rect.x > WIDTH-self.rect.width//4 or self.rect.x<self.rect.width//4:
            self.kill()
        if self.rect.y > HEIGHT-self.rect.height//4 or self.rect.y <self.rect.height//4:
            self.kill()


    def hurt(self,DAM):
        #reduce Healthy Point by hurt
        self.hp-=DAM
   
    def destory(self):
        boom=pygame.image.load(boom_image)#load destory image
        boom = pygame.transform.scale(boom, (30, 30))#scale control
        screen.blit(boom, (self.rect.x, self.rect.y))#display
        
#---------------------------The Enemy of Secoond Display --------------------------     
class Enemy2(Enemy1):#inherit Enemy1 class

    def __init__(self):
        self.speed=random.randint(5,20)#random display
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(ENMY2_image).convert_alpha()#load image
        self.image = pygame.transform.scale(self.image, (55, 55))#control scale
        #position of random
        self.rect=self.image.get_rect()
        self.rect.x = random.randint(self.rect.width, WIDTH - self.rect.width)
        self.rect.y = random.randint(self.rect.height, HEIGHT - self.rect.height)
        # set the enemy Health Point = 100
        self.hp=enmy_hp

    def update(self):
        #The timeing of attack
        X=random.randint(-2,2)
        Y=random.randint(-2,2)
        self.rect.y -=enemy2_speed*Y
        self.rect.x -=enemy2_speed*X
        #enemy boundary control
        if self.rect.x > WIDTH-self.rect.width//4 or self.rect.x<self.rect.width//4:
            self.kill()
        if self.rect.y > HEIGHT-self.rect.height//4 or self.rect.y <self.rect.height//4:
            self.kill()

            
#---------------------------Special Role - Boss--------------------------------     
class Boss(Enemy1):#inherit Enemy1 class

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(boss_image).convert_alpha()#load image
        self.image = pygame.transform.scale(self.image, (90, 90))#size
        #position
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT//2
        self.enmybullets=pygame.sprite.Group()
        #Healthy point
        self.hp=boss_hp

    def update(self):
        #random display
        Y=random.randint(-2,2)
        #attack
        if self.rect.y - boss_speed*Y <0:
            self.rect.y =  self.rect.height*2/ 3
        if self.rect.y - boss_speed*Y >HEIGHT:
            self.rect.y =HEIGHT - self.rect.height*2/ 3
        self.rect.y -=boss_speed*Y
        self.fire()
        
    def hurt(self,DAM):
        #minus HP by hurt
        self.hp-=DAM
   
    def destory(self):
        boom=pygame.image.load(boom_image)#load destory(boom) image
        boom = pygame.transform.scale(boom, (30, 30))#scale control
        screen.blit(boom, (self.rect.x, self.rect.y))#display     

    def fire(self):
        # bullet moviement
        self.bullet = weapon3()
        self.bullet.rect.x = self.rect.centerx - self.bullet.rect.width / 2
        self.bullet.rect.y = self.rect.y - self.bullet.rect.height
        self.enmybullets.add(self.bullet)
       
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(back_image)#load background
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))#scale control
        self.rect=self.image.get_rect()#get poistion
        
#------------------------------Character's Bullet Attack -------------------------------
#First Character         
class weapon(pygame.sprite.Sprite):
    
    def __init__(self,X,Y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(weapon_image) #load image
        self.image = pygame.transform.scale(self.image, (30, 30))#scale control
        #position
        self.rect=self.image.get_rect()
        self.x =X
        self.y =Y
        # set Attack Power
        self.ATK=wepon_atk
    
    def update(self):
    # clear the bullet 
        if self.x==0:
           self.rect.y -=bullet_speed*self.y
           if self.rect.y<=-self.rect.height or self.rect.y>HEIGHT:
              self.kill()# disappear
              
        if self.y==0:
           self.rect.x -=bullet_speed*self.x
           if self.rect.x<=-self.rect.width or self.rect.x>WIDTH:
              self.kill()# disappear
              
#Second Character
class weapon2(weapon):#inherit weapon class
    
     def __init__(self,X,Y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(weapon2_image)#load image
        self.image = pygame.transform.scale(self.image, (40, 40))#size
        #position
        self.rect=self.image.get_rect()
        self.x =X
        self.y =Y
        # set Attack Power
        self.ATK=wepon2_atk

class weapon3(weapon):#inherit weapon class
     def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(weapon3_image)#load image
        self.image = pygame.transform.scale(self.image, (40, 40))#size
        #position
        self.rect=self.image.get_rect()
        # set Attack Power
        self.ATK=wepon3_atk
     def update(self):
        # clear the bullet 
        self.rect.x +=bossbullet_speed
        if self.rect.x>WIDTH:
              self.kill()
# -----------------------------------Drawing scenario---------------------------------------
def process():
    
    global score
    # Detection of Bullet and enemy
    bullets_enemys_result = pygame.sprite.groupcollide(hero.bullets, enemys, True, False)
    # Gets value of the result of the collision event
    obj_enemys = bullets_enemys_result.values()
    # traverse values
    for enemy in obj_enemys:
        #hurt depend on weapon attack power
        enemy[0].hurt(hero.bullet.ATK)
        #HP of enemy <0
        if enemy[0].hp <= 0:
            # get 1 points
            score +=1
            #make the enemy disppear
            enemy[0].kill()
            enemy[0].destory()
            #Sound,Boom
            boomS.play()

    #The hero collided with the enemy
    hero_enemys_result = pygame.sprite.spritecollide(hero, enemys, False)
    if hero_enemys_result:
        for enemy in hero_enemys_result:
            #kill enemy by collided
                 enemy.hurt(100)
                 if enemy.hp<=0:
                    enemy.kill()
                    enemy.destory
                #hero lose 20 HP
                 hero.hurt(20) 
                 #Sound-"hurt"
                 hurtS.play()

    if boss.enmybullets:
        #collision detection
        bullet_result=pygame.sprite.spritecollide(hero,boss.enmybullets,False)
        if bullet_result:
           for bullet in bullet_result:
               bullet.kill()
               #hurt depend on weapon attack power
               hero.hurt(boss.bullet.ATK)
               #sound - "hurt"
               hurtS.play()
        #detection hero attack defence boss attack
        bulletcollide = pygame.sprite.groupcollide(hero.bullets,\
                                                   boss.enmybullets, True, True)
# -----------------------------------Time & Scripts---------------------------------------
#count the time
class timer(object):
    #use time.clock as a time counting tool
    def __init__(self):
        self.begin = True
        self.beginTime = 0
    # count
    def start(self):
        if self.begin:
            self.beginTime = time.clock()
            self.begin = False
        return time.clock() - self.beginTime
    # stop count
    def stop(self):
        self.stopTime = self.start()
        self.beginTime = 0
        self.begin = True
        return self.stopTime
# print the information of game going
def show(text):
    pygame.font.init()
    myFont = pygame.font.SysFont(pygame.font.get_default_font(),25)
    surf = myFont.render(text, False, pygame.Color("green"))
    screen.blit(surf,(0,0))
    
def show2(text):
    pygame.font.init()
    myFont = pygame.font.SysFont(pygame.font.get_default_font(),60)
    surf = myFont.render(text, False, pygame.Color("black"))
    screen.blit(surf,(WIDTH//7,HEIGHT//2)) 
#clean the screen
def clean_screen():
    boss.enmybullets.empty()  
    hero.kill()
    enemys.empty()
    hero.bullets.empty()
#chec if user can change hero
def check_nmuber_herobullets():
    if 0 <= len(hero.bullets) <= 30:
       return True
    else: 
       return False
#update objects   
def objectupdated():
    enemys.update()
    enemys.draw(screen)
    hero.bullets.update()
    hero.bullets.draw(screen)
    boss.enmybullets.update()
    boss.enmybullets.draw(screen)   
#------------------------------------Running the Game--------------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#caption
pygame.display.set_caption("Cowboys with dangerous")
#init
tk = timer()
times = 0
#menu image
menu = pygame.image.load(back2_image)#load
menu = pygame.transform.scale(menu, (WIDTH, HEIGHT))
# menu play background music
pygame.mixer.music.play(-1)

while True:
    
    #init
    numberofuse=1
    score = 0
    # effect sound; ensure run one time
    playsound = True 
    playsound2 =False
    my_font = pygame.font.SysFont("arial",50)
    # execute 
    hero = Hero(WIDTH//2, HEIGHT//2)
    bg= Background()
    group = pygame.sprite.Group()
    group.add(bg,hero)
    #enemys
    enemys=pygame.sprite.Group()
    boss= Boss()
    #time
    clock=pygame.time.Clock()  

    screen.blit(menu,(0,0))
    #filp the screen
    pygame.display.flip() 
    
    # mouse control
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
         break
    if e.type == pygame.MOUSEBUTTONDOWN :
        #Sound - Button
        button.play()
        #play the background again
        pygame.mixer.music.load("bgm.mp3")
        pygame.mixer.music.play(-1)
     
        while True:
           clock.tick(24)
           e = pygame.event.poll()
           if e.type == pygame.QUIT:
                break
#--------------------------------- Keyboard Control-------------------------------------------
           keys_list = pygame.key.get_pressed()
           if keys_list[pygame.K_UP]:
           # Move Up, reduce value y
             hero.up()
           if keys_list[pygame.K_DOWN]:
           # Move Down, increase value y
             hero.down()
           if keys_list[pygame.K_LEFT]:
           # Move Right, reduce value x
             hero.left()
           if keys_list[pygame.K_RIGHT]:
            # Move Left, increase value x
             hero.right()
             
           #Direction and Movement of Bullet 
           if keys_list[pygame.K_w]:
             if  check_nmuber_herobullets():
                   hero.fire(0,1)
           if keys_list[pygame.K_a]:    
              if  check_nmuber_herobullets():
                   hero.fire(1,0)
           if keys_list[pygame.K_s]: 
               if  check_nmuber_herobullets():
                   hero.fire(0,-1) 
           if keys_list[pygame.K_d]: 
               if check_nmuber_herobullets():
                   hero.fire(-1,0)  
           #press R; Hero 1 change to Hero 2
           if keys_list[pygame.K_r]: 
               #set the time of change
               if hero.hp>0 and numberofuse ==1:
                   change.play() 
                   numberofuse=0
                   hero = Hero2(hero.rect.centerx,hero.rect.y)
                   group.empty()              
                   group.add(bg,hero)
                   group.update()
                   group.draw(screen)

               
           # visualise the changes you just made
           pygame.display.flip() 
           group.update()
           group.draw(screen)
#------------------------Set the Diffcult level of game---------------------------------     
           #First enemy display below 30
           if times <= 20:
               if  len(enemys) <= 10:
                  enemy = Enemy1()
                  enemys.add(enemy)
           #boss display
           if times == 20:
               enemys.add(boss)
               monster.play()
               pygame.mixer.music.load("bgm2.mp3")
               pygame.mixer.music.play(-1)
           #increase enemy 1
           if times > 30:
               if  len(enemys) <= 25:
                  enemy = Enemy1()
                  enemys.add(enemy)
           #increase enemy 2       
           if times == 40:
              tree.play() 
           if times > 40:
               if  len(enemys) <=40:
                  enemy = Enemy2()
                  enemys.add(enemy)       
          
            #Win!
           if times >= 60 and hero.hp>0:
               #clean the screen
               clean_screen()
               pygame.mixer.music.pause()
               #show the Text
               show2("WINNER! Press Space to Restart!")
               if playsound:
                   #Sound - Win ensure play once
                   win.play()
                   playsound = False
               #next game
               if keys_list[pygame.K_SPACE]:
                   #Sound - Button
                   button.play()
                   break
           #Lost!
           if hero.hp <= 0:
               #clean the screen
               clean_screen()
               pygame.mixer.music.pause()
               #show the Text
               show2("FAILURE! Press Space to Restart!")
               if playsound:
                   #Sound - fail ensure play once
                   fail.play()
                   playsound = False   
               #The information of HP; TIME; POINT when running the game
               show("HP: 0, points: {}, time: {}s".format(score,str(times)))
               #next game
               if keys_list[pygame.K_SPACE]:
                   #Sound - Button
                   button.play()
                   break  
           objectupdated()
           # count the time
           times = int(tk.start())
           if hero.hp>0:
               
               show("HP: {}, points: {}, time: {}s".format(hero.hp,score,str(times)))
        
           #Execute 
           if times > 1: 
               process()
           pygame.display.update()
        if e.type == pygame.QUIT:
            break   
    times=0
    tk.stop()
pygame.quit() # for the rest of you.
os._exit(0)  # just for MacOs users