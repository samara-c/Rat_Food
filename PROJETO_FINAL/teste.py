import pygame
import sys



TAMANHO_TELA_X = 1200
TAMANHO_TELA_Y = 600

TAMANHO_PLAYER_X = 200
TAMANHO_PLAYER_Y = 200 

posicao_jogador_x = 100
posicao_jogador_y = 100

screen = pygame.display.set_mode((TAMANHO_TELA_X, TAMANHO_TELA_Y))
background = pygame.image.load('bg11.jpg').convert()

 

class Player (pygame.sprite.Sprite):
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
    
    self.sprites = []
    self.sprites.append(self.imagem1)
    self.sprites.append(self.imagem2)
    self.sprites.append(self.imagem3)
    self.sprites.append(self.imagem4)
    
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]
    self.is_animating = True
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [100,100]
    
  
#   def animate(self):
   
       
  def update(self):
      self.current_sprite += 1
      
      if self.current_sprite>= len(self.sprites):
        self.current_sprite = 0
        
      self.image = self.sprites[self.current_sprite]
      
    
  def moverPlayer(self,pos_x, pos_y):
    self.rect.topleft = [pos_x,pos_y]
      
             
moving_sprites = pygame.sprite.Group() 
pygame.init()

Clock = pygame.time.Clock()
player = Player()

# background = pygame.transform.scale(background, (TAMANHO_TELA_X, TAMANHO_TELA_Y))

# moving_sprites = pygame.sprite.Group() 
# player = Player(100,100)
# moving_sprites.add(player)



w = 1000
h = 500
x = 0
y = 0

x1 = w
y1 = 0


while True:
    screen.blit(background,[TAMANHO_TELA_X, TAMANHO_TELA_Y])
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
            
    x1 -= 15
    x -= 15
    if x > w:
        x = w
    if x1 > w:
        x1 = w
        
    
   
    screen.blit(background,(x,y))
    screen.blit(background,(x1,y1))
    moving_sprites.update()
    moving_sprites.draw(screen) 
    pygame.display.update()
    Clock.tick(10)