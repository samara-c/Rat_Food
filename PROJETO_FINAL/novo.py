import sys
import pygame 
from pygame.locals import *
from random import *
import math
from pygame import mixer
from pygame.version import PygameVersion
from pygame.display import flip


pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Rat Food')


TAMANHO_TELA_X = 1200
TAMANHO_TELA_Y = 650

TAMANHO_INIMIGO_X = 100
TAMANHO_INIMIGO_Y = 100

velocidade_bonus = -2
velocidade_inimigo = -2

screen = pygame.display.set_mode((TAMANHO_TELA_X,TAMANHO_TELA_Y))


TAMANHO_PLAYER_X = 140
TAMANHO_PLAYER_Y = 140


vator_bonus_pontos = []
vetor_bonus =  []
vetor_bonus_posicao_y = []
vetor_bonus_posicao_x = []
vetor_bonus_velocidade = []
bonus_v = []
bonus_pontos = []
bonus_pos = []


   
vetor_inimigos = []
vetor_inimigos_pontos = []
vetor_inimigos = []
vetor_inimigos_posicao_x = []
vetor_inimigos_posicao_y = []
vetor_inimigos_velocidade = []
vetor_inimigos_ativos = []
vetor_direcionais = []
pos_inimigos = []
sprites = []
pos_sprite = 0
pos_x = 35
pos_y = 100
clock = pygame.time.Clock()
vetor_bg = []
iniciar_musica = True
vetor_ajustes = []




BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (243, 255, 43)
RED = (255, 74, 73)
DARK_BLUE = (15, 41, 71)
BLUE = (49,171,232)
GREEN = (71,255,43)
PURPLE = (126,31,235)
DARK_RED = (214,11,9)
TAMANHO_FONTE_FASES = 200  

movimento_positivo = False

relogio = pygame.image.load('elements//clock.png').convert_alpha()
relogio = pygame.transform.scale(relogio, (90, 40)) 


background = pygame.image.load('elements//bg11.jpg').convert()
background = pygame.transform.scale(background, (TAMANHO_TELA_X, TAMANHO_TELA_Y - 50))
background_2 = pygame.transform.scale(background, (TAMANHO_TELA_X, TAMANHO_TELA_Y - 50)) 
background_inicio = background = pygame.transform.scale(background, (TAMANHO_TELA_X, TAMANHO_TELA_Y)) 
vetor_bg.append(background)
vetor_bg.append(background_2)

icone = pygame.image.load("elements//rato.png").convert()
pygame.display.set_icon(icone)



fase_1 = False  
fase_2 = False 
fase_3 = False
tela_inicial = True
tela_ajustes = False
tela_nome = False
tela_trofeu = False
menu_pos_selecionada = 0
menu_ajustes_selecionado = 0
tela_fase_1 = False

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) 
temporizador = 60

lancador_bonus = True
lancador_inimigos = True

opcao_iniciar_menu = True
opcao_instrucoes_menu = False
opcao_ajustes_menu = False
som_elemento = True

POSICOES = [120,270,390,540]
  

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
    
    self.velocidade_player = 8
    self.peso_player = 8
    self.pontos = 0
    self.energia=1000

  def checaPosicao(self, pos_x, pos_y):
    if pos_y <60:
      pos_y =60
    if pos_y > 500:
      pos_y = 500   
    if pos_x < 35:
      pos_x = 35       
    if pos_x > 1000:
      pos_x = 1000     
    return pos_x, pos_y  

class Ranking():
  def __init__(self):
    self.path = "ranking//"
    self.arquivo = self.path+"ranking.txt"
    self.pontuacao = ""
    self.jogador = ""
    
         
  
  def leRanking(self): 
    self.arquivo_ranking = open(self.arquivo, 'r')
    print(self.arquivo_ranking.readlines())
    self.arquivo_ranking.close()
  
  
 
      
      
  
      
