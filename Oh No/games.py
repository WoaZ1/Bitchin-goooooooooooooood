
import pygame, sys, os, math

from pygame.locals import *
from fractions import Fraction
import random


#Self Explanitory
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


#Used to change color of sprites
def colorize(image, newColor):
    image = image.copy()
    image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
    return image

#used to remove blank space in sprites
def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
#        target.blit(temp, location)
        return temp

def tileRound(x, base = 32):
    return int(base * round(float(x)/base))

def inWall(x,y,w,h):
    return False


fireBallNames = ['fireball1', 'fireball2', 'fireball3', 'fireball4']
fireballs = {}




pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

WIDTH = 1280
HEIGHT = 832
TILESIZE = 32
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pale King')




# LOADING SPRITES
ghostL = pygame.image.load('Sprites/ghostL.png')
ghostR = pygame.image.load('Sprites/ghostR.png')
playerDown1 = pygame.image.load('Sprites/playerDown.png')
playerDown2 = pygame.image.load('Sprites/playerDown2.png')
playerDownA = pygame.image.load('Sprites/playerADown.png')
playerUp1 = pygame.image.load('Sprites/playerUp.png')
playerUp2 = pygame.image.load('Sprites/playerUp2.png')
playerUpA = pygame.image.load('Sprites/playerAUp.png')
playerLeft1 = pygame.image.load('Sprites/playerLeft.png')
playerLeft2 = pygame.image.load('Sprites/playerLeft2.png')
playerLeftA = pygame.image.load('Sprites/playerALeft.png')
playerRight1 = pygame.image.load('Sprites/playerRight.png')
playerRight2 = pygame.image.load('Sprites/playerRight2.png')
playerRightA = pygame.image.load('Sprites/playerARight.png')
spikeImg = pygame.image.load('Sprites/Spike.png')
stamina = pygame.image.load('Sprites/Stam.png')
noStamina = pygame.image.load('Sprites/NoStam.png')
exStam = pygame.image.load('Sprites/ExStam.png')
heart = pygame.image.load('Sprites/Heart.png')
brokeHeart1 = pygame.image.load('Sprites/BrokeHeart1.png')
brokeHeart2 = pygame.image.load('Sprites/BrokeHeart2.png')
brokeHeart3 = pygame.image.load('Sprites/BrokeHeart3.png')
brokeHeart4 = pygame.image.load('Sprites/BrokeHeart4.png')
brokeHeart5 = pygame.image.load('Sprites/BrokeHeart5.png')
brokeHeart6 = pygame.image.load('Sprites/BrokeHeart6.png')
brokeHeart7 = pygame.image.load('Sprites/BrokeHeart7.png')
brokeHeart8 = pygame.image.load('Sprites/BrokeHeart8.png')
brokeHeart9 = pygame.image.load('Sprites/BrokeHeart9.png')
brokeHeart10 = pygame.image.load('Sprites/BrokeHeart10.png')
brokeHeartDie = pygame.image.load('Sprites/BrokeHeartDie.png')
chonk1 = pygame.image.load('Sprites/chonk00.png')
chonk2 = pygame.image.load('Sprites/chonk01.png')
chonk3 = pygame.image.load('Sprites/chonk02.png')
chonk4 = pygame.image.load('Sprites/chonk03.png')
chonk5 = pygame.image.load('Sprites/chonk04.png')
chonk6 = pygame.image.load('Sprites/chonk05.png')
chonk7 = pygame.image.load('Sprites/chonk06.png')
chonk8 = pygame.image.load('Sprites/chonk07.png')
chonk9 = pygame.image.load('Sprites/chonk08.png')
chonk10 = pygame.image.load('Sprites/chonk09.png')
chonk11 = pygame.image.load('Sprites/chonk10.png')
chonk12 = pygame.image.load('Sprites/chonk11.png')
chonk13 = pygame.image.load('Sprites/chonk12.png')
chonk14 = pygame.image.load('Sprites/chonk13.png')
chonk15 = pygame.image.load('Sprites/chonk14.png')
chonkL1 = pygame.image.load('Sprites/chonkL00.png')
chonkL2 = pygame.image.load('Sprites/chonkL01.png')
chonkL3 = pygame.image.load('Sprites/chonkL02.png')
chonkL4 = pygame.image.load('Sprites/chonkL03.png')
chonkL5 = pygame.image.load('Sprites/chonkL04.png')
chonkL6 = pygame.image.load('Sprites/chonkL05.png')
chonkL7 = pygame.image.load('Sprites/chonkL06.png')
chonkL8 = pygame.image.load('Sprites/chonkL07.png')
chonkL9 = pygame.image.load('Sprites/chonkL08.png')
chonkL10 = pygame.image.load('Sprites/chonkL09.png')
chonkL11 = pygame.image.load('Sprites/chonkL10.png')
chonkL12 = pygame.image.load('Sprites/chonkL11.png')
chonkL13 = pygame.image.load('Sprites/chonkL12.png')
chonkL14 = pygame.image.load('Sprites/chonkL13.png')
chonkL15 = pygame.image.load('Sprites/chonkL14.png')
fireballImg = pygame.image.load('Sprites/fireball.png')


