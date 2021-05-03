import sys, pygame
from pygame.locals import *
from random import *
import math
from pickle import FALSE




pygame.init()
pygame.display.set_caption('Rat Food')


TAMANHO_TELA_X = 1200
TAMANHO_TELA_Y = 650

TAMANHO_INIMIGO_X = 100
TAMANHO_INIMIGO_Y = 100

VELOCIDADE_BONUS = - 8
VELOCIDADE_INIMIGO = -5

screen = pygame.display.set_mode((TAMANHO_TELA_X,TAMANHO_TELA_Y))


TAMANHO_PLAYER_X = 140
TAMANHO_PLAYER_Y = 140
velocidade_player = 5

vator_bonus_pontos = []
vetor_bonus =  []
vetor_bonus_posicao_y = []
vetor_bonus_posicao_x = []
bonus_v = []
bonus_pos = []


energia = 1000   
vetor_inimigos = []
vetor_inimigos_pontos = []
vetor_inimigos = []
vetor_inimigos_posicao_x = []
vetor_inimigos_posicao_y = []
vetor_inimigos_ativos = []
pos_inimigos = []
sprites = []
pos_sprite = 0
pos_x = 35
pos_y = 100
clock = pygame.time.Clock()





BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (243, 255, 43)
RED = (255, 74, 73)
DARK_BLUE = (15, 41, 71)
BLUE = (49,171,232)
GREEN = (71,255,43)
TAMANHO_FONTE_FASES = 200

movimento_positivo = False

relogio = pygame.image.load('elements//clock.png').convert_alpha()
relogio = pygame.transform.scale(relogio, (90, 40)) 


background = pygame.image.load('bg11.jpg').convert()
background = pygame.transform.scale(background, (TAMANHO_TELA_X, TAMANHO_TELA_Y - 50)) 
background_inicio = background = pygame.transform.scale(background, (TAMANHO_TELA_X, TAMANHO_TELA_Y)) 


fase_1 = False  
fase_2 = False 
fase_3 = False
tela_inicial = True
menu_pos_selecionada = 0

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) 
temporizador = 60

lancador_bonus = True
lancador_inimigos = True