class ElementosTela() :
  
  def __init__(self):
    self.path = "fonts//"
    self.path_elements = "elements//"
    
    self.font_1 = pygame.font.Font(self.path+"Candy Beans.otf", 20)
    self.font_2 = pygame.font.Font(self.path+"No Virus.ttf", 20)
    self.font_3 = pygame.font.Font(self.path+"MilkyNice.ttf", 30)
    self.font_4 = pygame.font.Font(self.path+"MilkyNice.ttf", 36)
    self.font_titulo = pygame.font.Font(self.path+"PaperPlane-jE1R7.otf", 110)
    self.rato = pygame.image.load("player//"+'RatPilot1.png').convert_alpha()
    self.rato = pygame.transform.scale(self.rato, (200, 200))
    self.rato_1 = pygame.transform.scale(self.rato, (80, 80))
    
    self.font_fases = pygame.font.Font("fonts//HARD ROCK.ttf", TAMANHO_FONTE_FASES)
    
    
    self.font_fases2 = pygame.font.Font("fonts//Cotton Cloud.ttf", TAMANHO_FONTE_FASES)
    self.font_fases3 = pygame.font.Font("fonts//HARD ROCK.ttf", TAMANHO_FONTE_FASES)
    
    self.font = pygame.font.SysFont('sans',26)
    
    self.nuvem = pygame.image.load(self.path_elements+'cloud_inicio.png').convert_alpha()
    self.nuvem = pygame.transform.scale(self.nuvem, (960,505)) 
    
    self.posicao_item = 340
    
    self.text_iniciar = "Iniciar"
    self.texto_instrucoes = "Como jogar"
    self.texto_ajustes = "Ajustes"
    
    # AJUSTES
    
    self.posicao_som = 420
    self.posicao_idioma = 450
    self.continuar = "Continuar"
    self.texto_fim = "Agradecemos sua ajuda, copiloto "
    self.texto_pontos = "Voce fez "
    self.vamos = "Decolar!"
    self.bem_vindo = "Bem vindo, copiloto!"
    self.como_se_chama = "Como podemos te chamar?"
    self.som = "Som :"
    self.idioma = "Idioma : "
    self.som_true = " Ligado"
    self.som_false = " Desligado"
    self.idioma_pt = " PT-BR"
    self.idioma_en = " EN"
    self.voltar = "Voltar"
    self.instrucoes_completas = "Utilize as setas do seu teclado"
    self.instrucoes_completas_2 = " para mover o Alfredo e pegar os alimentos saudaveis"
    self.iterador_idioma = 0
    self.tocar = True
    self.sound_inst = pygame.mixer.Sound("como_jogar.mp3")
    
    self.energia_icone = pygame.image.load(self.path_elements+'energy.png').convert_alpha()
    self.energia_icone = pygame.transform.scale(self.energia_icone, (35,35))
    self.tamanho_barra = 100 
    
    
    self.note_2 = pygame.image.load(self.path_elements+'note_2.png').convert_alpha()
    self.note_2 = pygame.transform.scale(self.note_2, (700,700))
    
    #ELEMENTOS SONOROS
    self.som_ligado = True
    
    
    self.posicao_bg_1 = 0
    self.posicao_bg_2 = 1200
    
    self.player_name = "JOGADOR"
  
    self.trophy = pygame.image.load(self.path_elements+'Trofeu.png').convert_alpha()
    self.trophy = pygame.transform.scale(self.trophy, (400,400))
    
    #DIRECIONAIS
    self.escala = (200,120)
    
    self.direcional_direito = pygame.image.load(self.path_elements+'Direcional_Direita.png').convert_alpha()
    self.direcional_direito = pygame.transform.scale(self.direcional_direito, self.escala)
    
    self.direcional_esquerdo = pygame.image.load(self.path_elements+'Direcional_Esquerda.png').convert_alpha()
    self.direcional_esquerdo = pygame.transform.scale(self.direcional_esquerdo, self.escala)
    
    self.direcional_cima = pygame.image.load(self.path_elements+'Direcional_Cima.png').convert_alpha()
    self.direcional_cima = pygame.transform.scale(self.direcional_cima, self.escala)
    
    self.direcional_baixo = pygame.image.load(self.path_elements+'Direcional_Baixo.png').convert_alpha()
    self.direcional_baixo = pygame.transform.scale(self.direcional_baixo, self.escala)
    
    self.bonus1 = pygame.image.load("bonus//banana.png").convert_alpha()
    self.bonus1 = pygame.transform.scale(self.bonus1, (30, 30 ))
    
    vetor_direcionais.append(self.direcional_esquerdo)
    vetor_direcionais.append(self.direcional_cima)
    vetor_direcionais.append(self.direcional_direito)
    vetor_direcionais.append(self.direcional_baixo)
    
    self.pos_teclado = (610,180)
    self.pos_iterador = 0
    self.pos_relativa_x, self.pos_relativa_y = 450,190
     
  def checaPos(self):
      self.pos_iterador+=1
      if self.pos_iterador > 4000:
          self.pos_iterador = 0
  
  def carregaImagemDirecionais (self , pos):
   elementos.checaPos()   
   if (pos>=0 and pos<=1000):
       screen.blit(vetor_direcionais[0], self.pos_teclado)
       screen.blit(self.bonus1, (self.pos_relativa_x, self.pos_relativa_y))
       screen.blit(self.rato_1, (self.pos_relativa_x - 100, self.pos_relativa_y-10))
   
   if (pos>=1001 and pos<=2000):
       screen.blit(vetor_direcionais[1], self.pos_teclado)
       screen.blit(self.bonus1, (self.pos_relativa_x, self.pos_relativa_y))
       screen.blit(self.rato_1, (self.pos_relativa_x-20, self.pos_relativa_y-100))
       
   if (pos>=2001 and pos<=3000):
       screen.blit(vetor_direcionais[2], self.pos_teclado)
       screen.blit(self.bonus1, (self.pos_relativa_x, self.pos_relativa_y))
       screen.blit(self.rato_1, (self.pos_relativa_x+50, self.pos_relativa_y-10))
       
   if (pos>=3001 and pos<=4000):
       screen.blit(vetor_direcionais[3], self.pos_teclado)        
       screen.blit(self.bonus1, (self.pos_relativa_x, self.pos_relativa_y))   
       screen.blit(self.rato_1, (self.pos_relativa_x-20, self.pos_relativa_y+50))
      
  def exibePontos (self, pontos):   
   screen.blit(self.trophy, (400,40))
   texto_pontos = self.texto_pontos+str(player.pontos)+" pontos"
   texto_fim = self.texto_fim+self.player_name.upper()+"!"   
   texto = self.font_3.render(texto_fim, True, (BLACK))
   texto_2 = self.font_3.render(texto_pontos, True, (BLACK))
   texto_3 = self.font_4.render(self.continuar, True, (BLUE)) 
   screen.blit(texto, (285,450))
   screen.blit(texto_2, (475,480))
   screen.blit(texto_3, (550,550))
   
   print(str(player.pontos))   
  
  def carregaTelaJogador(self):  
   screen.blit(self.note_2,(250,-60))
   texto = self.font_3.render(self.bem_vindo, True, (BLACK))
   texto_2 = self.font_3.render(self.como_se_chama, True, (BLACK))
   texto_3 = self.font_4.render(self.vamos, True, (BLUE))
    
   screen.blit(texto,(460, 170))
   screen.blit(texto_2,(410,220))
   screen.blit(texto_3,(545,460)) 
      
        
  
  def leNomeJogador(self, key):
      if (len(self.player_name) < 8):
          self.player_name+=str(key)
      
      
  def escreveNomeJogador(self):
      texto = self.font_4.render(self.player_name.upper(), True, (DARK_RED))
      screen.blit(texto,(525,300))
      
  
    
  def tocarInstrucoes(self):
    if self.som_ligado and self.tocar:        
      pygame.mixer.find_channel().play(self.sound_inst)     
      self.tocar = False
  # def pararInstrucoes(self):
  #   pygame.mixer.       
  def carregaInstrucoes(self):
    texto_instrucoes = self.font_3.render(self.instrucoes_completas, True, (BLACK))
    texto_instrucoes_2 = self.font_3.render(self.instrucoes_completas_2, True, (BLACK))
    texto_voltar = self.font_4.render(self.voltar, True, (BLUE))
    screen.blit(texto_instrucoes,(self.posicao_idioma-80,self.posicao_item-10))
    screen.blit(texto_instrucoes_2,(self.posicao_idioma-250,self.posicao_item+30))
    screen.blit(texto_voltar,(self.posicao_idioma+120,self.posicao_item+100))   
 
  def carregaAjustes(self):
    texto_voltar = self.font_4.render(self.voltar, True, (BLACK))
    texto_som =  self.font_4.render(self.som, True, (BLACK))
    texto_idioma = self.font_4.render(self.idioma, True, (BLACK))
    opcao_ligado =  self.font_4.render(self.som_true, True, (BLACK))
    opcao_desligado =  self.font_4.render(self.som_false, True, (BLACK))
    barra =  self.font_4.render("/", True, (BLACK))
    texto_pt =  self.font_4.render(self.idioma_pt, True, (BLACK))
    texto_en = self.font_4.render(self.idioma_en, True, (BLACK)) 
                   
      
    screen.blit(texto_som,(self.posicao_som,self.posicao_item-50))
    screen.blit(opcao_ligado,(self.posicao_som+100,self.posicao_item-50))
    screen.blit(barra,(self.posicao_som+240,self.posicao_item-50))
    screen.blit(opcao_desligado,(self.posicao_som+260,self.posicao_item-50))
    screen.blit(texto_idioma,(self.posicao_idioma,self.posicao_item-100))
    screen.blit(texto_pt,(self.posicao_idioma+140,self.posicao_item-100))
    screen.blit(barra,(self.posicao_idioma+270,self.posicao_item-100))
    screen.blit(texto_en,(self.posicao_idioma+285,self.posicao_item-100))
    screen.blit(texto_voltar,(self.posicao_idioma+120,self.posicao_item+100))
    
  def navegaMenuAjustesIdioma(self,pos):
    if pos == 0:
      opcao_ligado =  self.font_4.render(self.som_true, True, (BLUE))
      screen.blit(opcao_ligado,(self.posicao_som+100,self.posicao_item-50))
    elif pos == 1:
      opcao_desligado =  self.font_4.render(self.som_false, True, (BLUE))
      screen.blit(opcao_desligado,(self.posicao_som+260,self.posicao_item-50))
    elif pos == 2:
      texto_voltar =  self.font_4.render(self.voltar, True, (BLUE))
      screen.blit(texto_voltar,(self.posicao_idioma+120,self.posicao_item+100))
      
      
  def checaSom(self, som):
    if som == True:  
      self.tocarMusica()
    if som == False:
      self.pararMusica()  
      
      
  def tocaSomBonus(self, som):
      if som == True:
          sound1 = pygame.mixer.Sound("bonus.WAV")
          pygame.mixer.find_channel().play(sound1)
          
  def tocaSomInimigo(self, som):
      if som == True:
          sound2 = pygame.mixer.Sound("enemy.WAV")
          pygame.mixer.find_channel().play(sound2)
  
  def tocarMusica(self):
      mixer.init()
      mixer.music.load('principal.mp3')
      mixer.music.set_volume(0.2)
      mixer.music.play(loops = 30, start = 0.0)
      
   
  def pararMusica(self):
      mixer.music.stop() 
  
  
  def reiniciar_vetores_e_pontos(self):
    lancador_bonus = True 
    lancador_inimigos = True
    c = 0
    while c < (len(vetor_inimigos_ativos)):
        vetor_inimigos_posicao_x[c] = 1300
        c+=1    
    c = 0
    while c < (len(vetor_bonus)):
        vetor_bonus_posicao_x[c] = 1300
        c+=1  
        
  def carregaElementosTelaInicial(self):
    screen.blit(self.nuvem, (120,55))
    screen.blit(self.rato, (520,30))
    elementos.carregaMenu()
 
  def carregaElementosBase(self):
    screen.blit(self.nuvem, (120,55))
    
    
  def moveBG(self, velocidade = 1, inicio = False):
    posicao_default = 50
    if inicio:
      posicao_default = 0
    screen.blit(vetor_bg[0],(self.posicao_bg_1,posicao_default))
    screen.blit(vetor_bg[1],(self.posicao_bg_2,posicao_default))
    
    if self.posicao_bg_1 <=-1200:
      self.posicao_bg_1 = 1200
    else:
      self.posicao_bg_1-=velocidade       
      
    if self.posicao_bg_2 <= -1200:
      self.posicao_bg_2 = 1200
    else:
      self.posicao_bg_2-=velocidade    
    
 
 
  def calculaBarraEnergia (self, valor):
    
    valor = math.ceil(valor/10)
    self.tamanho_barra = valor 
    print("O valor eh"+ str(valor))
    
    if valor >= 66 and valor <= 100:
      cor = GREEN
      player.velocidade_player = 10
      player.peso_player = 10
    elif valor >= 33 and valor <= 65:
      cor = YELLOW
      player.velocidade_player = 4
      player.peso_player = 4
    elif valor >= 0 and valor <= 32:
      cor = RED
      player.velocidade_player = 2
      player.peso_player = 2    
    return cor   
 
  def carregaBarraEnergia(self, cor = GREEN):
    pygame.draw.rect(screen,WHITE,(692,18,112,18), 0)
    pygame.draw.rect(screen,cor,(702,21,self.tamanho_barra,13), 0)
    screen.blit(self.energia_icone, (680,10))
 
  def carregaTitulo(self):
    texto =  self.font_titulo.render("Rat Food", True, (BLACK)) 
    screen.blit(texto,(410,220)) 
    
  def carregaMenu(self, cor = BLACK):
    self.opcao_iniciar =  self.font_4.render(self.text_iniciar, True, (cor))
    self.opcao_instrucoes = self.font_4.render(self.texto_instrucoes, True, (cor))
    self.opcao_ajustes = self.font_4.render(self.texto_ajustes, True, (cor))
    
    screen.blit(self.opcao_iniciar,(560,self.posicao_item))
    screen.blit(self.opcao_instrucoes,(520,self.posicao_item+50))
    screen.blit(self.opcao_ajustes,(550,self.posicao_item+100))
  
  def carregaTelaFase (self, texto, pos_y):
    texto_fase = self.font_3.render(texto, True, (WHITE))
    screen.blit(texto_fase,(550,pos_y))
    
    
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
    
   
   
  def deletaInimigo(self):
    c = 0
    while c < (len(vetor_inimigos_ativos)):
      if (vetor_inimigos_posicao_x[c] < -70):
        del(vetor_inimigos_posicao_x[c])
        del(vetor_inimigos_posicao_y[c])
        del(vetor_inimigos_ativos[c])
        del(vetor_inimigos_velocidade[c])
      c+=1    
    
  def sorteiaInimigo(self):
    limite = 50
    num = randint(0,limite)
    if self.iterador==num:
      inimigoObj.lancaInimigo()
      self.iterador = -1
    if self.iterador>limite:
      self.iterador=-1      

  def lancaInimigo(self):
    if lancador_inimigos == True:
      posicao = POSICOES[randint(0,3)]
      inimigoPosicao = randint(0,len(vetor_inimigos)-1)
      vetor_inimigos_ativos.append(vetor_inimigos[inimigoPosicao])
      vetor_inimigos_posicao_y.append(posicao)
      vetor_inimigos_posicao_x.append(1300)
      valor = randint(0,3)
      vetor_inimigos_velocidade.append(valor)

  def moveInimigo(self, k, fase):
    i = 0
    if (len(vetor_inimigos_ativos) < k+1):
      if (fase == "1"):   
          while i<(len(vetor_inimigos_ativos)):
            vetor_inimigos_posicao_x[i] += velocidade_inimigo-vetor_inimigos_velocidade[i]
            screen.blit(vetor_inimigos_ativos[i],(vetor_inimigos_posicao_x[i], vetor_inimigos_posicao_y[i]))
            i+=1
      elif (fase == "2"):   
          while i<(len(vetor_inimigos_ativos)):
            vetor_inimigos_posicao_x[i] += velocidade_inimigo-2-vetor_inimigos_velocidade[i]
            screen.blit(vetor_inimigos_ativos[i],(vetor_inimigos_posicao_x[i], vetor_inimigos_posicao_y[i]))
            i+=1  
      elif (fase == "3"):   
          while i<(len(vetor_inimigos_ativos)):
            vetor_inimigos_posicao_x[i] += velocidade_inimigo-4-vetor_inimigos_velocidade[i]
            screen.blit(vetor_inimigos_ativos[i],(vetor_inimigos_posicao_x[i], vetor_inimigos_posicao_y[i]))
            i+=1       
  def checaColisaoinimigos (self, image_rect):
    i  = 0
    vetor_colisao = []
    while i < len(vetor_inimigos_ativos):
      var = vetor_inimigos_ativos[i].get_rect(topleft=(vetor_inimigos_posicao_x[i],vetor_inimigos_posicao_y[i]))
      vetor_colisao.append(var)
      i+=1 
    s = 0
    while s<(len(vetor_colisao)):
      if image_rect.colliderect(vetor_colisao[s]):
        del(vetor_inimigos_posicao_x[s])
        del(vetor_inimigos_posicao_y[s])
        del(vetor_inimigos_ativos[s])
        del(vetor_inimigos_velocidade[s])
        player.energia-=10
        elementos.tocaSomInimigo(iniciar_musica)   
      s+=1       
        
  def verificaColisao(self, pos_player):
    i = 0
    while i < (len(vetor_inimigos_ativos)):
      if (vetor_inimigos_posicao_x[i] <= pos_player) and (vetor_inimigos_posicao_y[i] >= 185):
        i+=1
    
          
              


