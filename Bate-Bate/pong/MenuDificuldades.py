import pygame
import sys

class MenuDificuldade:
    @staticmethod
    def menu_dificuldade(screen, largura, altura, font_file):
        pygame.font.init()
        font = pygame.font.Font(font_file, 36)
        pequeno_font = pygame.font.Font(font_file, 24)
        
        dificuldades = ["1 - Fácil", "2 - Médio", "3 - Difícil"]
        dificuldade = None
        
        while dificuldade is None:
            screen.fill((0, 0, 0))
            
            titulo = font.render("Selecione o Nível", True, (255, 255, 255))
            titulo_rect = titulo.get_rect(center=(largura // 2, altura // 4))
            screen.blit(titulo, titulo_rect)
            
            for i, nivel in enumerate(dificuldades):
                texto = pequeno_font.render(f"{nivel}", True, (255, 255, 255))
                texto_rect = texto.get_rect(center=(largura // 2, altura // 2 + i * 50))
                screen.blit(texto, texto_rect)
                
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        dificuldade = 1
                    elif event.key == pygame.K_2:
                        dificuldade = 2
                    elif event.key == pygame.K_3:
                        dificuldade = 3
        
        return dificuldade
