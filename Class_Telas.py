import pygame

TEMPLATE_GAME = [['B', 'B', 'B', 'B', 'B', 'B','B', 'B', 'B', ],
                ['B', 'A', 'N', 'VD', 'N', 'VE', 'N', 'CP', 'B'],
                ['B', 'N', 'T', 'T', 'T', 'T', 'T', 'N', 'B'],
                ['B', 'N', 'T', 'T', 'T', 'T', 'T', 'N', 'B'],
                ['B', 'N', 'T', 'T', 'T', 'T', 'T', 'N', 'B'],
                ['B', 'N', 'T', 'T', 'T', 'T', 'T', 'N', 'B'],
                ['B', 'N', 'T', 'T', 'T', 'T', 'T', 'N', 'B'],
                ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
                ['P', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'P'],
                ['R', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'R'],
                ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]

BG_CORES = {'B' : (50, 50, 50),
            'A' : (217, 131, 121),
            'VD' : (129, 202, 212),
            'VE' : (212, 187, 129),
            'CP' : (129, 189, 123),
            'T' : (163, 163, 163),
            'I' : (212, 212, 212),
            'N' : (250,250,250),
            'P' : (0,255,0),
            'R' : (255,0,0),}

TILE_RECT = {'A' : 0,
            'VD' : 0,
            'VE' : 0,
            'CP' : 0}
# B = BORDER
# A = ANDAR
# VD = VIRAR DIREITA
# VE = VIRAR ESQUERDA
# CP = COLETAR PONTOS
# T = TABULEIRO
# I = INPUT
# N = NADA
# P = PLAY
# R = RESET

class Telas:
    def __init__(self, TILE_SIZE, window):
        self.tile_size = TILE_SIZE
        self.game_template = TEMPLATE_GAME
        self.tile_rect = TILE_RECT

        self.tile_play = []
        self.tile_reset = []
        self.tile_outside_T = []
        
        self.rect_inputs = []
        self.game_inputs = []
        self.play = False

        self.window = window

        self.message = ''

        self.tile_xsize = self.tile_size * 9
        self.tile_ysize = self.tile_size * 11
        #IMAGENS
        self.images = {'foward': self.arruma_imagem('assets/Images/foward.png'),
                    'turnR': self.arruma_imagem('assets/Images/turnR.png'),
                    'turnL': self.arruma_imagem('assets/Images/turnL.png'),
                    'collect': self.arruma_imagem('assets/Images/collect.png'),}

    def game_window(self):
        y=0
        for l in range(len(self.game_template)):
            x = 0
            for c in range(len(self.game_template[l])):
                for tile, color in BG_CORES.items():
                    if tile == self.game_template[l][c]:
                        self.window.fill(color, pygame.Rect(x,y,self.tile_size,self.tile_size))

                        if tile == 'N' or tile == 'VD' or tile == 'VE':
                            self.tile_outside_T.append(pygame.Rect(x,y,self.tile_size,self.tile_size))




                        if tile == 'P' and len(self.tile_play) < 2:
                            self.tile_play.append((x,y,self.tile_size,self.tile_size))
                        elif tile == 'R' and len(self.tile_reset) < 2:
                            self.tile_reset.append((x,y,self.tile_size,self.tile_size))
                        if tile == 'I' and len(self.rect_inputs) < 14:
                            self.rect_inputs.append((x,y,self.tile_size,self.tile_size))
                        if tile != 'B' and tile != 'N' and tile != 'T':
                            pygame.draw.rect(self.window, BG_CORES['B'], pygame.Rect(x,y,self.tile_size,self.tile_size),1)
                        if tile in self.tile_rect:
                            self.tile_rect[tile] = (x,y,self.tile_size,self.tile_size)
                            if tile == 'A':
                                self.window.blit(self.images['foward'],(x+10,y+10))
                            elif tile == 'VD':
                                self.window.blit(self.images['turnR'],(x+10,y+10))
                            elif tile == 'VE':
                                self.window.blit(self.images['turnL'],(x+10,y+10))
                            elif tile == 'CP':
                                self.window.blit(self.images['collect'],(x+10,y+10))

                x += self.tile_size
            y += self.tile_size
            
        for tile, color in BG_CORES.items():
            for i, inputs in enumerate(self.game_inputs):
                if inputs == tile:
                    self.window.fill(color, pygame.Rect(self.rect_inputs[i]))
                    if tile == 'A':
                        self.window.blit(self.images['foward'],(self.rect_inputs[i][0]+10,self.rect_inputs[i][1]+10))
                    elif tile == 'VD':
                        self.window.blit(self.images['turnR'],(self.rect_inputs[i][0]+10,self.rect_inputs[i][1]+10))
                    elif tile == 'VE':
                        self.window.blit(self.images['turnL'],(self.rect_inputs[i][0]+10,self.rect_inputs[i][1]+10))
                    elif tile == 'CP':
                        self.window.blit(self.images['collect'],(self.rect_inputs[i][0]+10,self.rect_inputs[i][1]+10))



    def exibir_movimentos(self, event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for coordenadas in self.tile_play:
                rect_play = pygame.Rect(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],)
                if rect_play.collidepoint(event.pos):
                    self.play = True
            for coordenadas in self.tile_reset:
                rect_reset = pygame.Rect(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],)
                if rect_reset.collidepoint(event.pos):
                    self.game_inputs.clear()
                    self.play = False
            for movimento , valores in self.tile_rect.items():
                rect__input = pygame.Rect(valores[0],valores[1],valores[2],valores[3])
                
                if rect__input.collidepoint(event.pos):
                    if len(self.game_inputs) < 14:
                        if movimento == 'A':
                            self.game_inputs.append('A')
                        elif movimento == 'VD':
                            self.game_inputs.append('VD')
                        elif movimento == 'VE':
                            self.game_inputs.append('VE')
                        elif movimento == 'CP':
                            self.game_inputs.append('CP')


        
    def arruma_imagem(self, caminho):
        image = pygame.image.load(caminho)
        return pygame.transform.scale(image, (self.tile_size -20,self.tile_size-20))