opcao_iniciar_menu = True
opcao_instrucoes_menu = False
opcao_ajustes_menu = False


  

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
    self.path = "fonts//"
    self.path_elements = "elements//"
    
    self.font_1 = pygame.font.Font(self.path+"Candy Beans.otf", 20)
    self.font_2 = pygame.font.Font(self.path+"No Virus.ttf", 20)
    self.font_3 = pygame.font.Font(self.path+"MilkyNice.ttf", 30)
    self.font_4 = pygame.font.Font(self.path+"MilkyNice.ttf", 36)
    self.font_fases = pygame.font.Font("fonts//HARD ROCK.ttf", TAMANHO_FONTE_FASES)
    
    
    self.font_fases2 = pygame.font.Font("fonts//Cotton Cloud.ttf", TAMANHO_FONTE_FASES)
    self.font_fases3 = pygame.font.Font("fonts//HARD ROCK.ttf", TAMANHO_FONTE_FASES)
    
    self.font = pygame.font.SysFont('sans',26)
    
    self.nuvem = pygame.image.load(self.path_elements+'cloud_inicio.png').convert_alpha()
    self.nuvem = pygame.transform.scale(self.nuvem, (960,505)) 
    
    self.posicao_item = 320
    
    self.text_iniciar = "Iniciar"
    self.texto_instrucoes = "Como jogar"
    self.texto_ajustes = "Ajustes"
    
    self.energia_icone = pygame.image.load(self.path_elements+'energy.png').convert_alpha()
    self.energia_icone = pygame.transform.scale(self.energia_icone, (35,35))
    self.tamanho_barra = 100 
  
  def carregaElementosTelaInicial(self):
    screen.blit(self.nuvem, (120,50))
    #self.texto = self.font_3.render("Sistemas de Informacao - Mackenzie", True, (BLACK))
    #screen.blit(self.texto,(400,580))
    elementos.carregaMenu()
 
 
  def calculaBarraEnergia (self, valor):
    
    valor = math.ceil(valor/10)
    self.tamanho_barra = valor 
    print("O valor eh"+ str(valor))
    
    if valor >= 66 and valor <= 100:
      cor = GREEN
    elif valor >= 33 and valor <= 65:
      cor = YELLOW
    elif valor >= 0 and valor <= 32:
      cor = RED    
    return cor   
 
  def carregaBarraEnergia(self, cor = GREEN):
    pygame.draw.rect(screen,WHITE,(692,18,112,18), 0)
    pygame.draw.rect(screen,cor,(702,21,self.tamanho_barra,13), 0)
    screen.blit(self.energia_icone, (680,10))
    
    
  def carregaMenu(self, cor = BLACK):
    self.opcao_iniciar =  self.font_4.render(self.text_iniciar, True, (cor))
    self.opcao_instrucoes = self.font_4.render(self.texto_instrucoes, True, (cor))
    self.opcao_ajustes = self.font_4.render(self.texto_ajustes, True, (cor))
    
    screen.blit(self.opcao_iniciar,(560,self.posicao_item))
    screen.blit(self.opcao_instrucoes,(520,self.posicao_item+50))
    screen.blit(self.opcao_ajustes,(550,self.posicao_item+100))
  
    
  def navegaMenu (self, pos):
    if pos == 0:
      self.opcao_iniciar =  self.font_4.render(self.text_iniciar, True, (BLUE))
      screen.blit(self.opcao_iniciar,(560,self.posicao_item))
    elif pos == 1:
      self.opcao_instrucoes =  self.font_4.render(self.texto_instrucoes, True, (BLUE))
      screen.blit(self.opcao_instrucoes,(520,self.posicao_item+50))
    elif pos == 2:
      self.opcao_ajustes =  self.font_4.render(self.texto_ajustes, True, (BLUE))
      screen.blit(self.opcao_ajustes,(550,self.posicao_item+100))  
   
  def exibeInstrucoes (self):
    print("ola")

#Controla os inimigos
class Inimigos():
  #Inicializa a classe vetor_inimigos e carrega os sprites correspondentes
  def __init__(self):
    self.path = "enemies//"
    
    self.inimigo1 =   pygame.image.load(self.path+'chicken.png').convert_alpha()
    self.inimigo1 = pygame.transform.scale(self.inimigo1, (75, 75))
    
    self.inimigo2 =   pygame.image.load(self.path+'cookie.png').convert_alpha()
    self.inimigo2 = pygame.transform.scale(self.inimigo2, (40, 40))
    
    self.inimigo3 =   pygame.image.load(self.path+'cupcake.png').convert_alpha()
    self.inimigo3 = pygame.transform.scale(self.inimigo3, (60, 60))
    
    self.inimigo4 =   pygame.image.load(self.path+'donut.png').convert_alpha()
    self.inimigo4 = pygame.transform.scale(self.inimigo4, (50, 50))
    
    self.inimigo5 =   pygame.image.load(self.path+'pizza.png').convert_alpha()
    self.inimigo5 = pygame.transform.scale(self.inimigo5, (70, 70))
    
    self.iterador = -1
    
   #Adiciona vetor_inimigos ao vetor   
    vetor_inimigos.append(self.inimigo1)
    vetor_inimigos.append(self.inimigo2)
    vetor_inimigos.append(self.inimigo3)
    vetor_inimigos.append(self.inimigo4)
    vetor_inimigos.append(self.inimigo5)
    print("O tamanho do vetor eh "+str(len(vetor_inimigos)))
   
   
  def deletaInimigo(self):
    c = 0
    while c < (len(vetor_inimigos_ativos)):
      if (vetor_inimigos_posicao_x[c] < -1):
        del(vetor_inimigos_posicao_x[c])
        del(vetor_inimigos_posicao_y[c])
        del(vetor_inimigos_ativos[c])
        print(str(len(vetor_inimigos_ativos)))
        print(str(len(vetor_inimigos_posicao_x)))
      c+=1    
    
  def sorteiaInimigo(self):
    print(str(self.iterador))
    print(str(len(vetor_inimigos)))
    limite = 50
    num = randint(0,50)
    if self.iterador==num:
      inimigoObj.lancaInimigo()
      print(str(self.iterador))
      print(str(num))
      self.iterador = -1
    if self.iterador>limite:
      self.iterador=-1      

  def lancaInimigo(self):
    print(str(lancador_inimigos))
    if lancador_inimigos == True:
      posicao = randint(60,540)
      inimigoPosicao = randint(0,len(vetor_inimigos)-1)
      vetor_inimigos_ativos.append(vetor_inimigos[inimigoPosicao])
      vetor_inimigos_posicao_y.append(posicao)
      vetor_inimigos_posicao_x.append(1300)

  def moveInimigo(self, k):
    i = 0
    if (len(vetor_inimigos_ativos) < k+1): 
      while i<(len(vetor_inimigos_ativos)):
        vetor_inimigos_posicao_x[i] += VELOCIDADE_INIMIGO
        screen.blit(vetor_inimigos_ativos[i],(vetor_inimigos_posicao_x[i], vetor_inimigos_posicao_y[i]))
        i+=1
        
  def verificaColisao(self, pos_player):
    i = 0
    while i < (len(vetor_inimigos_ativos)):
      if (vetor_inimigos_posicao_x[i] <= pos_player) and (vetor_inimigos_posicao_y[i] >= 185):
        print( "COLIDIU")
        i+=1
    
          
              


