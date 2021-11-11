from math import gamma
import random, sys, pygame
from pygame.locals import *
from pygame.version import *


# making global variables for the games..
FPS = 32
SCREENWIDTH = 800
SCREENHEIGHT = 500
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'sprites/bird.png'
BACKGROUND = 'sprites/background.png'
PIPE = 'sprites/pipe.png'

def welcomeScreen():
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2.7)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2.01)
    messagey = int(SCREENHEIGHT*0.01)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user ne cross daba diya to close ho jayega..
            if event.type == QUIT or (event.type==KEYDOWN and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # Agar user space or up key dabata hai to game start ho jayega..
            elif event.type == KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            
            else:

                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
                
def isCollide(playerx, playery, upperPipes, lowerPipes):
    return False


def getRandomPipeLen():
    """
    Generate positions of two pipes (ek ulta ek seedha) for blitting on the screen.
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT / 3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
    pipeX = SCREENWIDTH + 50
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2}
    ]
    return pipe

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2.7)
    basex = 0
    
    # Now creating pipes for bliting on the screen..

    newPipe1 = getRandomPipeLen()
    newPipe2 = getRandomPipeLen()

    # my list of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH + 400, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 400 + (SCREENWIDTH/2), 'y': newPipe2[0]['y']}
    ]
    # my list of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH + 400, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 400 + (SCREENWIDTH/2), 'y': newPipe2[0]['y']}
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMaxVelX = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # it is try only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['hit'].play()
        
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # will return ture if youo are crashed.
        if crashTest:
            return

        # Check for score
        playerMidPos = playerx - GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()


        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)


        # moving pipes to left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
        
        # Add a new pipe when the first pipe is about to go to the left part of the screen
        if 0<upperPipe['x'][0]<5:
            newpipe = getRandomPipeLen()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])


        # if teh pipe is out of the screen, remove it..
        if upperPipes[0]['x'] < - GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
            
        # lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['number'][digit].get_width()

        Xoffset = (SCREENWIDTH - width)/2
        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['number'][digit], (Xoffset, SCREENHEIGHT*1))
            Xoffset += GAME_SPRITES['number'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    # this is the main function jaha se hamara game start hoga..
    pygame.init() # Initialize all pygame modules..
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy bird by Anant')
    GAME_SPRITES['number'] = (
        pygame.image.load('sprites/0.png').convert_alpha(),
        pygame.image.load('sprites/1.png').convert_alpha(),
        pygame.image.load('sprites/2.png').convert_alpha(),
        pygame.image.load('sprites/3.png').convert_alpha(),
        pygame.image.load('sprites/4.png').convert_alpha(),
        pygame.image.load('sprites/5.png').convert_alpha(),
        pygame.image.load('sprites/6.png').convert_alpha(),
        pygame.image.load('sprites/7.png').convert_alpha(),
        pygame.image.load('sprites/8.png').convert_alpha(),
        pygame.image.load('sprites/9.png').convert_alpha()
    )

    GAME_SPRITES['message'] = pygame.image.load('sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
    pygame.image.load(PIPE).convert_alpha()
    )

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    GAME_SOUNDS['die'] = pygame.mixer.Sound('audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('audio/point.wav')

    while True:
        welcomeScreen() #Welcome screen dikhayega.. Till user doesn't click anywhere.
        mainGame()