chonkLAnim = [chonkL1,chonkL2,chonkL3,chonkL4,chonkL5,chonkL6,chonkL7,chonkL8,chonkL9,chonkL10,chonkL11,chonkL12,chonkL13,chonkL14,chonkL15]
chonkAnim = [chonk1,chonk2,chonk3,chonk4,chonk5,chonk6,chonk7,chonk8,chonk9,chonk10,chonk11,chonk12,chonk13,chonk14,chonk15]

swipeU = pygame.image.load('Sprites/AttackU.png')
swipeL= pygame.image.load('Sprites/AttackL.png')
swipeD= pygame.image.load('Sprites/AttackD.png')
swipeR= pygame.image.load('Sprites/AttackR.png')
playerHurt = colorize(playerDown1, (255,255,255))

#Setting the initial sprite for the player
playerStill = playerDown1


# Num of objects
tileNum = 0



enemyNum = 0
fireNum = 0



# Stage number
stage = 0


# Counters for timing abilities (this is used for animations and movement)
dashCount = 0
staminaCount = 0
attackStamCount = 0
attackCount = 0
hurtCount = 0
hitCount = 0


# Used as an easy way to time the player's walk animation and movement
walkCount = 0


#Used to keep track of all the enemies
class enemy (object):
    def __init__(self,x,y,act,hp):
        self.id = "pant"
        global enemyNum
        enemyNum += 1
        
        self.X = x
        self.Y = y


        #Health
        self.maxHealth = hp
        self.health = hp


        #Is the enemy in the hurt animation
        self.hurt = False


        #Is the enemy invulnerable?
        self.invul = False
        

        #Can the enemy move or attack?
        self.con = act


        #Is the enemy dead?
        self.dead = False


        self.hurtVeloX = 0
        self.hurtVeloY = 0

        
        self.hurtCount = 0

        # X and Y velocities
        self.xVelo = 0
        self.yVelo = 0



    #Draws enemy
    def draw(self):
        SCREEN.blit(self.Img,(self.X - player.playerX, self.Y - player.playerY))



        #Moves the hitbox and the activation box
    def update(self,x,y):
        if self.health == 0:
            self.dead = True

        if player.playerX +WIDTH/2 > self.X:
            self.Img = self.R
        else:
            self.Img = self.L

#        print self.X - player.playerX-x+self.X
#        print self.X

        self.hitbox.move_ip(x+self.X -self.oldX,y+self.Y - self.oldY)
        self.actBox.move_ip(x+self.X - self.oldX,y+self.Y - self.oldY) 


        self.hitbox.move_ip(self.X - player.playerX -self.hitbox.left,self.Y - player.playerY -self.hitbox.top)
        self.actBox.move_ip(self.X - player.playerX -self.hitbox.left,self.Y - player.playerY -self.hitbox.top)


        self.xVelo = 0
        self.yVelo = 0


        #Checks to see if the player is in the range to activate the enemy    
    def active(self):

        if pygame.Rect.colliderect(player.hitbox, self.actBox) == True and self.act == False:
            self.act = True
            self.con = True

        #If the enemy dies
    def kill(self):
        self.dead = True

    #Damages enemy
    def hurtf(self):
        if self.canHurt == True:
            self.health -= 1
            self.hurt = True
            self.con = False

    def hurtMove(self):

        if self.hurt == True and self.knockBack == True:
            try:
                if self.exhaustCount >= 100:
                    self.exhaustCount = 0
            except:
                pass
            self.hurtCount += 1
            if self.hurtCount == 1:
                self.hurtf()
                    
                self.hurtVeloX, self.hurtVeloY = player.playerX+WIDTH/2 - eval(enemyStr).X, player.playerY+HEIGHT/2 - eval(enemyStr).Y

                if self.hurtVeloY == 0:
                    self.hurtVeloY = 1
                if self.hurtVeloX == 0:
                    self.hurtVeloX = 1
                if abs(self.hurtVeloX) > abs(self.hurtVeloY):
                    self.hurtVeloX = self.hurtVeloX/abs(self.hurtVeloY)*10
                    self.hurtVeloY = self.hurtVeloY/abs(self.hurtVeloY)*10
                elif abs(self.hurtVeloY) > abs(self.hurtVeloX):
                    self.hurtVeloY = self.hurtVeloY/abs(self.hurtVeloX)*10
                    self.hurtVeloX = self.hurtVeloX/abs(self.hurtVeloX)*10