#Controla os bonus
class Bonus():
  def __init__(self):
    self.path = "bonus//"
    self.bonus1 = pygame.image.load(self.path+'banana.png').convert_alpha()
    self.bonus1 = pygame.transform.scale(self.bonus1, (50, 50 ))
    self.pontosBonus1 = 10
    
    self.bonus2 = pygame.image.load(self.path+'apple.png').convert_alpha()
    self.bonus2 = pygame.transform.scale(self.bonus2, (40, 40 ))
    self.pontosBonus2 = 15
    
    self.bonus3 = pygame.image.load(self.path+'grape.png').convert_alpha()
    self.bonus3 = pygame.transform.scale(self.bonus3, (50, 50 ))
    self.pontosBonus3 = 15
    
    self.bonus4 = pygame.image.load(self.path+'strawberry.png').convert_alpha()
    self.bonus4 = pygame.transform.scale(self.bonus4, (30, 30 ))
    self.pontosBonus4 = 30
    
    #Define a quantidade de frutas no vetor, As frutas que valem mais pontos sao mais raras
    bonus_v.append(self.bonus1)
    bonus_v.append(self.bonus1)
    bonus_v.append(self.bonus1)
    bonus_v.append(self.bonus2)
    bonus_v.append(self.bonus2)
    bonus_v.append(self.bonus3)
    bonus_v.append(self.bonus3)
    bonus_v.append(self.bonus4)
    
    
    self.iterador = -1
    self.energia = 1000
  
  def deletaBonus(self):
    c = 0
    while c < (len(vetor_bonus)):
      if (vetor_bonus_posicao_x[c] < -1):
        del(vetor_bonus_posicao_x[c])
        del(vetor_bonus_posicao_y[c])
        del(vetor_bonus[c])
        self.energia -= 20
        
#         print(str(len(vetor_bonus)))
#         print(str(len(vetor_bonus_posicao_x)))
      c+=1  
  
  def sorteiaBonus(self):
    print(str(self.iterador))
    print(str(len(vetor_bonus)))
    limite = 50
    num = randint(0,50)
    if self.iterador==num:
      bonusObj.lancaBonus()
      print(str(self.iterador))
      print(str(num))
      print(str(len(vetor_bonus)))
      self.iterador = -1
    if self.iterador>limite:
      self.iterador=-1  
  
  def lancaBonus(self):
    print(str(lancador_bonus))
    if lancador_bonus == True:
      posicao = randint(60,540)
      bonusPosicao = randint(0,len(bonus_v)-1)
      vetor_bonus.append(bonus_v[bonusPosicao])
      vetor_bonus_posicao_y.append(posicao)
      vetor_bonus_posicao_x.append(1300)
      
  def moveBonus(self, k):
    i = 0
    if (len(vetor_bonus) < k+1): 
      while i<(len(vetor_bonus)):
        vetor_bonus_posicao_x[i] += VELOCIDADE_BONUS
        screen.blit(vetor_bonus[i],(vetor_bonus_posicao_x[i], vetor_bonus_posicao_y[i]))
        i+=1  



    


