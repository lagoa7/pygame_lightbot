import pygame



class Play:
    def __init__(self, TILE_SIZE ,window):
        self.window = window
        self.tile_size = TILE_SIZE

        self.pokecode = pygame.image.load('assets/Images/PokeCode.png')
        self.pokecode_w = self.pokecode.get_width()

        self.play_font = pygame.font.Font('assets/Fonts/Pokemon_solid.ttf',40)

        self.font = pygame.font.Font('assets/Fonts/OpenSans_regular.ttf',14)
        self.font_instrucoes = pygame.font.Font('assets/Fonts/OpenSans_regular.ttf',30)

        self.instrucoes = self.font_instrucoes.render('Instruções', True, (255, 255, 255))
        self.instrucoes_w = self.instrucoes.get_width()

        self.linhas = [
            self.font.render('Seu personagem spawna no quadrado branco e tem que ir para o quadrato preto', True, (255, 255, 255)),
            self.font.render('Você tem que seguir o caminho lilás, se cair no cinza a fase se reinicia', True, (255, 255, 255)),
            self.font.render('Em algumas fases é necessário coletar pokebolas', True, (255, 255, 255)),
            self.font.render('Você monta sua movimentação, existem 4 opções de ações:', True, (255, 255, 255)),
            self.font.render('-Andar', True, (255, 255, 255)),
            self.font.render('-Virar para a Direita', True, (255, 255, 255)),
            self.font.render('-Virar para a Esquerda', True, (255, 255, 255)),
            self.font.render('-Coletar Pokebola', True, (255, 255, 255)),
            self.font.render('O seu objetivo é chegar no quadrado final coletando as pokebolas no caminho', True, (255, 255, 255)),
            self.font.render('ATENÇÃO: Não basta chegar ao final é necessário parar no quadrado', True, (255, 255, 255))]

        self.play = self.play_font.render('< - Press SPACE to Play ->', True, (255,255,255))
        self.play_w = self.play.get_width()

        self.add = 30
        self.print = False

    def play_window(self):
        self.window.blit(self.pokecode,(20,30))
        self.window.blit(self.instrucoes,(40,200))
        if not self.print:
            for i, render in enumerate(self.linhas):
                self.window.blit(render,(10,225+self.add))
                self.add += 30
            self.print = True
        self.window.blit(self.play,(20, 600))

    def start_game(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return True
        
    







# self.instrucoes                                  Instruções
# self.linha1       Seu personagem spawna no quadrado branco e tem que ir para o quadrato preto
# self.linha2         Você tem que seguir o caminho lilás, se cair no cinza a fase se reinicia
# self.linha3                  Em algumas fases é necessário coletar pokebolas
# self.linha4                Você monta sua movimentação existem 4 opções de ações:
# self.linha5                                        -Andar
# self.linha6                                -Virar para a Direita
# self.linha7                                -Virar para a Esquerda
# self.linha8                                   -Coletar Pokebola
# self.linha9       O seu objetivo é chegar no quadrado final coletando as pokebolas no caminho
# self.linha10            ATENÇÃO: Não basta chegar ao final é necessário parar no quadrado
