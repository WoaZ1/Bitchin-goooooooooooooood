import pygame, sys, os, math

from pygame.locals import *
from fractions import Fraction


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





pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

WIDTH = 1280
HEIGHT = 832
TILESIZE = 32
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pale King')




# LOADING SPRITES
ghostImg = pygame.image.load('Sprites/playerDown.png')
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
heart = pygame.image.load('Sprites/Heart.png')
noHeart = pygame.image.load('Sprites/NoHeart.png')
swipeU = pygame.image.load('Sprites/AttackU.png')
swipeL= pygame.image.load('Sprites/AttackL.png')
swipeD= pygame.image.load('Sprites/AttackD.png')
swipeR= pygame.image.load('Sprites/AttackR.png')
playerHurt = colorize(playerDown1, (255,255,255))

#Setting the initial sprite for the player
playerStill = playerDown1


# Num of objects
spikeNum = 2
ghostNum = 1

# Stage number
stage = 0



# Counters for timing abilities (this is used for animations and movement)
dashCount = 0
staminaCount = 0
attackStamCount = 0
attackCount = 0
hurtCount = 0


# Used as an easy way to time the player's walk animation and movement
walkCount = 0


# First Enemy Created, is a simple enemy that moves towards the player.
# Will move faster if farther away
class ghost (object):
    def __init__(self,x,y,act = False,hp = 10):
        self.ghostX = x
        self.ghostY = y

        #Is the enemy active? Default: False
        self.act = act

        #Hitbox of the enemy
        self.hitbox = pygame.Rect(self.ghostX-player.playerX, self.ghostY-player.playerY, 32,32)

        #If the player moves within this area, the enemy activates
        self.actBox = pygame.Rect(self.ghostX-player.playerX - 400, self.ghostY-player.playerY - 400,800,800)

        # X and Y velocities
        self.xVelo = 0
        self.yVelo = 0

        #Health
        self.maxHealth = hp
        self.health = hp

        #Is the enemy in the hurt animation
        self.hurt = False

        #Is the enemy invulnerable?
        self.invul = False
        
        #Can the enemy move or attack?
        self.con = False

        #Is the enemy dead?
        self.dead = False


        self.hurtVeloX = 0
        self.hurtVeloY = 0

        
        self.hurtCount = 0


    #Draws enemy
    def draw(self):
        SCREEN.blit(ghostImg,(self.ghostX - player.playerX, self.ghostY - player.playerY))


    #Moves enemy, uses velocities to make it easier to move the hitbox
    def move(self):
        if self.con == True:
            self.xVelo = (((player.playerX-self.ghostX) + WIDTH/2) / 20)
            self.yVelo = (((player.playerY-self.ghostY) + HEIGHT/2) / 20)


        if self.hurt == True:
            if self.hurtCount == 1:
                
                    
                self.hurtVeloX, self.hurtVeloY = player.playerX+WIDTH/2 - eval(ghostStr).ghostX, player.playerY+HEIGHT/2 - eval(ghostStr).ghostY

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
#                if eval(ghostStr).ghostX < 0:
#                    self.hurtVeloX = self.hurtVeloX*-1
#                if eval(ghostStr).ghostY < 0:
#                    self.hurtVeloY = self.hurtVeloY*-1
            self.xVelo = -1*self.hurtVeloX 
            self.yVelo = -1*self.hurtVeloY
            if self.hurtCount > 5:
                self.hurt = False
                self.hurtCount = 0
                self.con = True

        self.ghostX += self.xVelo
        self.ghostY += self.yVelo


    #Moves the hitbox and the activation box
    def update(self,x,y):

        self.hitbox.move_ip(x+self.xVelo,y+self.yVelo)
        self.actBox.move_ip(x+self.xVelo,y+self.yVelo)
        self.xVelo = 0
        self.yVelo = 0


    #Checks to see if the player is in the range to activate the enemy    
    def active(self):
        if pygame.Rect.colliderect(player.hitbox, self.actBox) == True and self.act == False:
            self.act = True
            self.con = True

    #Damages enemy
    def hurtf(self):

        self.health -= 1
        self.hurt = True
        self.con = False

    #If the enemy dies
    def kill(self):
        self.dead = True



        