elementos = ElementosTela()

while tela_inicial:

        #Handle Input Events
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()            
    if event.type == pygame.KEYDOWN:
        if event.key == K_SPACE:
          if menu_pos_selecionada == 0:
            tela_inicial = False 
            fase_1 = True 
          if menu_pos_selecionada == 1:
            tela_inicial = False   
        
        if event.key == K_DOWN:
          menu_pos_selecionada+=1
          if menu_pos_selecionada >2:
            menu_pos_selecionada = 2
        if event.key == K_UP:
          menu_pos_selecionada-=1
          if menu_pos_selecionada < 0:
            menu_pos_selecionada = 0  
        
  screen.blit(background_inicio, (0, 0))
  elementos.carregaElementosTelaInicial()
  elementos.navegaMenu(menu_pos_selecionada)
  pygame.display.flip()






player = Player()
inimigoObj = Inimigos()
bonusObj = Bonus()

while fase_1:
    
    
   
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
        pos_y -= velocidade_player  
    if movimento_positivo == False:
        pos_y += 50
   
    if temporizador == 0:
      break
      
    if pos_y <60:
      pos_y =60
    if pos_y > 500:
      pos_y = 500   
     
#       elif event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_w or event.key == pygame.K_UP :
#             pos_y -= 10
#             
#         elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
#             pos_y +=10
   
    if (len(vetor_bonus) < 3):
      lancador_bonus = True
    else:
      lancador_bonus = False  
   
    bonusObj.iterador+=1
    bonusObj.deletaBonus()
    bonusObj.sorteiaBonus()
    
    
    energia = bonusObj.energia
    if energia <0:
      energia = 0
    
    if (len(vetor_inimigos_ativos) < 4    ):
      lancador_inimigos = True
    else:
      lancador_inimigos = False  
   
   # inimigoObj.verificaColisao(pos_y)
    inimigoObj.iterador+=1
    inimigoObj.deletaInimigo()
    inimigoObj.sorteiaInimigo()
    
      
              
        
    if (pos_sprite > len(sprites) -1):
          
          pos_sprite = 0
        
    
    screen.blit(background,[0,50])
    pygame.draw.rect(screen, BLACK,(0,0,1200,50))
    
    #pegar tamanho varaiavel, ver se ja liberou espaco, depois blitar proxima imagem. colocar velocidade movimento, *criar vetores com nuvem, controlar elas
    screen.blit(sprites[pos_sprite], (pos_x, pos_y)) 
    #elementos.escreverNomeFase()
    bonusObj.moveBonus(3)
    inimigoObj.moveInimigo(5)
    screen.blit(relogio, (1035,7))
    timer1 = elementos.font_3.render(str(temporizador), True, (WHITE))
    screen.blit(timer1, (1110, 10))
    fase = elementos.font_3.render("Fase 1", True, (WHITE)) 
    screen.blit(fase, (50, 10))
    score = elementos.font_3.render("Placar: ", True, (WHITE)) 
    screen.blit(score,(850,10))
    pontos = elementos.font_3.render(str(player.pontos), True, (YELLOW))
    screen.blit(pontos,(960,10))
    elementos.carregaBarraEnergia(elementos.calculaBarraEnergia(energia))
    
    
    pygame.display.flip()      
    pos_sprite+=1
    clock.tick(60)
    
    
       
    


frame = pygame.draw.rect(screen, (WHITE), Rect((0, 0), (800, 600)))





