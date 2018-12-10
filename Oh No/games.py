import pygame, sys, os

from pygame.locals import *

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def colorize(image, newColor):
    image = image.copy()
    image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
    return image


def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
#        target.blit(temp, location)
        return temp



pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

WIDTH = 1280
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pale King')


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


playerStill = playerDown1

spikeNum = 2
ghostNum = 1


stage = 0
dashCount = 0
staminaCount = 0
attackStamCount = 0
attackCount = 0
hurtCount = 0

mainCount = 0



class ghost (object):
    def __init__(self,x,y,act = False):
        self.ghostX = x
        self.ghostY = y
        self.act = act
        self.hitbox = pygame.Rect(self.ghostX-player.playerX, self.ghostY-player.playerY, 32,32)
        self.actBox = pygame.Rect(self.ghostX-player.playerX - 400, self.ghostY-player.playerY - 400,800,800)
        self.xVelo = 0
        self.yVelo = 0
        self.maxHealth = 2
        self.health = 1
        self.hurt = True
        self.con = False
        self.dead = False

    def draw(self):
        SCREEN.blit(ghostImg,(self.ghostX - player.playerX, self.ghostY - player.playerY))

    def move(self):
        self.xVelo = (((player.playerX-self.ghostX) + WIDTH/2) / 20) 

        self.ghostX += self.xVelo

        self.yVelo = ((player.playerY-self.ghostY) + HEIGHT/2) / 20

        self.ghostY += self.yVelo

    def update(self,x,y):
        
        self.hitbox.move_ip(x+self.xVelo,y+self.yVelo)
        self.actBox.move_ip(x+self.xVelo,y+self.yVelo)


    def active(self):
        if pygame.Rect.colliderect(player.hitbox, self.actBox) == True:
            self.act = True

    def hurtf(self):

        self.health -= 1
        self.hurt = True
        self.con = False


    def kill(self):
        self.dead = True



        

class spike (object):
    def __init__(self, x, y):
        self.spikeX = x
        self.spikeY = y
        self.hitbox = pygame.Rect(self.spikeX-player.playerX, self.spikeY-player.playerY, 64,64)

    def draw(self):
        SCREEN.blit(spikeImg,(self.spikeX - player.playerX, self.spikeY - 8 - player.playerY))

    def update(self,x,y):
        self.hitbox.move_ip(x,y)









class Player(object):
    
    def __init__(self):
        self.playerX = 0
        self.playerY = 0
        self.playerCon = True
        self.playerMoveLeft = False
        self.playerMoveRight = False
        self.playerMoveUp = False
        self.playerMoveDown = False
        self.playerDash = False
        self.playerDashLeft = False
        self.playerDashRight = False
        self.playerDashUp = False
        self.playerDashDown = False
        self.playerMaxStam = 3
        self.playerStam = self.playerMaxStam
        self.playerFace = 'D'
        self.playerMaxHealth = 5
        self.playerHealth = 5
        self.playerAttackU = False
        self.playerAttackL = False
        self.playerAttackD = False
        self.playerAttackR = False
        self.playerHurt = False
        self.playerInvuln = False
        self.playerHurtFace = 'D'
        self.hitbox = pygame.Rect(WIDTH/2 - 16,HEIGHT/2 - 16,32,32)
        self.attackBoxU = pygame.Rect(-50040,-49960, 100, 20)
        self.attackBoxD = pygame.Rect(-50000,-50000, 100, 20)
        self.attackBoxL = pygame.Rect(-50000,-50000, 20, 100)
        self.attackBoxR = pygame.Rect(-49975,-50040, 20, 80)
        

    def Left(self):
        self.playerX -= 7
        
    def Right(self):
        self.playerX += 7
        
    def Up(self):
        self.playerY -= 7
    
    def Down(self):
        self.playerY += 7

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

    def attackU(self):
        SCREEN.blit(swipeU,(WIDTH/2 - 16 -50,HEIGHT/2 - 16 - 80))
        self.attackBoxU.move_ip(WIDTH/2 - 16 -50,HEIGHT/2 - 16 - 80)
        self.playerCon = False
    def attackL(self):
        SCREEN.blit(swipeL,(WIDTH/2 - 16 -80,HEIGHT/2 - 16 - 50))
        self.attackBoxL.move_ip(WIDTH/2 - 16 -80,HEIGHT/2 - 16 - 50)
        self.playerCon = False
    def attackD(self):
        SCREEN.blit(swipeD,(WIDTH/2 - 16 -50,HEIGHT/2 - 16-20))
        self.playerCon = False
    def attackR(self):
        SCREEN.blit(swipeR,(WIDTH/2 - 16 -10,HEIGHT/2 - 16 - 50))
        self.playerCon = False

    def hurt(self):
        self.playerHurtFace = self.playerFace
        self.playerHealth -= 1
        self.playerHurt = True
        self.playerCon = False
        

    def getPlayerPos(self):
        return self.playerX, self.playerY