#                if eval(enemyStr).X < 0:
#                    self.hurtVeloX = self.hurtVeloX*-1
#                if eval(enemyStr).Y < 0:
#                    self.hurtVeloY = self.hurtVeloY*-1
            if self.hurtVeloX > 20:
                self.hurtVeloX = 20
            if self.hurtVeloX < -20:
                self.hurtVeloX = -20
            if self.hurtVeloY > 20:
                self.hurtVeloY = 20
            if self.hurtVeloY < -20:
                self.hurtVeloY = -20
            self.xVelo = -1*self.hurtVeloX 
            self.yVelo = -1*self.hurtVeloY

      
            if self.hurtCount > 5:
                self.hurt = False
                self.hurtCount = 0
                self.con = True

            
# First Enemy Created, is a simple enemy that moves towards the player.
# Will move faster if farther away            
class ghost (enemy):
    def __init__(self,x,y,act = False,hp = 3):


        enemy.__init__(self,x,y,act,hp)
        #Is the enemy active? Default: False
        self.act = act
        self.knockBack = True

        self.id = 'ghost'

        #Hitbox of the enemy
        self.hitbox = pygame.Rect(self.X-player.playerX, self.Y-player.playerY, 32,32)

        #If the player moves within this area, the enemy activates
        self.actBox = pygame.Rect(self.X-player.playerX - 400, self.Y-player.playerY - 400,800,800)


        self.L = ghostL
        self.R = ghostR
        
        self.canHurt = True

        self.speed = 8


        self.oldX = self.X
        self.oldY = self.Y
        
        self.Img = ghostL






        #Moves enemy, uses velocities to make it easier to move the hitbox
    def move(self):
        self.oldX = self.X
        self.oldY = self.Y
        if self.con == True:


            
            dx = player.playerX + WIDTH/2 -16- self.X
            dy = player.playerY + HEIGHT/2 -16- self.Y
           
            angle = math.atan2(dy, dx)

            if dx > 0:
                self.L = ghostL
            if dx < 0:
                self.R = ghostR

            self.xVelo = (self.speed*math.cos(angle))
            self.yVelo = (self.speed*math.sin(angle))

        if self.hurt == True:   
            self.hurtMove()

        


        print self.xVelo, self.yVelo
        self.X += self.xVelo
        self.Y += self.yVelo



class charger (enemy):
    def __init__(self,x,y,act = False,hp = 7):


        enemy.__init__(self,x,y,act,hp)
        #Is the enemy active? Default: False
        self.act = act
        self.knockBack = True

        #Hitbox of the enemy
        self.hitbox = pygame.Rect(self.X-player.playerX, self.Y-player.playerY, 64,64)

        #If the player moves within this area, the enemy activates
        self.actBox = pygame.Rect(self.X-player.playerX - 400, self.Y-player.playerY - 400,800,800)


        self.L = chonkL1
        self.R = chonk1

        self.canHurt = True

        self.dashCount = 0

        self.speed = 4

        self.Img = chonkL1

        self.exhaustCount = 50

        self.chargeAngle = 0
        self.oldX = self.X
        self.oldY = self.Y


    def move(self):



        if player.playerX + WIDTH/2-16 - self.X < 0 and self.dashCount < 20 and self.exhaustCount != 0:
            try:
                self.L = chonkLAnim[self.dashCount]
            except:
                pass
        if player.playerX + WIDTH/2-16 - self.X > 0 and self.dashCount < 20 and self.exhaustCount != 0:
            try:
                self.R = chonkAnim[self.dashCount]
            except:
                pass
            
        self.oldX = self.X
        self.oldY = self.Y
        
        if self.con == True and abs(player.playerX)-abs(self.X)+abs(player.playerY)-abs(self.Y)>= 500 or self.con == True and self.exhaustCount <= 100:
            self.exhaustCount += 1

            dx = player.playerX + WIDTH/2 -16- self.X
            dy = player.playerY + HEIGHT/2 -16- self.Y
           
            angle = math.atan2(dy, dx)

            if dx > 0:
                self.L = chonkL1
            if dx < 0:
                self.R = chonk1

            
            self.xVelo = (self.speed*math.cos(angle))
            self.yVelo = (self.speed*math.sin(angle))
        elif self.hurt == False:
            self.con = False
            self.dashCount += 1

                
            if self.dashCount == 20:

                dx = player.playerX + WIDTH/2-16 - self.X
                dy = player.playerY + HEIGHT/2-16 - self.Y
           
                self.chargeAngle = math.atan2(dy, dx)
            if self.dashCount > 20 and self.dashCount < 35:
                self.xVelo = ((self.speed*10)*math.cos(self.chargeAngle))
                self.yVelo = ((self.speed*10)*math.sin(self.chargeAngle))
            if self.dashCount > 40:
                self.dashCount = 0
                self.con = True
                self.exhaustCount = 0
        else:
            pass
                

        self.hurtMove()


        self.X += self.xVelo
        self.Y += self.yVelo



