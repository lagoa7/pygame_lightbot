import pygame
import time

class End:
    def __init__(self, TILE_SIZE, window):
        self.window = window
        self.tile_size = TILE_SIZE

        self.font_vitoria = pygame.font.Font('assets/Fonts/Pokemon_solid.ttf',100)
        self.vitoria = self.font_vitoria.render('Vitória!', True, (255, 255, 255))
        self.vitoria_w = self.vitoria.get_width()


        self.font_destruicao = pygame.font.Font('assets/Fonts/OpenSans_regular.ttf',30)
        # self.destruicao = self.font_destruicao.render('Esse jogo se AUTODESTRUIRÁ', True, (255,0,0))
        # self.destruicao_w = self.destruicao.get_width()

        self.add = 30

        self.linhas = [
            self.font_destruicao.render('Esse jogo', True, (255,0,0)),
            self.font_destruicao.render('Se', True, (255,0,0)),
            self.font_destruicao.render('Autodestruirá', True, (255,0,0)),
            self.font_destruicao.render('Em', True, (255,0,0)),
            self.font_destruicao.render('3 segundos', True, (255,0,0))]

    def end_window(self):
        self.window.fill((0,0,0), pygame.Rect(0,0,self.tile_size * 9,self.tile_size * 11))

        self.window.blit(self.vitoria,(self.vitoria_w/3,200))
        self.window.blit(self.linhas[0],(self.vitoria_w/3,350))
        self.window.blit(self.linhas[1],(self.vitoria_w/3,350 + 30))
        self.window.blit(self.linhas[2],(self.vitoria_w/3,350 + 60))
        self.window.blit(self.linhas[3],(self.vitoria_w/3,350 + 90))
        self.window.blit(self.linhas[4],(self.vitoria_w/3,350 + 120))

        

        return False


        