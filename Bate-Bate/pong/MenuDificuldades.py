import pygame

class MenuDificuldade:
    @staticmethod
    def menu_dificuldade(screen, largura, altura, font_file):
        font = pygame.font.Font(font_file, 36)
        dificuldade = ""

        while not dificuldade:
            screen.fill((0, 0, 0))
            texto = font.render("Selecione a dificuldade:", True, (255, 255, 255))
            texto_facil = font.render("1 - Fácil", True, (255, 255, 255))
            texto_medio = font.render("2 - Médio", True, (255, 255, 255))
            texto_dificil = font.render("3 - Difícil", True, (255, 255, 255))

            screen.blit(texto, (largura // 2 - texto.get_width() // 2, altura // 2 - 50))
            screen.blit(texto_facil, (largura // 2 - texto_facil.get_width() // 2, altura // 2 + 20))
            screen.blit(texto_medio, (largura // 2 - texto_medio.get_width() // 2, altura // 2 + 60))
            screen.blit(texto_dificil, (largura // 2 - texto_dificil.get_width() // 2, altura // 2 + 100))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        dificuldade = "Fácil"
                    elif event.key == pygame.K_2:
                        dificuldade = "Médio"
                    elif event.key == pygame.K_3:
                        dificuldade = "Difícil"

        return dificuldade
