import sys, pygame
from pygame.locals import *
from random import *


pygame.init()



screen = pygame.display.set_mode((1000,500))


pygame.display.set_caption("Papa Bolinhas")



BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
cores = [RED, BLUE, YELLOW, GREEN]

background = pygame.image.load('bg11.jpg').convert()
background = pygame.transform.scale(background, (1000, 500)) 





class Player():
  
  TAMANHO_PLAYER_X = 200
  TAMANHO_PLAYER_Y = 200
  
  def __init__(self, pos_x, pos_y):
    super().__init__()
    
    
    self.imagem1 = pygame.image.load('RatPilot1.png').convert_alpha()
    self.imagem1 = pygame.transform.scale(self.imagem1, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    self.imagem2 = pygame.image.load('RatPilot2.png').convert_alpha()
    self.imagem2 = pygame.transform.scale(self.imagem2, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    self.imagem3 = pygame.image.load('RatPilot3.png').convert_alpha()
    self.imagem3 = pygame.transform.scale(self.imagem3, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    self.imagem4 = pygame.image.load('RatPilot4.png').convert_alpha()
    self.imagem4 = pygame.transform.scale(self.imagem4, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    
    self.sprites = []
    self.sprites.append(self.imagem1)
    self.sprites.append(self.imagem2)
    self.sprites.append(self.imagem3)
    self.sprites.append(self.imagem4)
    
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]
    self.is_animating = True
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x,pos_y]
    





while True:
    
    
   
    for event in pygame.event.get():
       
        pos_sprite = 0
        pos_x = 100
        pos_y = 100
        player = Player(pos_x, pos_y)
        screen.blit(background,[0,0])
        screen.blit(pygame.sprite[pos_sprite], (pos_x, pos_y))     
        pygame.display.flip()      
       
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    


frame = pygame.draw.rect(screen, (WHITE), Rect((0, 0), (800, 600)))





