import sys
import time
import pygame
pygame.init()
larg_tela = 800
alt_tela = 600
tela = pygame.display.set_mode((larg_tela,alt_tela))
pygame.display.set_caption("JOGO LIG4")

num_linhas = 6
num_colunas = 7
cor_preenchimento = (0,255,0)
cor_fundo = (255,255,255)
cor_linha = (0,0,0)
larg_celula = larg_tela // num_colunas
alt_celula = alt_tela // num_linhas
grade = [[False] * num_colunas for _ in range(num_linhas)]
def desenhargrade():
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            pygame.draw.rect(tela, cor_linha, (coluna * larg_celula, linha * alt_celula, larg_celula, alt_celula), 1)
            if grade[linha][coluna]:
                pygame.draw.rect(tela, cor_preenchimento, (coluna * larg_celula + 1, linha * alt_celula + 1, larg_celula - 2, alt_celula - 2))



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            colunaclicada = pos[0]//larg_celula
            linhaclicada = pos[1] // alt_celula
            grade[linhaclicada][colunaclicada] = not grade[linhaclicada][colunaclicada]

    tela.fill(cor_fundo)
    desenhargrade()
    pygame.display.flip()

pygame.quit()