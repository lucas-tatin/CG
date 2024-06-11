import pygame
from pygame import mixer
from MenuDificuldades import MenuDificuldade
import random
import sys
import time

last_score_time = 0

def main():
    global last_score_time  # Adicionando a declaração global

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

    vencedor = ""  # Variável definida aqui para estar acessível em todo o escopo de main()
    controle = True
    rodando = True

    font_file = "Bate-Bate/pong/font/PressStart2P-Regular.ttf"
    font = pygame.font.Font(font_file, 36)
    placar_font = pygame.font.Font(font_file, 24)

    mixer.music.load("Bate-Bate/pong/audios/music_game.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    som = mixer.Sound("Bate-Bate/pong/audios/Sound_A.wav")

    dificuldade_escolhida = MenuDificuldade.menu_dificuldade(screen, largura, altura, font_file)

    clock = pygame.time.Clock()

    # Ajustes de dificuldade
    if dificuldade_escolhida == "Fácil":
        raquete_pc_dy = 3
        velocidade_bola_x = 3
        velocidade_bola_y = 3
    elif dificuldade_escolhida == "Médio":
        raquete_pc_dy = 5
        velocidade_bola_x = 5
        velocidade_bola_y = 5
    elif dificuldade_escolhida == "Difícil":
        raquete_pc_dy = 7
        velocidade_bola_x = 7
        velocidade_bola_y = 7

    global pc_x, pc_y, player_1_x, player_1_y, bola_x, bola_y, score_pc, score_player_1

    def posicao_inicial():
        global pc_x, pc_y, player_1_x, player_1_y, bola_x, bola_y, score_pc, score_player_1, last_score_time, bola_cor

        pc_x = 10
        pc_y = altura // 2 - raquete_altura // 2

        player_1_x = largura - 20
        player_1_y = altura // 2 - raquete_altura // 2

        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola // 2

        score_player_1 = 0
        score_pc = 0

        last_score_time = time.time()
        bola_cor = BRANCO

    def fim_jogo():
        nonlocal vencedor, controle  # Declara a variável vencedor como nonlocal para acessá-la no escopo da função
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

    def mudar_cor_bola():
        global bola_cor
        bola_cor = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    posicao_inicial()

    while rodando:
        if not controle:
            fim_jogo()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and player_1_y > 0:
                player_1_y -= raquete_player_1_dy
            if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:
                player_1_y += raquete_player_1_dy

            screen.fill(PRETO)

            bola_x += velocidade_bola_x
            bola_y += velocidade_bola_y

            bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola)
            raquete_pc_rect = pygame.Rect(pc_x, pc_y, raquete_largura, raquete_altura)
            raquete_player_1_rect = pygame.Rect(player_1_x, player_1_y, raquete_largura, raquete_altura)

            # Movimento aleatório e mudança de cor ao colidir
            if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(raquete_player_1_rect):
                som.play()
                velocidade_bola_x = -velocidade_bola_x
                velocidade_bola_y = random.randint(-7, 7)
                mudar_cor_bola()

            if bola_y <= 0 or bola_y >= altura - tamanho_bola:
                velocidade_bola_y = -velocidade_bola_y
                mudar_cor_bola()

            if bola_x <= 0:
                bola_x = largura // 2 - tamanho_bola // 2
                bola_y = altura // 2 - tamanho_bola // 2
                velocidade_bola_x = -velocidade_bola_x
                score_player_1 += 1
                last_score_time = time.time()
                print(f"Score Player_1: {score_player_1}")
                if score_player_1 == 3:
                    print("Player_1 ganhou!")
                    vencedor = "Player 1"
                    controle = False

            if bola_x >= largura - tamanho_bola:
                bola_x = largura // 2 - tamanho_bola // 2
                bola_y = altura // 2 - tamanho_bola // 2
                velocidade_bola_x = -velocidade_bola_x
                velocidade_bola_y = random.randint(-7, 7)  # Adicionado para garantir uma direção aleatória após o ponto
                score_pc += 1
                last_score_time = time.time()
                print(f"Score PC: {score_pc}")
                if score_pc == 3:
                    print("PC ganhou!")
                    vencedor = "PC"
                    controle = False    

            # Aumento da velocidade da bola ao longo do tempo
            if time.time() - last_score_time > 10:  # Aumenta a cada 10 segundos
                velocidade_bola_x *= 1.1
                velocidade_bola_y *= 1.1
                last_score_time = time.time()

            # Movimento da raquete do PC
            if bola_y > pc_y + raquete_altura // 2:
                pc_y += raquete_pc_dy
            elif bola_y < pc_y + raquete_altura // 2:
                pc_y -= raquete_pc_dy

            # Desenho dos elementos na tela
            screen.fill(PRETO)
            pygame.draw.rect(screen, BRANCO, raquete_pc_rect)
            pygame.draw.rect(screen, BRANCO, raquete_player_1_rect)
            pygame.draw.ellipse(screen, bola_cor, bola_rect)

            placar_text = placar_font.render(f"{score_pc} x {score_player_1}", True, BRANCO)
            screen.blit(placar_text, (largura // 2 - placar_text.get_width() // 2, 20))

            pygame.display.flip()

            clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
