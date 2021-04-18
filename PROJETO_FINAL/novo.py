import sys, pygame
from pygame.locals import *
from random import *


pygame.init()


TAMANHO_TELA_X = 1200
TAMANHO_TELA_Y = 600

screen = pygame.display.set_mode((TAMANHO_TELA_X,TAMANHO_TELA_Y))


TAMANHO_PLAYER_X = 200
TAMANHO_PLAYER_Y = 200
sprites = []
pos_sprite = 0
pos_x = 40
pos_y = 100
clock = pygame.time.Clock()

BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
cores = [RED, BLUE, YELLOW, GREEN]

background = pygame.image.load('bg11.jpg').convert()
background = pygame.transform.scale(background, (TAMANHO_TELA_X, TAMANHO_TELA_Y)) 





class Player():
  
  
  
  def __init__(self):
    super().__init__()
    
    
    self.imagem1 = pygame.image.load('RatPilot1.png').convert_alpha()
    self.imagem1 = pygame.transform.scale(self.imagem1, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    self.imagem2 = pygame.image.load('RatPilot2.png').convert_alpha()
    self.imagem2 = pygame.transform.scale(self.imagem2, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    self.imagem3 = pygame.image.load('RatPilot3.png').convert_alpha()
    self.imagem3 = pygame.transform.scale(self.imagem3, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    self.imagem4 = pygame.image.load('RatPilot4.png').convert_alpha()
    self.imagem4 = pygame.transform.scale(self.imagem4, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    
    
    sprites.append(self.imagem1)
    sprites.append(self.imagem2)
    sprites.append(self.imagem3)
    sprites.append(self.imagem4)
    
    self.current_sprite = 0
    self.image = sprites[self.current_sprite]
    self.is_animating = True
    
    self.rect = self.image.get_rect()
    #self.rect.topleft = [pos_x,pos_y]
    




player = Player()

while True:
    
    
   
    for event in pygame.event.get():
       
        
        
       
      if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w or event.key == pygame.K_UP :
            pos_y -= 10
            
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            pos_y +=10
              
        
    if (pos_sprite > len(sprites) -1):
          
          pos_sprite = 0
        
    
    screen.blit(background,[0,0])
    screen.blit(sprites[pos_sprite], (pos_x, pos_y))     
    pygame.display.flip()      
    pos_sprite+=1
    clock.tick(40)
       
    


frame = pygame.draw.rect(screen, (WHITE), Rect((0, 0), (800, 600)))





