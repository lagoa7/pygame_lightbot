import time
from numpy import False_
import pygame
from Class_Telas import Telas

ORIENTACOES = ['R','R','R','D','D','R']
PONTOS = [0,0,1,2,2,2]
FASES = [[['T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T'],
        ['S', 'C', 'C', 'C', 'F'],
        ['T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T']],

        [['T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T'],
        ['S', 'C', 'T', 'C', 'F'],
        ['T', 'C', 'C', 'C', 'T'],
        ['T', 'T', 'T', 'T', 'T']],

        [['T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T'],
        ['S', 'C', 'P', 'C', 'F'],
        ['T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T']],

        [['T', 'S', 'T', 'F', 'T'],
        ['T', 'C', 'T', 'C', 'T'],
        ['T', 'C', 'T', 'C', 'T'],
        ['T', 'C', 'T', 'C', 'T'],
        ['T', 'P', 'C', 'P', 'T']],

        [['T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'P', 'C', 'F'],
        ['S', 'T', 'C', 'T', 'T'],
        ['C', 'C', 'P', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T']],

        [['T', 'T', 'T', 'C', 'F'],
        ['T', 'T', 'T', 'P', 'T'],
        ['T', 'C', 'C', 'C', 'T'],
        ['T', 'P', 'T', 'T', 'T'],
        ['S', 'C', 'T', 'T', 'T']]]


CORES = {'C' : (179, 111, 201),
            'P' : (124, 36, 150),
            'S' : (227, 227, 227),
            'F' : (81, 81, 81),
            'T' : (163, 163, 163),}



class Tabuleiro:
    def __init__(self,TILE_SIZE,window,tela):
        self.tela = tela
        self.game_inputs = self.tela.game_inputs

        self.tile_size = TILE_SIZE
        self.fases = FASES
        self.pontos = PONTOS
        self.window = window
        self.tile_xsize = self.tile_size * 5
        self.tile_ysize = self.tile_size * 5
        self.player_tile = [0,0]
        self.spawn_tile = [0,0]

        self.contador = 0
        self.fase_atu = 0
        self.qtd_fase = len(self.fases)
        print(self.qtd_fase)
        self.pontos_atu = 0

        self.game_end = False

        self.end_tile = None
        self.point_tile = []
        self.tabu_tile = []

        self.font = pygame.font.Font('assets/Fonts/Pokemon_solid.ttf',self.tile_size-50)
        self.text_pontos = self.font.render(str(self.pontos_atu), True, (255, 255, 255))
        self.text_width = self.text_pontos.get_width()

        self.orientacoes = ORIENTACOES
        self.personagem_U = pygame.image.load("assets/Images/character_U.png")
        self.personagem_R = pygame.image.load("assets/Images/character_R.png")
        self.personagem_D = pygame.image.load("assets/Images/character_D.png")
        self.personagem_L = pygame.image.load("assets/Images/character_L.png")
        self.pokebola = pygame.image.load('assets/Images/pokeball.png')


    def tabuleiro_window(self):
        y = self.tile_size * 2
        if self.fase_atu  == self.qtd_fase:
                return True
        for l in range(len(self.fases[self.fase_atu])):
            x = self.tile_size * 2
            for c in range(len(self.fases[self.fase_atu][l])):
                for tile, color in CORES.items():
                    if tile == self.fases[self.fase_atu][l][c]:
                        self.window.fill(color, pygame.Rect(x,y,self.tile_size,self.tile_size))
                        if self.contador < 1:
                            self.text_pontos = self.font.render(str(self.pontos_atu), True, (255, 255, 255))
                            if tile == 'P':
                                self.point_tile.append(pygame.Rect(x,y,self.tile_size,self.tile_size))

                            elif tile == 'F':
                                self.end_tile = pygame.Rect(x,y,self.tile_size,self.tile_size)
                            elif tile == 'T':
                                self.tabu_tile.append(pygame.Rect(x,y,self.tile_size,self.tile_size))
                            elif tile == 'S':
                                self.spawn_tile = [x,y]
                                self.player_tile = [x,y]
                                self.orientacao_personagem()
                            
                        if tile != 'T':
                            pygame.draw.rect(self.window, (50, 50, 50), pygame.Rect(x,y,self.tile_size,self.tile_size),1)
                          
                x += self.tile_size
            y += self.tile_size
        self.contador += 1
        if self.tela.play == True and self.contador >= 1:
            self.contador +=1
            self.movimenta_personagem()
            
        self.desenha_pontos()
        self.desenha_personagem()
        self.game_end = self.tile_check()
        self.window.blit(self.text_pontos,(self.tile_size*4+ self.text_width,self.tile_size/3))
        return self.game_end
        
        

    # Verificador de Tile
    # Ver em qual tile o personagel esta
    # Se estiver em um tile de Tabuleiro parar o jogo
    # Se estiver em tile de pontos e coletar o ponto sumir a pokebola
    # Se chegar na casa final coletando todos os pontos se houver mudar de fase


    def tile_check(self):
        for tabuleiro in self.tabu_tile:
            if tabuleiro.collidepoint(self.player_tile):
                self.contador = 0
                self.tela.play = False
                self.pontos_atu = 0
                self.game_inputs.clear()
                self.tela.game_inputs.clear()
        if self.fase_atu  == self.qtd_fase:
            return True
            
        if self.end_tile.collidepoint(self.player_tile) and self.pontos_atu == self.pontos[self.fase_atu] and len(self.game_inputs) == 0:
            time.sleep(1)
            self.contador = 0
            self.tela.play = False
        
            self.fase_atu += 1
            self.point_tile.clear()
            self.tabu_tile.clear()
            self.pontos_atu = 0
            self.game_inputs.clear()
            self.tela.game_inputs.clear()
        # testa colisao do quadrado seguido do fim
        # next_end = (self.end_tile[0]+self.tile_size,self.end_tile[1],self.end_tile[2])
        for tiles in self.tela.tile_outside_T:
            if tiles.collidepoint(self.player_tile):
                self.contador = 0
                self.tela.play = False
                self.pontos_atu = 0
                self.game_inputs.clear()
                self.tela.game_inputs.clear()



    def desenha_personagem(self):
        if self.contador == 1:
            if self.ori_per == 'R':
                self.window.blit(self.personagem_R, (self.player_tile[0]+10,self.player_tile[1]+5))
            elif self.ori_per == 'D':
                self.window.blit(self.personagem_D, (self.player_tile[0]+10,self.player_tile[1]+5))


        elif self.contador > 1:
            if self.ori_per == 'R':
                self.window.blit(self.personagem_R, (self.player_tile[0]+10,self.player_tile[1]+5))
            elif self.ori_per == 'D':
                self.window.blit(self.personagem_D, (self.player_tile[0]+10,self.player_tile[1]+5))
            elif self.ori_per == 'L':
                self.window.blit(self.personagem_L, (self.player_tile[0]+10,self.player_tile[1]+5))
            elif self.ori_per == 'U':
                self.window.blit(self.personagem_U, (self.player_tile[0]+10,self.player_tile[1]+5))
    
    def desenha_pontos(self):
        for tile_pontos in self.point_tile:
            self.window.blit(self.pokebola,(tile_pontos[0]+10,tile_pontos[1]+10))
            

    def orientacao_personagem(self):
        self.ori_per = self.orientacoes[self.fase_atu]

    def muda_fase(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if self.fase_atu != self.qtd_fase:
                    self.fase_atu += 1
                    self.contador=0
                    self.point_tile.clear()
                    self.tabu_tile.clear()

    def movimenta_personagem(self):
        if len(self.game_inputs) != 0:
            if self.game_inputs[0] == 'A':
                if self.ori_per == 'R':
                    self.player_tile[0] += self.tile_size
                elif self.ori_per == 'D':
                    self.player_tile[1] += self.tile_size
                elif self.ori_per == 'L':
                    self.player_tile[0] -= self.tile_size
                elif self.ori_per == 'U':
                    self.player_tile[1] -= self.tile_size
            elif self.game_inputs[0] == 'VD':
                self.define_orientacao_VD()
            elif self.game_inputs[0] == 'VE':
                self.define_orientacao_VE()
            elif self.game_inputs[0] == 'CP':
                for i, tile in enumerate(self.point_tile):
                    if tile.collidepoint(self.player_tile):
                        self.point_tile.pop(i)
                        self.pontos_atu += 1
                        self.text_pontos = self.font.render(str(self.pontos_atu), True, (255, 255, 255))
                time.sleep(0.25)
            self.game_inputs.pop(0)
            time.sleep(0.25)
        else:      
            time.sleep(2)
            self.tela.play = False
            self.player_tile = self.spawn_tile
            self.contador = 0
            self.pontos_atu = 0
            self.text_pontos = self.font.render(str(self.pontos_atu), True, (255, 255, 255))

    def trata_imagem(self):
        self.personagem_R = pygame.transform.scale(self.personagem_R, (self.tile_size-20,self.tile_size-10))
        self.personagem_U = pygame.transform.scale(self.personagem_U, (self.tile_size-20,self.tile_size-10))
        self.personagem_L = pygame.transform.scale(self.personagem_L, (self.tile_size-20,self.tile_size-10))
        self.personagem_D = pygame.transform.scale(self.personagem_D, (self.tile_size-20,self.tile_size-10))
        self.pokebola = pygame.transform.scale(self.pokebola, (self.tile_size-20,self.tile_size-20))
        self.pokebola = pygame.transform.flip(self.pokebola, True, False)

    def define_orientacao_VD(self):
        
        if self.ori_per == 'R':
            self.ori_per = 'D'
        elif self.ori_per == 'D':
            self.ori_per = 'L'
        elif self.ori_per == 'L':
            self.ori_per = 'U'
        elif self.ori_per == 'U':
            self.ori_per = 'R'

    def define_orientacao_VE(self):
        if self.ori_per == 'R':
            self.ori_per = 'U'
        elif self.ori_per == 'U':
            self.ori_per = 'L'
        elif self.ori_per == 'L':
            self.ori_per = 'D'
        elif self.ori_per == 'D':
            self.ori_per = 'R'