class mage(enemy):
    def __init__(self,x,y,act = False,hp = 2):


        enemy.__init__(self,x,y,act,hp)
        #Is the enemy active? Default: False
        self.act = act
        self.knockBack = True

        #Hitbox of the enemy
        self.hitbox = pygame.Rect(self.X-player.playerX, self.Y-player.playerY, 32,32)
        self.w = 32
        self.h = 32

        #If the player moves within this area, the enemy activates
        self.actBox = pygame.Rect(self.X-player.playerX - 400, self.Y-player.playerY - 400,800,800)

        self.mode = 0

        self.teleCount = 0
        self.fireCount = 0

        self.canHurt = True

        self.L = ghostL
        self.R = ghostR
        self.oldX = self.X
        self.oldY = self.Y


    def move(self):
        if self.dead == False:
            self.oldX = self.X
            self.oldY = self.Y
            if self.con == True:
                if self.mode == 0:
                    self.fireCount += 1

                    if self.fireCount == 45:
                        self.fire()
                        self.fireCount = 0
                        self.mode = 1
                if self.mode == 1:
                    self.teleCount += 1
                    
                    if self.teleCount == 50:
                        
                        self.tele()
                        self.teleCount = 0
                        self.mode = 0

            

            self.hurtMove()

            self.X += self.xVelo
            self.Y += self.yVelo
        
    def fire(self):
        global fireNum
        dx = player.playerX + WIDTH/2-16 - self.X
        dy = player.playerY + HEIGHT/2-16 - self.Y
           
        self.angle = math.atan2(dy, dx)
        for i in range (3):
            fireNum += 1
            fireballs['fireball'+str(fireNum)] = fireball(self.X,self.Y,self.angle + float(i)/float(5)- 0.2)
        
       

    def tele(self):
        while True:
            a, b = (random.randint(-600,600),random.randint(-400,400))
            if inWall (a,b,self.w,self.h) == False:
                self.X += a
                self.Y += b
                break
    

class fireball(object):
    def __init__(self,x,y,angle,speed = 15):
        self.Img = fireballImg
        self.X = x
        self.Y = y
        self.xVelo = 0
        self.yVelo = 0
        self.oldX = self.X
        self.oldY = self.Y
        self.speed = speed
        self.angle = angle
        self.hitbox = pygame.Rect(self.X-player.playerX, self.Y-player.playerY, 16,16)

    def move(self):

        self.oldX = self.X
        self.oldY = self.Y
        
        self.xVelo = ((self.speed)*math.cos(self.angle))
        self.yVelo = ((self.speed)*math.sin(self.angle))

        self.X += self.xVelo
        self.Y += self.yVelo

    def update(self,x,y):


        self.hitbox.move_ip(x+self.X -self.oldX,y+self.Y - self.oldY)


        self.hitbox.move_ip(self.X - player.playerX -self.hitbox.left,self.Y - player.playerY -self.hitbox.top)


        self.xVelo = 0
        self.yVelo = 0
        
    def draw(self):
        SCREEN.blit(self.Img,(self.X - player.playerX, self.Y - player.playerY))    

class tile (object):
    def __init__(self,x,y):
        
        global tileNum
        tileNum += 1
        
        self.X = tileRound(x)
        self.Y = tileRound(y)
        self.hurts = False

    def draw(self):
        SCREEN.blit(self.img,(self.X - player.playerX, self.Y - 8 - player.playerY))

    def update(self,x,y):

        self.hitbox.move_ip(x,y)
        
#A spike tile, damages player
class spike (tile):
    def __init__(self, x, y):
        tile.__init__(self,x,y)
        self.hitbox = pygame.Rect(self.X-player.playerX, self.Y-player.playerY, 64,64)
        self.img = spikeImg
        self.hurts = True













