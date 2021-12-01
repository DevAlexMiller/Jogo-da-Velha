#BIBLIOTECAS
import pygame
import sys
import time
from pygame.locals import*
pygame.init()

#CORES
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
lightGrey = (211, 211, 211)

#TELA
screen = pygame.display.set_mode((600, 600))
altura = screen.get_height()
largura = screen.get_width()
screen.fill(lightGrey)

#LINHAS
pygame.draw.line(screen, black,(200,0), [200,600], 5)
pygame.draw.line(screen, black,(400,0), [400,600], 5)
pygame.draw.line(screen, black,(0,200), [600,200], 5)
pygame.draw.line(screen, black,(0,400), [600,400], 5)

#IMAGENS
img_recomeco = pygame.image.load("start.jpg")
img_x = pygame.image.load("x.png")
img_velha = pygame.image.load("velha.jpg")
img_O = pygame.image.load("O.png")
img_x = pygame.transform.scale(img_x,(100,100))
img_O = pygame.transform.scale(img_O,(100,100))

#VARIÁVEIS/MATRIZES
quadrante_linha = [50,250,450]
quadrante_coluna = [50,250,450]
rodada = 0
y = 0
jogo = [[0,1,2],[3,4,5],[6,7,8]]
z = 0
d = 0

#FUNÇÕES  
def jogada_x(pos):
    index_coluna = int(pos[0]/200)
    index_linha = int(pos[1]/200)
    if jogo[index_linha][index_coluna] != 'X' and jogo[index_linha][index_coluna] != 'O' :
        jogo[index_linha][index_coluna] = 'X'
        screen.blit(img_x,(quadrante_linha[index_coluna],quadrante_coluna[index_linha]))
        x = 0
        return x
    else:
        x = -1
        return x
    
def jogada_o(pos):
    index_coluna = int(pos[0]/200)
    index_linha = int(pos[1]/200)
    if jogo[index_linha][index_coluna] != 'X' and jogo[index_linha][index_coluna] != 'O' :
        jogo[index_linha][index_coluna] = 'O'
        screen.blit(img_O,(quadrante_linha[index_coluna],quadrante_coluna[index_linha]))
        x = 0
        return x
    else:
        x = -1
        return x 

def finalizar():
    if jogo[0][0]==jogo[0][1] and jogo[0][0]==jogo[0][2]:
        pygame.draw.line(screen, red,(0,100), [600,100], 5)
        return 77 
    elif jogo[1][0]==jogo[1][1] and jogo[1][0]==jogo[1][2]:
        pygame.draw.line(screen, red,(0,300), [600,300], 5)
        return 77
    elif jogo[2][0]==jogo[2][1] and jogo[2][0]==jogo[2][2]:
         pygame.draw.line(screen, red,(0,500), [600,500], 5)
         return 77
    elif jogo[0][0]==jogo[1][0] and jogo[0][0]==jogo[2][0]:
         pygame.draw.line(screen, red,(100,0), [100,600], 5)
         return 77
    elif jogo[0][1]==jogo[1][1] and jogo[0][1]==jogo[2][1]:
         pygame.draw.line(screen, red,(300,0), [300,600], 5)
         return 77
    elif jogo[0][2]==jogo[1][2] and jogo[0][2]==jogo[2][2]:
         pygame.draw.line(screen, red,(500,0), [500,600], 5)
         return 77 
    elif jogo[0][0]==jogo[1][1] and jogo[0][0]==jogo[2][2]:
         pygame.draw.line(screen, red,(0,0), [600,600], 5)
         
         return 77 
    elif jogo[0][2]==jogo[1][1] and jogo[0][2]==jogo[2][0]:
         pygame.draw.line(screen, red,(600,0), [0,600], 5)
         return 77 

#PROGRAMA_PRINCIPAL
while y == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            y == 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos  = pygame.mouse.get_pos()
            if(rodada%2 == 0):
                    z = jogada_x(click_pos)
                    rodada = rodada + 1 + z
                    d = finalizar()
            elif(rodada%2 == 1):
                    z = jogada_o(click_pos)
                    rodada = rodada + 1 + z
                    d = finalizar()               
    pygame.display.flip()
    if(d == 77):
            screen.blit
            break
    if rodada >=9:
            screen.fill(white)
            screen.blit(img_velha, (200,250))
            break