#Controla os bonus
class Bonus():
  def __init__(self):
    self.path = "bonus//"
    self.bonus1 = pygame.image.load(self.path+'banana.png').convert_alpha()
    self.bonus1 = pygame.transform.scale(self.bonus1, (50, 50 ))
        
    self.bonus2 = pygame.image.load(self.path+'apple.png').convert_alpha()
    self.bonus2 = pygame.transform.scale(self.bonus2, (40, 40 ))
    
    self.bonus3 = pygame.image.load(self.path+'grape.png').convert_alpha()
    self.bonus3 = pygame.transform.scale(self.bonus3, (50, 50 ))
    
    self.bonus4 = pygame.image.load(self.path+'strawberry.png').convert_alpha()
    self.bonus4 = pygame.transform.scale(self.bonus4, (30, 30 ))
    
    self.bonus5 = pygame.image.load(self.path+'watermelon.png').convert_alpha()
    self.bonus5 = pygame.transform.scale(self.bonus5, (70, 70 ))
    
    self.bonus6 = pygame.image.load(self.path+'peach.png').convert_alpha()
    self.bonus6 = pygame.transform.scale(self.bonus6, (40, 40 ))
    
    
    
    #Define a quantidade de frutas no vetor, As frutas que valem mais pontos sao mais raras
    bonus_v.append(self.bonus1)
    bonus_v.append(self.bonus1)
    bonus_v.append(self.bonus2)
    bonus_v.append(self.bonus2)
    bonus_v.append(self.bonus3)
    bonus_v.append(self.bonus3)
    bonus_v.append(self.bonus4)
    bonus_v.append(self.bonus4)
    bonus_v.append(self.bonus5)
    bonus_v.append(self.bonus6)

        
    self.iterador = -1
    self.energia = 1000
  
  def deletaBonus(self):
    c = 0
    while c < (len(vetor_bonus)):
      if (vetor_bonus_posicao_x[c] < -70):
        del(vetor_bonus_posicao_x[c])
        del(vetor_bonus_posicao_y[c])
        del(vetor_bonus[c])
        del (vetor_bonus_velocidade[c])
      c+=1  
  
  def sorteiaBonus(self):
    limite = 50
    num = randint(0,50)
    if self.iterador==num:
      bonusObj.lancaBonus()
      
      self.iterador = -1
    if self.iterador>limite:
      self.iterador=-1  
  
  def lancaBonus(self):
    
    if lancador_bonus == True:
      posicao = POSICOES[randint(0,3)]
      bonusPosicao = randint(0,len(bonus_v)-1)
      vetor_bonus.append(bonus_v[bonusPosicao])
      vetor_bonus_posicao_y.append(posicao)
      vetor_bonus_posicao_x.append(1300)
      valor = randint(0,3)
      vetor_bonus_velocidade.append(valor)
      
      
  def moveBonus(self, k, fase):
    i = 0
    if (len(vetor_bonus) < k+1):
      if (fase == "1"):   
          while i<(len(vetor_bonus)):
            vetor_bonus_posicao_x[i] += velocidade_bonus-vetor_bonus_velocidade[i]
            screen.blit(vetor_bonus[i],(vetor_bonus_posicao_x[i], vetor_bonus_posicao_y[i]))
            i+=1  
      elif (fase == "2"):   
          while i<(len(vetor_bonus)):
            vetor_bonus_posicao_x[i] += velocidade_bonus-2-vetor_bonus_velocidade[i]
            screen.blit(vetor_bonus[i],(vetor_bonus_posicao_x[i], vetor_bonus_posicao_y[i]))
            i+=1
      elif (fase == "3"):   
          while i<(len(vetor_bonus)):
            vetor_bonus_posicao_x[i] += velocidade_bonus-4-vetor_bonus_velocidade[i]
            screen.blit(vetor_bonus[i],(vetor_bonus_posicao_x[i], vetor_bonus_posicao_y[i]))
            i+=1          
        
  def checaColisaoBonus (self, image_rect):
    i  = 0
    vetor_colisao = []
    while i < len(vetor_bonus):
      var = vetor_bonus[i].get_rect(topleft=(vetor_bonus_posicao_x[i],vetor_bonus_posicao_y[i]))
      vetor_colisao.append(var)
      i+=1
    try :   
        s = 0
        while s<(i):
          if image_rect.colliderect(vetor_colisao[s]):
            del(vetor_bonus_posicao_x[s])
            del(vetor_bonus_posicao_y[s])
            del(vetor_bonus[s])
            del(vetor_bonus_velocidade[s])
            player.pontos+=5
            elementos.tocaSomBonus(iniciar_musica)   
          s+=1  
    except IndexError:
        print("HOIVE UM ERRO AQUI")
        print (str(i))
        print (str(s))
        
          

