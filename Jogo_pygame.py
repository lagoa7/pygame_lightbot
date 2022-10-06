import pygame
from Class_Tabuleiro import Tabuleiro
from Class_Telas import Telas
# IMPORTS ----
# -------------------------------------------------------------------------------------------------------------------------
TILE_SIZE = 110

def inicializa():
    pygame.init()
    # 9 11
    window = pygame.display.set_mode((TILE_SIZE * 9, TILE_SIZE * 11))
    tela = Telas(TILE_SIZE, window)
    tabuleiro = Tabuleiro(TILE_SIZE, window,tela)
    tabuleiro.trata_imagem()
    return window, tela, tabuleiro


def recebe_eventos(tela):
    run = True
    for event in pygame.event.get():
        # ----- Verifica consequências
        tela.exibir_movimentos(event)
        tabuleiro.muda_fase(event)
        if event.type == pygame.QUIT:
            run = False

        
    return run


def desenha(window,tela,tabuleiro):
    tela.game_window()
    tabuleiro.tabuleiro_window()
    pygame.display.update()
    return tela


def game_loop(window, tela, tabuleiro):
    run = True
    while run:
        run = recebe_eventos(tela)
        if run:
            desenha(window,tela,tabuleiro)




def finaliza():
    pygame.quit()

if __name__ == '__main__':
    window , tela, tabuleiro = inicializa()
    game_loop(window, tela, tabuleiro)