# This was the first thing I made for this project but at the time of commenting I realize this class has basically no use, at this point it is tied in with the main program and it would be a hastle to remove it
class Player(object):
    
    def __init__(self):
        self.playerX = 0
        self.playerY = 0
        
        #Does the player have control?
        self.playerCon = True
        
        #Which way is the player moving?
        self.playerMoveLeft = False
        self.playerMoveRight = False
        self.playerMoveUp = False
        self.playerMoveDown = False

        #Is the player dashing? 
        self.playerDash = False

        #Which way is the player dashing?
        self.playerDashLeft = False
        self.playerDashRight = False
        self.playerDashUp = False
        self.playerDashDown = False

        #player stamina counts
        self.playerMaxStam = 3
        self.playerStam = self.playerMaxStam

        #Which way is the player facing?
        self.playerFace = 'D'

        #player health counts
        self.playerMaxHealth = 5
        self.playerHealth = 5
        self.playerTempHealth = 0
        self.playerBrokeHealth = 0

        #Which way is the player attacking?
        self.playerAttackU = False
        self.playerAttackL = False
        self.playerAttackD = False
        self.playerAttackR = False

        #Is the player being hurt?
        self.playerHurt = False

        #Is the player invulnerable?
        self.playerInvuln = False

        #Which way was the player facing when he was last hurt?
        self.playerHurtFace = 'D'

        #Player's Hitbox
        self.hitbox = pygame.Rect(WIDTH/2 - 16,HEIGHT/2 - 16,32,32)

        #Hitbox For attacks, Is far off screen but gets moved to correct position when the player attacks.
        self.attackBoxU = pygame.Rect(-50040,-50055, 80, 20)
        self.attackBoxD = pygame.Rect(-50035,-50020, 80, 20)
        self.attackBoxL = pygame.Rect(-50055,-50045, 20, 80)
        self.attackBoxR = pygame.Rect(-49975,-50040, 20, 80)

        self.speed = 7


        self.brokeBoys = False
        self.brokeCount = 0
        self.brokePiece = 1

        self.brokeDie = False
        self.brokeDieCount = 0
        

    #Player Walking
    def Left(self):
        self.playerX -= player.speed
        
    def Right(self):
        self.playerX += player.speed
        
    def Up(self):
        self.playerY -= player.speed
    
    def Down(self):
        self.playerY += player.speed


    #Player Dashing
    def dashL(self):
        self.playerX -= 40
        self.playerCon = False
        
    def dashR(self):
        self.playerX += 40
        self.playerCon = False
        
    def dashU(self):
        self.playerY -= 40
        self.playerCon = False
        
    def dashD(self):
        self.playerY += 40
        self.playerCon = False

    #Player Attacking
    def attackU(self):
        SCREEN.blit(swipeU,(WIDTH/2 - 16 -50,HEIGHT/2 - 16 - 80))
        self.playerCon = False
    def attackL(self):
        SCREEN.blit(swipeL,(WIDTH/2 - 16 -80,HEIGHT/2 - 16 - 50))
        self.playerCon = False
    def attackD(self):
        SCREEN.blit(swipeD,(WIDTH/2 - 16 -50,HEIGHT/2 - 16-20))
        self.playerCon = False
    def attackR(self):
        SCREEN.blit(swipeR,(WIDTH/2 - 16 -10,HEIGHT/2 - 16 - 50))
        self.playerCon = False

    #Player got hurt
    def hurt(self):
        self.playerHurtFace = self.playerFace
        self.playerHealth -= 1
        self.playerInvuln = True
        self.playerHurt = True
        self.playerCon = False
        self.brokeBoys = True
        self.brokePiece = 1
        if self.playerStam < 1:
            self.playerStam = 1
        
    #Returns player Pos
    def getPlayerPos(self):
        return self.playerX, self.playerY

    def hit(self):
        self.playerStam += 1
        if self.brokeBoys == True:
            self.brokePiece += 1
        


#Things for testing
player = Player()
    
    
tile1 = spike(100,100)
tile2 = spike(150,100)


#enemy1 = mage(1500,200)
#enemy2 = charger(1500,200)
enemy1 = ghost(1500,200)



























while True:  #Main

    #BLACK BACKGROUND
    SCREEN.fill((0,0,0))

# =================================================================================
    #PLAYER INPUT
# =================================================================================

    #Getting player X and Y at beginning of frame for reference of where the camera moves
    oldPlayerX, oldPlayerY = player.getPlayerPos()


    # Getting user input
    for event in pygame.event.get():

        #If user presses the X he quits
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        #Moving the player and detecting when key is released
        if event.type == KEYDOWN:
                if event.key == K_a:
                    player.playerMoveLeft = True
                    player.playerFace = 'L'
                if event.key == K_d:
                    player.playerMoveRight = True
                    player.playerFace = 'R'
                if event.key == K_w:
                    player.playerMoveUp = True
                    player.playerFace = 'U'
                if event.key == K_s:
                    player.playerMoveDown = True
                    player.playerFace = 'D'
                    
        if event.type == KEYUP:
            if event.key == K_a:
                player.playerMoveLeft = False
            if event.key == K_d:
                player.playerMoveRight = False
            if event.key == K_w:
                player.playerMoveUp = False
            if event.key == K_s:
                player.playerMoveDown = False



        #If the player has control
        if player.playerCon == True:


            
            #Getting user input for attacking
            if event.type == KEYDOWN:

                
                if event.key == K_j and player.playerFace == 'U':
                    player.playerAttackU = True
                if event.key == K_j and player.playerFace == 'L':
                    player.playerAttackL = True
                if event.key == K_j and player.playerFace == 'D':
                    player.playerAttackD = True
                if event.key == K_j and player.playerFace == 'R':
                    player.playerAttackR = True


                #If stamina is > 0, dash is possible
                if player.playerStam > 0:
                    if event.key == K_k and player.playerMoveLeft == True:
                        dashCount = 1
                        player.playerDashLeft = True
                    if event.key == K_k and player.playerMoveRight == True:
                        dashCount = 1
                        player.playerDashRight = True
                    if event.key == K_k and player.playerMoveUp == True:
                        dashCount = 1
                        player.playerDashUp = True
                    if event.key == K_k and player.playerMoveDown == True:
                        dashCount = 1
                        player.playerDashDown = True



# =================================================================================
    # GAME LOGIC