rankingObj = Ranking()
elementos = ElementosTela()
elementos.tocarMusica()
while tela_inicial:
  posicao = 400
  
  while opcao_instrucoes_menu:
    if elementos.tocar:
        elementos.tocarInstrucoes()  
    for event in pygame.event.get():   
      if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == K_SPACE:  
            opcao_instrucoes_menu = False 
            elementos.tocar = True        
    elementos.moveBG(1,True)
    elementos.carregaElementosBase()
    elementos.carregaInstrucoes()
    elementos.carregaImagemDirecionais(elementos.pos_iterador)
    
    pygame.display.flip()
    
    
  while opcao_ajustes_menu:
    for event in pygame.event.get():   
      if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == K_RIGHT or event.key == K_DOWN:
          menu_ajustes_selecionado+=1
          if menu_ajustes_selecionado >2:
              menu_ajustes_selecionado=2
        if event.key == K_LEFT or event.key == K_UP:
          menu_ajustes_selecionado-=1
          if menu_ajustes_selecionado <0:
              menu_ajustes_selecionado=0 
        if event.key == K_SPACE:  
          if menu_ajustes_selecionado == 0:
            iniciar_musica = True    
            elementos.checaSom(iniciar_musica)
            rankingObj.leRanking() 
          if menu_ajustes_selecionado == 1:
            iniciar_musica = False    
            elementos.checaSom(iniciar_musica)
            rankingObj.leRanking()   
          if menu_ajustes_selecionado == 2:  
            opcao_ajustes_menu = False
            rankingObj.leRanking()
            
                
    
    elementos.moveBG(1,True)
    elementos.carregaElementosBase()
    elementos.carregaAjustes()
    elementos.navegaMenuAjustesIdioma(menu_ajustes_selecionado)
    pygame.display.flip()
  
  while tela_nome:
   enviar = True     
   for event in pygame.event.get():   
      if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      if event.type == pygame.KEYDOWN:
          
          if event.key == K_SPACE:
              tela_nome = False 
              fase_1 = True
          
          if event.key == K_BACKSPACE:
              elementos.player_name = elementos.player_name[:-1]
              enviar = False       
          
          if event.key == K_CAPSLOCK or event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
              enviar = False
              
          key=event.key
          if enviar:
              elementos.leNomeJogador(chr(key))
              
   elementos.moveBG(1, True)
   elementos.carregaTelaJogador()
   elementos.escreveNomeJogador()
   pygame.display.flip()
  
  while fase_1:
    
    fase = "1"
   
    for event in pygame.event.get():
       
        
        
       
      if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      if event.type == CLOCKTICK:
            temporizador = temporizador -1
                            
    pressed = pygame.key.get_pressed()
      
    pos_y -= (pressed[pygame.K_UP] - pressed[pygame.K_DOWN]) * player.velocidade_player
    pos_y += (pressed[pygame.K_DOWN] - pressed[pygame.K_UP]) * player.peso_player
    pos_x += (pressed[pygame.K_RIGHT] - pressed[pygame.K_LEFT]) * player.velocidade_player
    pos_x -= (pressed[pygame.K_LEFT] - pressed[pygame.K_RIGHT]) * player.peso_player
   
    pos_x, pos_y = player.checaPosicao(pos_x, pos_y)
       
    if temporizador == 0:
      fase_1 = False
      fase_2 = True
      temporizador = 60
      elementos.reiniciar_vetores_e_pontos()
      break
      
    
     
   
    if (len(vetor_bonus) < 3):
      lancador_bonus = True
    else:
      lancador_bonus = False  
   
    bonusObj.iterador+=1
    bonusObj.deletaBonus()
    bonusObj.sorteiaBonus()
    
    
    energia = player.energia
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
        
    elementos.moveBG()
    pygame.draw.rect(screen, BLACK,(0,0,1200,50))
    
    
    
    image_rect = sprites[pos_sprite].get_rect(topleft=(pos_x,pos_y))
    
   
    screen.blit(sprites[pos_sprite], image_rect)  
    bonusObj.checaColisaoBonus(image_rect)
    bonusObj.moveBonus(3, fase)
    inimigoObj.checaColisaoinimigos(image_rect)
    inimigoObj.moveInimigo(5, fase)
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
    

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()            
    if event.type == pygame.KEYDOWN:
        if event.key == K_SPACE:  
          if menu_pos_selecionada == 0:
            tela_nome = True
            player = Player()
            inimigoObj = Inimigos()
            bonusObj = Bonus() 
          if menu_pos_selecionada == 1:
            opcao_instrucoes_menu = True   
          if menu_pos_selecionada == 2:
            opcao_ajustes_menu = True
            
        if event.key == K_DOWN:
          menu_pos_selecionada+=1
          if menu_pos_selecionada >2:
            menu_pos_selecionada = 2
        if event.key == K_UP:
          menu_pos_selecionada-=1
          if menu_pos_selecionada < 0:
            menu_pos_selecionada = 0
  
  
  # INICIO FASE 2          
  while fase_2:
      
    fase_n2 = "2"
     
    for event in pygame.event.get():
        
        
       
      if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      if event.type == CLOCKTICK:
            temporizador = temporizador -1
                            
    pressed = pygame.key.get_pressed()
      
    pos_y -= (pressed[pygame.K_UP] - pressed[pygame.K_DOWN]) * player.velocidade_player
    pos_y += (pressed[pygame.K_DOWN] - pressed[pygame.K_UP]) * player.peso_player
    pos_x += (pressed[pygame.K_RIGHT] - pressed[pygame.K_LEFT]) * player.velocidade_player
    pos_x -= (pressed[pygame.K_LEFT] - pressed[pygame.K_RIGHT]) * player.peso_player
   
    pos_x, pos_y = player.checaPosicao(pos_x, pos_y)
    
    if temporizador == 0:
      fase_2 = False
      fase_3 = True
      temporizador = 60
      elementos.reiniciar_vetores_e_pontos()
      break
      
     
   
    if (len(vetor_bonus) < 3):
      lancador_bonus = True
    else:
      lancador_bonus = False  
   
    bonusObj.iterador+=1
    bonusObj.deletaBonus()
    bonusObj.sorteiaBonus()
    
    
    energia = player.energia
    if energia <0:
      energia = 0
    
    if (len(vetor_inimigos_ativos) < 4):
      lancador_inimigos = True
    else:
      lancador_inimigos = False  
   
   # inimigoObj.verificaColisao(pos_y)
    inimigoObj.iterador+=1
    inimigoObj.deletaInimigo()
    inimigoObj.sorteiaInimigo()
    
      
              
        
    if (pos_sprite > len(sprites) -1):
          
          pos_sprite = 0
        
    elementos.moveBG()
    pygame.draw.rect(screen, BLACK,(0,0,1200,50))
    
    
    
    image_rect = sprites[pos_sprite].get_rect(topleft=(pos_x,pos_y))
    
   
    screen.blit(sprites[pos_sprite], image_rect)  
    bonusObj.checaColisaoBonus(image_rect)
    bonusObj.moveBonus(3, fase_n2)
    inimigoObj.checaColisaoinimigos(image_rect)
    inimigoObj.moveInimigo(5, fase_n2)
    screen.blit(relogio, (1035,7))
    timer1 = elementos.font_3.render(str(temporizador), True, (WHITE))
    screen.blit(timer1, (1110, 10))
    fase = elementos.font_3.render("Fase 2", True, (WHITE)) 
    screen.blit(fase, (50, 10))
    score = elementos.font_3.render("Placar: ", True, (WHITE)) 
    screen.blit(score,(850,10))
    pontos = elementos.font_3.render(str(player.pontos), True, (YELLOW))
    screen.blit(pontos,(960,10))
    elementos.carregaBarraEnergia(elementos.calculaBarraEnergia(energia))
    
    
    pygame.display.flip()      
    pos_sprite+=1
    clock.tick(60)
    
  #INICIO FASE 3  
  while fase_3:
      
        fase_n3 = "3"
         
        for event in pygame.event.get():
            
            
           
          if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          if event.type == CLOCKTICK:
                temporizador = temporizador -1
                                
        pressed = pygame.key.get_pressed()
          
        pos_y -= (pressed[pygame.K_UP] - pressed[pygame.K_DOWN]) * player.velocidade_player
        pos_y += (pressed[pygame.K_DOWN] - pressed[pygame.K_UP]) * player.peso_player
        pos_x += (pressed[pygame.K_RIGHT] - pressed[pygame.K_LEFT]) * player.velocidade_player
        pos_x -= (pressed[pygame.K_LEFT] - pressed[pygame.K_RIGHT]) * player.peso_player
   
        pos_x, pos_y = player.checaPosicao(pos_x, pos_y)
        if temporizador == 0:
          fase_3 = False
          tela_trofeu = True
          temporizador = 60
          elementos.reiniciar_vetores_e_pontos()
          break
          
        if pos_y <60:
          pos_y =60
        if pos_y > 500:
          pos_y = 500   
         
       
        if (len(vetor_bonus) < 3):
          lancador_bonus = True
        else:
          lancador_bonus = False  
       
        bonusObj.iterador+=1
        bonusObj.deletaBonus()
        bonusObj.sorteiaBonus()
        
        
        energia = player.energia
        if energia <0:
          energia = 0
        
        if (len(vetor_inimigos_ativos) < 4):
          lancador_inimigos = True
        else:
          lancador_inimigos = False  
       
       # inimigoObj.verificaColisao(pos_y)
        inimigoObj.iterador+=1
        inimigoObj.deletaInimigo()
        inimigoObj.sorteiaInimigo()
        
          
                  
            
        if (pos_sprite > len(sprites) -1):
              
              pos_sprite = 0
            
        elementos.moveBG()
        pygame.draw.rect(screen, BLACK,(0,0,1200,50))
        
        
        
        image_rect = sprites[pos_sprite].get_rect(topleft=(pos_x,pos_y))
        
       
        screen.blit(sprites[pos_sprite], image_rect)  
        bonusObj.checaColisaoBonus(image_rect)
        bonusObj.moveBonus(3, fase_n3)
        inimigoObj.checaColisaoinimigos(image_rect)
        inimigoObj.moveInimigo(5, fase_n3)
        screen.blit(relogio, (1035,7))
        timer1 = elementos.font_3.render(str(temporizador), True, (WHITE))
        screen.blit(timer1, (1110, 10))
        fase = elementos.font_3.render("Fase 3", True, (WHITE)) 
        screen.blit(fase, (50, 10))
        score = elementos.font_3.render("Placar: ", True, (WHITE)) 
        screen.blit(score,(850,10))
        pontos = elementos.font_3.render(str(player.pontos), True, (YELLOW))
        screen.blit(pontos,(960,10))
        elementos.carregaBarraEnergia(elementos.calculaBarraEnergia(energia))
        
        
        pygame.display.flip()      
        pos_sprite+=1
        clock.tick(60)  
  
  
  while tela_trofeu:
   for event in pygame.event.get():   
      if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      if event.type == pygame.KEYDOWN:
          
          if event.key == K_SPACE:
              tela_trofeu = False 
   
   elementos.moveBG(1, True)              
   elementos.exibePontos(player.pontos)
   pygame.display.flip()   

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()            
    if event.type == pygame.KEYDOWN:
        if event.key == K_SPACE:  
          if menu_pos_selecionada == 0:
            tela_nome = True 
          if menu_pos_selecionada == 1:
            opcao_instrucoes_menu = True
          if menu_pos_selecionada == 2:
            opcao_ajustes_menu = True
                 
        
        if event.key == K_DOWN:
          menu_pos_selecionada+=1
          if menu_pos_selecionada >2:
            menu_pos_selecionada = 2
        if event.key == K_UP:
          menu_pos_selecionada-=1
          if menu_pos_selecionada < 0:
            menu_pos_selecionada = 0            
        
  elementos.moveBG(1, True)
  elementos.carregaElementosTelaInicial()
  elementos.navegaMenu(menu_pos_selecionada)
  elementos.carregaTitulo()
  pygame.display.flip()


frame = pygame.draw.rect(screen, (WHITE), Rect((0, 0), (800, 600)))