player = Player()
    
    
spike1 = spike(100,100)
spike2 = spike(200,200)


ghost1 = ghost(1500,200)


























while True:  #Main

    #BLACK BACKGROUND
    SCREEN.fill((0,0,0))

# =================================================================================
    #PLAYER INPUT
# =================================================================================
    oldPlayerX, oldPlayerY = player.getPlayerPos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



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
                    
        if player.playerCon == True:


            

            if event.type == KEYDOWN:

                
                if event.key == K_j and player.playerFace == 'U':
                    player.playerAttackU = True
                if event.key == K_j and player.playerFace == 'L':
                    player.playerAttackL = True
                if event.key == K_j and player.playerFace == 'D':
                    player.playerAttackD = True
                if event.key == K_j and player.playerFace == 'R':
                    player.playerAttackR = True

                    
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

    mainCount += 1
    if mainCount == 25:
        mainCount = 0
    
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


    if player.playerHurt == True:
        if hurtCount == 0:
            playerStillCopy = playerStill
        player.playerInvuln = True
        hurtCount += 1
        if hurtCount%2 != 0:
            playerStill = colorize(playerStill, (255,255,255))
        else:
            playerStill = playerStillCopy

        if hurtCount < 10:
            if player.playerHurtFace == 'U':
                player.playerY += 10
            if player.playerHurtFace == 'R':
                player.playerX -= 10
            if player.playerHurtFace == 'D':
                player.playerY -= 10
            if player.playerHurtFace == 'L':
                player.playerX += 10

        if hurtCount >= 10:
            player.playerCon = True

        if hurtCount >= 20:
            player.playerInvuln = False
            player.playerHurt = False
            hurtCount = 0

            
            
        



    if player.playerAttackU == True:
        if attackCount ==0:
            playerStillCopy = playerStill
            attackBox = pygame.Rect(WIDTH/2 - 16 -50,HEIGHT/2 - 16 - 80, 82,20)
            playerStill = playerUpA
        if attackCount == 3:
            playerStill = playerStillCopy
        player.attackU()
        attackCount += 1
        if attackCount == 7:
            player.attackBoxU.move_ip(-50000,-50000)
            player.playerCon = True
            attackCount = 0
            player.playerAttackU = False
            mainCount = 0
            
    if player.playerAttackL == True:
        if attackCount ==0:
            playerStillCopy = playerStill
            playerStill = playerLeftA
        if attackCount == 3:
            playerStill = playerStillCopy
        player.attackL()
        attackCount += 1
        if attackCount == 7:
            player.attackBoxL.move_ip(-50000,-50000)
            player.playerCon = True
            attackCount = 0
            player.playerAttackL = False
            mainCount = 0
            
    if player.playerAttackD == True:
        if attackCount ==0:
            swordMovement = (-(WIDTH/2 -10+50000),-(HEIGHT/2 +50 +50000))
            player.attackBoxD.move_ip(WIDTH/2 -10+50000,HEIGHT/2 +50 +50000)
            playerStillCopy = playerStill
            playerStill = playerDownA
        if attackCount == 3:
            playerStill = playerStillCopy
        player.attackD()
        attackCount += 1
        if attackCount == 7:
            player.attackBoxD.move_ip(swordMovement)
            player.playerCon = True
            attackCount = 0
            player.playerAttackD = False
            mainCount = 0

            
    if player.playerAttackR == True:
        if attackCount ==0:
            swordMovement = (-(WIDTH/2 + 16+50000),-(HEIGHT/2+50000))
            player.attackBoxR.move_ip(WIDTH/2 + 16+50000,HEIGHT/2+50000)
            playerStillCopy = playerStill
            playerStill = playerRightA
        if attackCount == 3:
            playerStill = playerStillCopy
        player.attackR()
        attackCount += 1
        if attackCount == 7:
            player.attackBoxR.move_ip(swordMovement)
            player.playerCon = True
            attackCount = 0
            player.playerAttackR = False
            mainCount = 0
        

    #DASH COUNTER

    if dashCount > 0:
        if dashCount == 1:
            playerStillCopy = playerStill
        playerStill = blit_alpha(SCREEN, playerStill, (100,100), 220)
        player.playerCon = False
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
            mainCount = 0





    #ACTUALLY MOVING THE PLAYER
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

    if player.playerCon == True:
        if player.playerMoveLeft == True:
            player.playerFace = 'L'
            if mainCount > 15 :
                playerStill = playerLeft1
            else:
                playerStill = playerLeft2
                player.Left()
        if player.playerMoveRight == True:
            player.playerFace = 'R'
            
            if mainCount>15 :
                playerStill = playerRight1
            else:
                playerStill = playerRight2
                player.Right()

        if player.playerMoveUp == True:
            player.playerFace = 'U'
            
            if mainCount > 15 :
                playerStill = playerUp1
            else:
                playerStill = playerUp2
                player.Up()
        if player.playerMoveDown == True:
            player.playerFace = 'D'
            if mainCount > 15 :
                playerStill = playerDown1
            else:
                playerStill = playerDown2
                player.Down()

    playerX, playerY = player.getPlayerPos()

    for i in range (ghostNum):
        ghostStr = 'ghost' + str(i+1)

        if eval(ghostStr).act == True:

            eval(ghostStr).move()
        else:
            eval(ghostStr).active()


    for i in range (ghostNum):
        ghostStr = 'ghost' + str(i+1)

        if eval(ghostStr).dead == False:

            eval(ghostStr).update(oldPlayerX-playerX,oldPlayerY-playerY)
            
            if pygame.Rect.colliderect(player.hitbox, eval(ghostStr).hitbox) == True and player.playerInvuln == False:
                player.hurt()
                
            pygame.draw.rect(SCREEN,(255,255,255),player.attackBoxR)
            pygame.draw.rect(SCREEN,(255,255,255),player.attackBoxD)
            pygame.draw.rect(SCREEN,(255,255,255),player.attackBoxL)
            pygame.draw.rect(SCREEN,(255,255,255),player.attackBoxU)


            if pygame.Rect.colliderect(player.attackBoxU, eval(ghostStr).hitbox) == True:
                eval(ghostStr).hurtf()
            if pygame.Rect.colliderect(player.attackBoxD, eval(ghostStr).hitbox) == True:
                eval(ghostStr).hurtf()
            if pygame.Rect.colliderect(player.attackBoxL, eval(ghostStr).hitbox) == True:
                eval(ghostStr).hurtf()
            if pygame.Rect.colliderect(player.attackBoxR, eval(ghostStr).hitbox) == True:
                eval(ghostStr).hurtf()


            if eval(ghostStr).health <= 0:
                eval(ghostStr).kill()


    for i in range (spikeNum):
        spikeStr = 'spike' + str(i+1)

        eval(spikeStr).update(oldPlayerX-playerX,oldPlayerY-playerY)

    if player.playerHealth == 0:
        restart_program()


# =================================================================================
    # DRAWING SHIT
# =================================================================================
    playerX, playerY = player.getPlayerPos()





    for i in range (spikeNum):
        spikeStr = 'spike' + str(i+1)
        eval(spikeStr).draw()
        
    for i in range (ghostNum):
        ghostStr = 'ghost' + str(i+1)
        if eval(ghostStr).dead == False:
            eval(ghostStr).draw()


    SCREEN.blit(playerStill,(WIDTH/2 - 16,HEIGHT/2 - 16))


    for i in range (player.playerMaxStam):
        if i < player.playerStam:
            SCREEN.blit(stamina,((WIDTH - 35*(i))-150,10))
        if i >= player.playerStam:
            SCREEN.blit(noStamina,((WIDTH - 35*(i))-150,10))

    for i in range (player.playerMaxHealth):
        if i < player.playerHealth:
            SCREEN.blit(heart,( 5 + 80*(i), 10))
        if i >= player.playerHealth:
            SCREEN.blit(noHeart,( 5 + 80*(i), 10))

            
    pygame.display.update()
    fpsClock.tick(FPS)