# =================================================================================

    #A main counter for the player's walking animation and movement
    walkCount += 1
    if walkCount == 25:
        player.speed = 7
        walkCount = 0

        
    #Seeing if the player get hurt for every spike
    for i in range (tileNum):
        tileStr = 'tile' + str(i+1)
        if eval(tileStr).hurts == True:
            if pygame.Rect.colliderect(player.hitbox, eval(tileStr).hitbox) == True and player.playerInvuln == False:
                player.hurt()

    #Stamina Regen

    if player.playerStam < player.playerMaxStam:
        staminaCount += 1
        if staminaCount == 60:
            player.playerStam += 1
            staminaCount = 40
    if player.playerStam > player.playerMaxStam:
        staminaCount += 1
        if staminaCount == 60:
            player.playerStam -= 1
            staminaCount = 40


    #If the player gets hurt
    if player.playerHurt == True:
        if hurtCount == 0:
            #Saving a copy of the current player sprite
            playerStillCopy = playerStill
        #Player is invulnerable shortly after being hit
        player.playerInvuln = True
        hurtCount += 1

        #Modulo of hurtCount for animation
        if hurtCount%2 != 0:
            playerStill = colorize(playerStill, (255,255,255))
        else:
            playerStill = playerStillCopy


        #Pushes the player backwards when hit
        if hurtCount < 10:
            if player.playerHurtFace == 'U':
                player.playerY += 10
            if player.playerHurtFace == 'R':
                player.playerX -= 10
            if player.playerHurtFace == 'D':
                player.playerY -= 10
            if player.playerHurtFace == 'L':
                player.playerX += 10

        #Lets player regain control before losing their invulnerability
        if hurtCount >= 10:
            player.playerCon = True


        #Player loses invulnerability
        if hurtCount >= 40:
            player.playerInvuln = False
            player.playerHurt = False
            hurtCount = 0

            
            
        


    #PLAYER ATTACKING, WILL ONLY EXPLAIN FIRST ONE BECAUSE ALL ARE THE SAME
    if player.playerAttackU == True:
        
        #Only does this once at beginning of swing
        if attackCount ==0:
            
            #Saves the last player Sprite
            playerStillCopy = playerStill
            
            #Moves the Sword's Hitbox to the proper position and saves a reverse sword movement to put it back
            swordMovement = (-(WIDTH/2+50000), -(HEIGHT/2+50000))
            player.attackBoxU.move_ip(WIDTH/2+50000,HEIGHT/2+50000)

            #Puts the player in the swinging sprite
            playerStill = playerUpA


        #Right after the beginning of swing puts sword hitbox back offscreen
        if attackCount == 1:
            player.attackBoxU.move_ip(swordMovement)

        #In the middle of the animation reverts player sprite back to normal
        if attackCount == 3:
            playerStill = playerStillCopy

        
        player.attackU()
        attackCount += 1


        #At the end of attack
        if attackCount == 10:

            #Player regains control
            player.playerCon = True
            attackCount = 0
            player.playerAttackU = False

            #Allows the player to walk right away after attacking
            walkCount = 0
            
    if player.playerAttackL == True:
        if attackCount ==0:
            swordMovement = (-(WIDTH/2+50000), -(HEIGHT/2+50000))
            player.attackBoxL.move_ip(WIDTH/2+50000,HEIGHT/2+50000)
            playerStillCopy = playerStill
            playerStill = playerLeftA
        if attackCount == 1:
            player.attackBoxL.move_ip(swordMovement)
        if attackCount == 3:
            playerStill = playerStillCopy
        player.attackL()
        attackCount += 1
        if attackCount == 10:
            player.playerCon = True
            attackCount = 0
            player.playerAttackL = False
            walkCount = 0
            
    if player.playerAttackD == True:
        if attackCount ==0:
            swordMovement = (-(WIDTH/2 -10+50000),-(HEIGHT/2 +50 +50000))
            player.attackBoxD.move_ip(WIDTH/2 -10+50000,HEIGHT/2 +50 +50000)
            playerStillCopy = playerStill
            playerStill = playerDownA
        if attackCount == 1:
            player.attackBoxD.move_ip(swordMovement)
        if attackCount == 3:
            playerStill = playerStillCopy
        player.attackD()
        attackCount += 1
        if attackCount == 10:
            player.playerCon = True
            attackCount = 0
            player.playerAttackD = False
            walkCount = 0

            
    if player.playerAttackR == True:
        if attackCount ==0:
            swordMovement = (-(WIDTH/2 + 16+50000),-(HEIGHT/2+50000))
            player.attackBoxR.move_ip(WIDTH/2 + 16+50000,HEIGHT/2+50000)
            playerStillCopy = playerStill
            playerStill = playerRightA
        if attackCount == 1:
            player.attackBoxR.move_ip(swordMovement)
        if attackCount == 3:
            playerStill = playerStillCopy
        player.attackR()
        attackCount += 1
        if attackCount == 10:
            player.playerCon = True
            attackCount = 0
            player.playerAttackR = False
            walkCount = 0






        

    #DASH COUNTER

    if dashCount > 0:
        if dashCount == 1:
            playerStillCopy = playerStill
            
        #Making the character slightly transparent while dashing
        playerStill = blit_alpha(SCREEN, playerStill, (100,100), 220)
        player.playerCon = False

        #Player is invulnerable while dashing
        player.playerInvuln = True
        dashCount += 1
        
        if dashCount > 6:
            player.playerStam -= 1
            player.playerDashLeft = False
            player.playerDashRight = False
            player.playerDashUp = False
            player.playerDashDown = False
            player.playerCon = True
            player.playerInvuln = False
            playerStill = playerStillCopy
            dashCount = 0
            walkCount = 0





    #ACTUALLY MOVING THE PLAYER

    #Moves the player while dashing
    if player.playerDashLeft == True:
        staminaCount = 0
        player.dashL()
    if player.playerDashRight == True:
        staminaCount = 0
        player.dashR()
    if player.playerDashUp == True:
        staminaCount = 0
        player.dashU()
    if player.playerDashDown == True:
        staminaCount = 0
        player.dashD()


    #Moves the player while walking and changes sprite to reflect said walking
    if player.playerCon == True:
        if player.playerMoveLeft == True:
            player.playerFace = 'L'
            if walkCount > 15 :
                playerStill = playerLeft1
            else:
                playerStill = playerLeft2
                player.Left()
        if player.playerMoveRight == True:
            player.playerFace = 'R'
            
            if walkCount>15 :
                playerStill = playerRight1
            else:
                playerStill = playerRight2
                player.Right()

        if player.playerMoveUp == True:
            player.playerFace = 'U'
            
            if walkCount > 15 :
                playerStill = playerUp1
            else:
                playerStill = playerUp2
                player.Up()
        if player.playerMoveDown == True:
            player.playerFace = 'D'
            if walkCount > 15 :
                playerStill = playerDown1
            else:
                playerStill = playerDown2
                player.Down()


    if player.brokeBoys == True:
        if player.brokePiece == 11:
            player.playerHealth += 1
            player.brokePiece = 1
    if player.playerHealth == player.playerMaxHealth:
        player.brokeBoys = False

    if player.playerHealth < player.playerMaxHealth - 2:
        player.brokeDie = True
        player.playerMaxHealth -= 1

        
    #Gets newer player X and Y after the movement is finished

    playerX, playerY = player.getPlayerPos()


    # Moves the enemy
    if fireNum < enemyNum:
        for i in range (enemyNum):
            enemyStr = 'enemy' + str(i+1)
            fireStr = 'fireball' + str(i + 1)

            if eval(enemyStr).act == True:

                eval(enemyStr).move()
            else:
                eval(enemyStr).active()

            try:
                fireballs['fireball'+str(i+1)].move()
            except:
                pass




            # Updates the enemy's hitbox

            if eval(enemyStr).dead == False:

                eval(enemyStr).update(oldPlayerX-playerX,oldPlayerY-playerY)


                #Checking if player is touching a enemy
                if pygame.Rect.colliderect(player.hitbox, eval(enemyStr).hitbox) == True and player.playerInvuln == False:
                    eval(enemyStr).health += 1
                    eval(enemyStr).hurtf()
                    player.hurt()
            try:
                fireballs['fireball'+str(i+1)].update(oldPlayerX-playerX,oldPlayerY-playerY)
                if pygame.Rect.colliderect(player.hitbox, fireballs['fireball'+str(i+1)].hitbox) == True and player.playerInvuln == False:
                    player.hurt()
            except:
                pass
    else:
        for i in range (fireNum):
            enemyStr = 'enemy' + str(i+1)
            fireStr = 'fireball' + str(i + 1)
            try:
                if eval(enemyStr).act == True:

                    eval(enemyStr).move()
                else:
                    eval(enemyStr).active()
            except:
                pass
            fireballs['fireball'+str(i+1)].move()

            try:
                if eval(enemyStr).dead == False:

                    eval(enemyStr).update(oldPlayerX-playerX,oldPlayerY-playerY)


                    #Checking if player is touching a enemy
                    if pygame.Rect.colliderect(player.hitbox, eval(enemyStr).hitbox) == True and player.playerInvuln == False:
                        eval(enemyStr).health += 1
                        eval(enemyStr).hurtf()
                        player.hurt()
            except:
                pass

            fireballs['fireball'+str(i+1)].update(oldPlayerX-playerX,oldPlayerY-playerY)
            if pygame.Rect.colliderect(player.hitbox, fireballs['fireball'+str(i+1)].hitbox) == True and player.playerInvuln == False:
                player.hurt()
                





                


            #Checking if enemy is hitting a sword hitbox
            try:
                if eval(enemyStr).invul == False:
                    if pygame.Rect.colliderect(player.attackBoxU, eval(enemyStr).hitbox) == True:
                        eval(enemyStr).hurtf()
                        player.hit()
                        if player.playerStam > player.playerMaxStam:
                            staminaCount = 0
                    if pygame.Rect.colliderect(player.attackBoxD, eval(enemyStr).hitbox) == True:
                        eval(enemyStr).hurtf()
                        player.hit()
                        if player.playerStam > player.playerMaxStam:
                            staminaCount = 0
                    if pygame.Rect.colliderect(player.attackBoxL, eval(enemyStr).hitbox) == True:
                        eval(enemyStr).hurtf()
                        player.hit()
                        if player.playerStam > player.playerMaxStam:
                            staminaCount = 0
                    if pygame.Rect.colliderect(player.attackBoxR, eval(enemyStr).hitbox) == True:
                        eval(enemyStr).hurtf()
                        player.hit()
                        if player.playerStam > player.playerMaxStam:
                            staminaCount = 0
            except:
                pass

            #Kills the enemy if health is 0
            try:
                if eval(enemyStr).health <= 0:
                    eval(enemyStr).kill()
            except:
                pass

        try:       
            if eval(enemyStr).hurt == True:
                eval(enemyStr).hurtCount += 1
        except:
            pass

            
            


    #Updating the tiles' positions on screen
    for i in range (tileNum):
        tileStr = 'tile' + str(i+1)

        eval(tileStr).update(oldPlayerX-playerX,oldPlayerY-playerY)


    #If player is dead program closes
    if player.playerHealth == 0:
        restart_program()


