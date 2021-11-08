import random, sys, pygame
from pygame.locals import *
from pygame.version import *


# making global variables for the games..
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'sprites/bird.png'
BACKGROUND = 'sprites/backgound.png'
PIPE = 'sprites/pipe.png'


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

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND)
    
    GAME_SOUNDS['die'] = pygame.mixer.sound('audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.sound('audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.sound('audio/point.wav')
    GAME_SOUNDS['die'] = pygame.mixer.sound('audio/die.wav')