#A spike tile, damages player
class spike (object):
    def __init__(self, x, y):
        self.spikeX = tileRound(x)
        self.spikeY = tileRound(y)
        self.hitbox = pygame.Rect(self.spikeX-player.playerX, self.spikeY-player.playerY, 64,64)


    def draw(self):
        SCREEN.blit(spikeImg,(self.spikeX - player.playerX, self.spikeY - 8 - player.playerY))

    def update(self,x,y):

        self.hitbox.move_ip(x,y)








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
        

    #Player Walking
    def Left(self):
        self.playerX -= 7
        
    def Right(self):
        self.playerX += 7
        
    def Up(self):
        self.playerY -= 7
    
    def Down(self):
        self.playerY += 7


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
        self.playerHurt = True
        self.playerCon = False
        
    #Returns player Pos
    def getPlayerPos(self):
        return self.playerX, self.playerY


#Things for testing
player = Player()
    
    
spike1 = spike(100,100)
spike2 = spike(150,100)


ghost1 = ghost(1500,200)


























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
        walkCount = 0

        
    #Seeing if the player get hurt for every spike
    for i in range (spikeNum):
        spikeStr = 'spike' + str(i+1)
        if pygame.Rect.colliderect(player.hitbox, eval(spikeStr).hitbox) == True and player.playerInvuln == False:
            player.hurt()

    #Stamina Regen

    if player.playerStam != player.playerMaxStam:
        staminaCount += 1
        if staminaCount == 20:
            player.playerStam += 1
            staminaCount = 0



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
        if hurtCount >= 20:
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
        if attackCount == 7:

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
        if attackCount == 7:
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
        if attackCount == 7:
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
        if attackCount == 7:
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


    #Gets newer player X and Y after the movement is finished

    playerX, playerY = player.getPlayerPos()


    # Moves the ghost
    
    for i in range (ghostNum):
        ghostStr = 'ghost' + str(i+1)

        if eval(ghostStr).act == True:

            eval(ghostStr).move()
        else:
            eval(ghostStr).active()


    # Updates the ghost's hitbox
    for i in range (ghostNum):
        ghostStr = 'ghost' + str(i+1)

        if eval(ghostStr).dead == False:

            eval(ghostStr).update(oldPlayerX-playerX,oldPlayerY-playerY)


            #Checking if player is touching a ghost
            if pygame.Rect.colliderect(player.hitbox, eval(ghostStr).hitbox) == True and player.playerInvuln == False:
                player.hurt()
                


            #Checking if ghost is hitting a sword hitbox

            if eval(ghostStr).invul == False:
                if pygame.Rect.colliderect(player.attackBoxU, eval(ghostStr).hitbox) == True:
                    eval(ghostStr).hurtf()
                if pygame.Rect.colliderect(player.attackBoxD, eval(ghostStr).hitbox) == True:
                    eval(ghostStr).hurtf()
                if pygame.Rect.colliderect(player.attackBoxL, eval(ghostStr).hitbox) == True:
                    eval(ghostStr).hurtf()
                if pygame.Rect.colliderect(player.attackBoxR, eval(ghostStr).hitbox) == True:
                    eval(ghostStr).hurtf()

            #Kills the ghost if health is 0
            if eval(ghostStr).health <= 0:
                eval(ghostStr).kill()

        if eval(ghostStr).hurt == True:
            eval(ghostStr).hurtCount += 1

            
            


    #Updating the spikes' positions on screen
    for i in range (spikeNum):
        spikeStr = 'spike' + str(i+1)

        eval(spikeStr).update(oldPlayerX-playerX,oldPlayerY-playerY)


    #If player is dead program closes
    if player.playerHealth == 0:
        restart_program()


# =================================================================================
    # DRAWING SHIT
# =================================================================================



    #Drawing all the spikes
    for i in range (spikeNum):
        spikeStr = 'spike' + str(i+1)
        eval(spikeStr).draw()

        
    #Drawing all the ghosts    
    for i in range (ghostNum):
        ghostStr = 'ghost' + str(i+1)
        if eval(ghostStr).dead == False:
            eval(ghostStr).draw()


    #Drawing the player in the middle of the screen
    SCREEN.blit(playerStill,(WIDTH/2 - 16,HEIGHT/2 - 16))


    #Drawing the player's stamina bar
    for i in range (player.playerMaxStam):
        if i < player.playerStam:
            SCREEN.blit(stamina,((WIDTH - 35*(i))-150,10))
        if i >= player.playerStam:
            SCREEN.blit(noStamina,((WIDTH - 35*(i))-150,10))


    #Drawing the player's health bar
    for i in range (player.playerMaxHealth):
        if i < player.playerHealth:
            SCREEN.blit(heart,( 5 + 80*(i), 10))
        if i >= player.playerHealth:
            SCREEN.blit(noHeart,( 5 + 80*(i), 10))


    #Updating the screen
    pygame.display.update()

    #Ticking the FPS
    fpsClock.tick(FPS)