# =================================================================================
    # DRAWING SHIT
# =================================================================================



    #Drawing all the tiles
    for i in range (tileNum):
        tileStr = 'tile' + str(i+1)
        eval(tileStr).draw()

        
    #Drawing all the enemys
    if enemyNum > fireNum:
        for i in range (enemyNum):
            enemyStr = 'enemy' + str(i+1)
            if eval(enemyStr).dead == False:
                eval(enemyStr).draw()
            try:
                fireballs['fireball'+str(i+1)].draw()
            except:
                pass
    else:
        for i in range (fireNum):
            try:
                enemyStr = 'enemy' + str(i+1)
                if eval(enemyStr).dead == False:
                    eval(enemyStr).draw()
            except:
                pass
            fireballs['fireball'+str(i+1)].draw()


    #Drawing the player in the middle of the screen
    SCREEN.blit(playerStill,(WIDTH/2 - 16,HEIGHT/2 - 16))


    #Drawing the player's stamina bar
    if player.playerStam < player.playerMaxStam:
        for i in range (player.playerMaxStam):
            if i < player.playerStam:
                SCREEN.blit(stamina,((WIDTH - 35*(i))-150,10))
            if i >= player.playerStam:
                SCREEN.blit(noStamina,((WIDTH - 35*(i))-150,10))
    else:
        for i in range (player.playerStam):
            if i < player.playerMaxStam:
                SCREEN.blit(stamina,((WIDTH - 35*(i))-150,10))
            if i >= player.playerMaxStam:
                SCREEN.blit(exStam,((WIDTH - 35*(i))-150,10))


    #Drawing the player's health bar
    for i in range (player.playerMaxHealth):
        if i < player.playerHealth:
            SCREEN.blit(heart,( 5 + 80*(i), 10))
        elif player.brokeBoys == True and i== player.playerHealth:
            if player.brokePiece == 1:
                SCREEN.blit(brokeHeart1,( 5 + 80*(i), 10))
            if player.brokePiece == 2:
                SCREEN.blit(brokeHeart2,( 5 + 80*(i), 10))
            if player.brokePiece == 3:
                SCREEN.blit(brokeHeart3,( 5 + 80*(i), 10))
            if player.brokePiece == 4:
                SCREEN.blit(brokeHeart4,( 5 + 80*(i), 10))
            if player.brokePiece == 5:
                SCREEN.blit(brokeHeart5,( 5 + 80*(i), 10))
            if player.brokePiece == 6:
                SCREEN.blit(brokeHeart6,( 5 + 80*(i), 10))
            if player.brokePiece == 7:
                SCREEN.blit(brokeHeart7,( 5 + 80*(i), 10))
            if player.brokePiece == 8:
                SCREEN.blit(brokeHeart8,( 5 + 80*(i), 10))
            if player.brokePiece == 9:
                SCREEN.blit(brokeHeart9,( 5 + 80*(i), 10))
            if player.brokePiece == 10:
                SCREEN.blit(brokeHeart10,( 5 + 80*(i), 10))
        else:
            SCREEN.blit(brokeHeart1,( 5 + 80*(i), 10))
        if i == player.playerMaxHealth - 1 and player.brokeDie == True:
            SCREEN.blit(brokeHeartDie,( 5 + 80*(i+1) - 20, -10))
            player.brokeDieCount += 1
            if player.brokeDieCount == 10:
                player.brokeDie = False
                player.brokeDieCount = 0
            


    #Updating the screen
    pygame.display.update()

    #Ticking the FPS
    fpsClock.tick(FPS)

