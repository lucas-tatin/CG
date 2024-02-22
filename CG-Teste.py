import sys
import pygame

pygame.init()

#Configuração da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Lucas", True, BRANCO)
#texto_rect = texto.get_rect(center=(largura/2, altura/2)) #Centro
#texto_rect = texto.get_rect(midtop=(largura/2, 0)) #Centro superior
#exto_rect = texto.get_rect(midbottom=(largura/2, altura)) #Centro inferior
#texto_rect = texto.get_rect(bottomright=(largura, altura))  #Canto inferior direito
#texto_rect = texto.get_rect(bottomleft=(0, altura))  #Canto inferior esquerdo
#texto_rect = texto.get_rect(topleft=(0, 0))  #Canto superior esquerdo
#texto_rect = texto.get_rect(topright=(largura, 0))  #Canto superior direito
#texto_rect = texto.get_rect(center=(50, altura/2))  #Centro esquerdo
#texto_rect = texto.get_rect(center=(750, 300)) #Centro direito

#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()
