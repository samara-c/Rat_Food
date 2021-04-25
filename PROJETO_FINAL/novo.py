import sys, pygame
from pygame.locals import *
from random import *


pygame.init()

 

TAMANHO_TELA_X = 1200
TAMANHO_TELA_Y = 600

TAMANHO_INIMIGO_X = 100
TAMANHO_INIMIGO_Y = 100

VELOCIDADE_BONUS = - 15

screen = pygame.display.set_mode((TAMANHO_TELA_X,TAMANHO_TELA_Y))


TAMANHO_PLAYER_X = 200
TAMANHO_PLAYER_Y = 200
VELOCIDADE_PLAYER = 15

vator_bonus_pontos = []
vetor_bonus =  []
vetor_bonus_posicao_y = []
vetor_bonus_posicao_x = []
bonus = []
bonus_pos = []

inimigos = []
pos_inimigos = []
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
TAMANHO_FONTE_FASES = 200
j = 0
movimento_positivo = False

placar = pygame.image.load('elements//cloud.png').convert()
placar = pygame.transform.scale(placar, (300, 100)) 

background = pygame.image.load('bg11.jpg').convert()
background = pygame.transform.scale(background, (TAMANHO_TELA_X, TAMANHO_TELA_Y)) 


CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) 
temporizador = 60





