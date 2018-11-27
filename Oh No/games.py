import pygame, sys, os

from pygame.locals import *
pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

WIDTH = 1280
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pale King')



playerStill = pygame.image.load('Sprites/New Piskel.png')
spikeImg = pygame.image.load('Sprites/Spike.png')
stamina = pygame.image.load('Sprites/Stam.png')
noStamina = pygame.image.load('Sprites/NoStam.png')
heart = pygame.image.load('Sprites/Heart.png')
noHeart = pygame.image.load('Sprites/NoHeart.png')
swipeU = pygame.image.load('Sprites/AttackU.png')
swipeL= pygame.image.load('Sprites/AttackL.png')
swipeD= pygame.image.load('Sprites/AttackD.png')
swipeR= pygame.image.load('Sprites/AttackR.png')

spikeNum = 2


stage = 0
dashCount = 0
staminaCount = 0
attackStamCount = 0
attackCount = 0
hurtCount = 0






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
        self.playerMaxStam = 2
        self.playerStam = self.playerMaxStam
        self.playerFace = 'D'
        self.playerMaxHealth = 3
        self.playerHealth = 2
        self.playerAttackU = False
        self.playerAttackL = False
        self.playerAttackD = False
        self.playerAttackR = False
        self.playerHurt = False
        self.playerInvuln = False
        self.playerHurtFace = 'D'
        self.hitbox = pygame.Rect(WIDTH/2 - 16,HEIGHT/2 - 16,32,32)

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

    for i in range (spikeNum):
        spikeStr = 'spike' + str(i+1)
        if pygame.Rect.colliderect(player.hitbox, eval(spikeStr).hitbox) == True and player.playerInvuln == False:
            player.hurt()

    #Stamina Regen

    if player.playerStam != player.playerMaxStam:
        staminaCount += 1
        if staminaCount == 30:
            player.playerStam += 1
            staminaCount = 0


    if player.playerHurt == True:
        player.playerInvuln = True
        hurtCount += 1
        if hurtCount%2 != 0:
            playerStill = pygame.image.load('Sprites/New Piskel Hurt.png')
        else:
            playerStill = pygame.image.load('Sprites/New Piskel.png')

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
        player.attackU()
        attackCount += 1
        if attackCount == 7:
            player.playerCon = True
            attackCount = 0
            player.playerAttackU = False
            
    if player.playerAttackL == True:
        player.attackL()
        attackCount += 1
        if attackCount == 7:
            player.playerCon = True
            attackCount = 0
            player.playerAttackL = False
            
    if player.playerAttackD == True:
        player.attackD()
        attackCount += 1
        if attackCount == 7:
            player.playerCon = True
            attackCount = 0
            player.playerAttackD = False
            
    if player.playerAttackR == True:
        player.attackR()
        attackCount += 1
        if attackCount == 7:
            player.playerCon = True
            attackCount = 0
            player.playerAttackR = False
        

    #DASH COUNTER

    if dashCount > 0:
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
            dashCount = 0





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
            player.Left()
        if player.playerMoveRight == True:
            player.Right()
        if player.playerMoveUp == True:
            player.Up()
        if player.playerMoveDown == True:
            player.Down()

    playerX, playerY = player.getPlayerPos()


    for i in range (spikeNum):
        spikeStr = 'spike' + str(i+1)

        eval(spikeStr).update(oldPlayerX-playerX,oldPlayerY-playerY)


# =================================================================================
    # DRAWING SHIT
# =================================================================================
    playerX, playerY = player.getPlayerPos()

    

    

    for i in range (spikeNum):
        spikeStr = 'spike' + str(i+1)
        eval(spikeStr).draw()


    spike1.draw()
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

