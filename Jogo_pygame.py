import imp
from tkinter.tix import WINDOW
import pygame
from Class_Tabuleiro import Tabuleiro
from Class_Telas import Telas
from Class_Play import Play
from Class_End import End
import time
# IMPORTS ----
# -------------------------------------------------------------------------------------------------------------------------
TILE_SIZE = 70

def inicializa():
    pygame.init()
    # 9 11
    game_start = False
    game_end = False

    window = pygame.display.set_mode((TILE_SIZE * 9, TILE_SIZE * 11))

    end = End(TILE_SIZE, window)
    start = Play(TILE_SIZE, window)
    tela = Telas(TILE_SIZE, window)
    tabuleiro = Tabuleiro(TILE_SIZE, window,tela)

    tabuleiro.trata_imagem()

    run = True
    return window, tela, tabuleiro, start, end, game_end, game_start, run


def recebe_eventos(tela,tabuleiro,start, game_end, game_start,run):
    for event in pygame.event.get():
        # ----- Verifica consequências
        if not game_start:
            game_start = start.start_game(event)
        else:
            tela.exibir_movimentos(event)
            tabuleiro.muda_fase(event)
        if event.type == pygame.QUIT:
            run = False

        
    return run, game_start


def desenha(window,tela,tabuleiro, start,end, game_end, game_start,run):

    if not game_start:
        start.play_window()
    else:
        tela.game_window()
        game_end = tabuleiro.tabuleiro_window()
    if game_end:
        run = end.end_window()
    pygame.display.update()
    return run


def game_loop(window, tela, tabuleiro, start, game_end, game_start,run):
    if run != False:
        while run:
            run, game_start = recebe_eventos(tela,tabuleiro,start, game_end, game_start,run)
            if run:
                run =  desenha(window,tela,tabuleiro,start,end ,game_end,game_start, run)
                if run == False:
                    time.sleep(3)



def finaliza():
    pygame.quit()

if __name__ == '__main__':
    window , tela, tabuleiro, start,end,  game_end, game_start, run = inicializa()
    game_loop(window, tela, tabuleiro, start, game_end, game_start,run)