class Player():
  
  
  
  def __init__(self):
    super().__init__()
    
    self.path = "player//"
    self.imagem1 = pygame.image.load(self.path+'RatPilot1.png').convert_alpha()
    self.imagem1 = pygame.transform.scale(self.imagem1, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    self.imagem2 = pygame.image.load(self.path+'RatPilot2.png').convert_alpha()
    self.imagem2 = pygame.transform.scale(self.imagem2, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    self.imagem3 = pygame.image.load(self.path+'RatPilot3.png').convert_alpha()
    self.imagem3 = pygame.transform.scale(self.imagem3, (TAMANHO_PLAYER_X, TAMANHO_PLAYER_Y))
    self.imagem4 = pygame.image.load(self.path+'RatPilot4.png').convert_alpha()
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
    
    self.pontos = 0

class ElementosTela() :
  
  def __init__(self):
    self.font_fases = pygame.font.Font("fonts//HARD ROCK.ttf", TAMANHO_FONTE_FASES)
    self.text_fases = self.font_fases.render("FASE 1", True, (WHITE)) 
    
    self.font_fases2 = pygame.font.Font("fonts//Cotton Cloud.ttf", TAMANHO_FONTE_FASES)
    self.font_fases3 = pygame.font.Font("fonts//HARD ROCK.ttf", TAMANHO_FONTE_FASES)
    
    self.text_fases2 = self.font_fases2.render("Fase 1", True, (WHITE)) 
    self.text_fases3 = self.font_fases3.render("FASE 1", True, (BLACK)) 
    
    self.font = pygame.font.SysFont('sans',30)
  
  def escreverNomeFase(self):
#     screen.blit(self.text_fases3, (410,200))
    screen.blit(self.text_fases2, (400,200))     

class Inimigos():
  #Inicializa a classe inimigos e carrega os sprites correspondentes
  def __init__(self):
    self.path = "enemies//"
    
    self.inimigo1 =   pygame.image.load(self.path+'chicken.png').convert_alpha()
    self.inimigo1 = pygame.transform.scale(self.inimigo1, (TAMANHO_INIMIGO_X, TAMANHO_INIMIGO_Y))
    
    self.inimigo2 =   pygame.image.load(self.path+'cookie.png').convert_alpha()
    self.inimigo2 = pygame.transform.scale(self.inimigo2, (70, 70))
    
    self.inimigo3 =   pygame.image.load(self.path+'cupcake.png').convert_alpha()
    self.inimigo3 = pygame.transform.scale(self.inimigo3, (70, 70))
    
    self.inimigo4 =   pygame.image.load(self.path+'donut.png').convert_alpha()
    self.inimigo4 = pygame.transform.scale(self.inimigo4, (70, 70))
    
    self.inimigo5 =   pygame.image.load(self.path+'pizza.png').convert_alpha()
    self.inimigo5 = pygame.transform.scale(self.inimigo5, (70, 70))
    
    
   #Adiciona inimigos ao vetor   
    inimigos.append(self.inimigo1)
    inimigos.append(self.inimigo2)
    inimigos.append(self.inimigo3)
    inimigos.append(self.inimigo4)
    inimigos.append(self.inimigo5)
   
   
     
    

  def lancaInimigo(self):
    pos_inicial_y = randint(100,500)
    screen.blit(self.inimigo1, (400,300)) 
    screen.blit(self.inimigo2, (200,300)) 

class Bonus():
  def __init__(self):
    self.path = "bonus//"
    self.bonus1 = pygame.image.load(self.path+'banana.png').convert_alpha()
    self.bonus1 = pygame.transform.scale(self.bonus1, (70, 70 ))
    self.pontosBonus1 = 50
    
    self.bonus2 = pygame.image.load(self.path+'apple.png').convert_alpha()
    self.bonus2 = pygame.transform.scale(self.bonus2, (70, 70 ))
    self.pontosBonus2 = 55
    
    self.bonus3 = pygame.image.load(self.path+'grape.png').convert_alpha()
    self.bonus3 = pygame.transform.scale(self.bonus3, (70, 70 ))
    self.pontosBonus3 = 70
    
    bonus.append(self.bonus1)
    bonus.append(self.bonus2)
    bonus.append(self.bonus3)
   
  
  def deletaBonus(self):
    c = 0
    while c < (len(vetor_bonus)):
      if (vetor_bonus_posicao_x[c] < 200):
        del(vetor_bonus_posicao_x[c])
        del(vetor_bonus_posicao_y[c])
        del(vetor_bonus[c])
      c+=1  
  
  def sorteiaBonus(self, j):
    num = randint(0, 1000)
    if j==num or j > 1000:
      bonusObj.lancaBonus()
      j = -1
  
  
  def lancaBonus(self):
    posicao = randint(100,500)
    bonusPosicao = randint(0,2)
    vetor_bonus.append(bonus[bonusPosicao])
    vetor_bonus_posicao_y.append(posicao)
    vetor_bonus_posicao_x.append(1250)
      
  def moveBonus(self):
    i = 0
    k = 10
    if (len(vetor_bonus) < k): 
      while i<(len(vetor_bonus)):
        vetor_bonus_posicao_x[i] += VELOCIDADE_BONUS
        screen.blit(vetor_bonus[i],(vetor_bonus_posicao_x[i], vetor_bonus_posicao_y[i]))
        i+=1  
    
player = Player()
elementos = ElementosTela()
inimigos = Inimigos()
bonusObj = Bonus()
while True:
    
    
   
    for event in pygame.event.get():
       
        
        
       
      if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      if event.type == CLOCKTICK:
            temporizador = temporizador -1
                  
      if event.type == pygame.KEYDOWN:
        if event.key == K_SPACE:
          movimento_positivo = True
          
      if event.type == pygame.KEYUP:
        if event.key == K_SPACE:
          movimento_positivo = False    
          
      pressed = pygame.key.get_pressed()
      
    if movimento_positivo == True:
        pos_y -= VELOCIDADE_PLAYER  
    if movimento_positivo == False:
        pos_y += VELOCIDADE_PLAYER+10 
      
    if pos_y <10:
      pos_y =10
    if pos_y > 390:
      pos_y = 390   
     
#       elif event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_w or event.key == pygame.K_UP :
#             pos_y -= 10
#             
#         elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
#             pos_y +=10
   
    j+=1
    bonusObj.deletaBonus()
    bonusObj.sorteiaBonus(j)
    
      
              
        
    if (pos_sprite > len(sprites) -1):
          
          pos_sprite = 0
        
    
    screen.blit(background,[0,0])
    
    #pegar tamanho varaiavel, ver se ja liberou espaco, depois blitar proxima imagem. colocar velocidade movimento, *criar vetores com nuvem, controlar elas
    screen.blit(sprites[pos_sprite], (pos_x, pos_y)) 
    #elementos.escreverNomeFase()
    inimigos.lancaInimigo()
    bonusObj.moveBonus()
    screen.blit(placar,(800,60))
    timer1 = elementos.font.render('Time ' + str(temporizador), True, (YELLOW))
    screen.blit(timer1, (1000, 50))  
    pygame.display.flip()      
    pos_sprite+=1
    clock.tick(60)
       
    


frame = pygame.draw.rect(screen, (WHITE), Rect((0, 0), (800, 600)))





