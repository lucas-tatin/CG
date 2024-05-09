import pygame
from pygame import mixer
from MenuDificuldades import MenuDificuldade
import random
import sys

def main():
    pygame.init()

    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)

    largura = 800
    altura = 600

    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Pong")

    raquete_largura = 10
    raquete_altura = 60
    tamanho_bola = 10

    raquete_player_1_dy = 5
    raquete_pc_dy = 5

    velocidade_bola_x = 3
    velocidade_bola_y = 3

    vencedor = ""  # Variável definida aqui para estar acessível em todo o escopo de main()
    controle = False
    rodando = True

    font_file = "Bate-Bate/pong/font/PressStart2P-Regular.ttf"
    font = pygame.font.Font(font_file, 36)

    mixer.music.load("Bate-Bate/pong/audios/music_game.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    som = mixer.Sound("Bate-Bate/pong/audios/Sound_A.wav")

    # Aqui corrigimos a chamada para a função menu_dificuldade() da classe MenuDificuldade
    dificuldade_escolhida = MenuDificuldade.menu_dificuldade(screen, largura, altura, font_file)

    clock = pygame.time.Clock()

    def posicao_inicial():
        global pc_x, pc_y, player_1_x, player_1_y, bola_x, bola_y, score_pc, score_player_1

        pc_x = 10
        pc_y = altura // 2 - raquete_altura // 2

        player_1_x = largura - 20
        player_1_y = altura // 2 - raquete_altura // 2

        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola // 2

        score_player_1 = 0
        score_pc = 0

    def fim_jogo():
        nonlocal vencedor  # Declara a variável vencedor como nonlocal para acessá-la no escopo da função
        global rodando, controle
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        controle = True
                        posicao_inicial()
                        return

            screen.fill(PRETO)
            texto_fim = font.render(f"Vencedor: {vencedor}", True, BRANCO)
            text_fim_rect = texto_fim.get_rect(center=(largura // 2, altura // 2))
            screen.blit(texto_fim, text_fim_rect)

            pygame.display.flip()

    posicao_inicial()

    while rodando:
        if not controle:
            fim_jogo()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False

            screen.fill(PRETO)

            bola_x += velocidade_bola_x
            bola_y += velocidade_bola_y

            bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola)
            raquete_pc_rect = pygame.Rect(pc_x, pc_y, raquete_largura, raquete_altura)
            raquete_player_1_rect = pygame.Rect(
                player_1_x, player_1_y, raquete_largura, raquete_altura
            )

            if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(
                raquete_player_1_rect
            ):
                som.play()
                velocidade_bola_x = -velocidade_bola_x

            if bola_y <= 0 or bola_y >= altura - tamanho_bola:
                velocidade_bola_y = -velocidade_bola_y

            if bola_x <= 0:
                bola_x = largura // 2 - tamanho_bola // 2
                bola_y = altura // 2 - tamanho_bola // 2
                velocidade_bola_x = -velocidade_bola_x
                score_player_1 += 1
                print(f"Score Player_1: {score_player_1}")
                if score_player_1 == 5:
                    print("Player_1 ganhou!")
                    vencedor = "Player 1"
                    fim_jogo()

            if bola_x >= largura - tamanho_bola:
                bola_x = largura // 2 - tamanho_bola // 2
                bola_y = altura // 2 - tamanho_bola // 2
                velocidade_bola_x = -velocidade_bola_x
                score_pc += 1
                print(f"Score PC: {score_pc}")
                if score_pc == 5:
                    print("PC ganhou!")
                    vencedor = "PC"
                    fim_jogo()

            if dificuldade_escolhida == "Fácil":
                pc_y = altura // 2 - raquete_altura // 2
            elif dificuldade_escolhida == "Médio":
                # Lógica para ajustar a posição da raquete do PC no modo médio
                pass
            elif dificuldade_escolhida == "Difícil":
                # Lógica para ajustar a posição da raquete do PC no modo difícil
                pass

            pygame.display.flip()

            clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
