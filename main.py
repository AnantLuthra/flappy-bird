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
                

def mainGame():
    pass


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