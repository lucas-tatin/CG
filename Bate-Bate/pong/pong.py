import pygame
from pygame import mixer
from MenuDificuldades import MenuDificuldade
from raquete import Raquete
from bola import Bola
import random
import sys
import time

def main():
    pygame.init()

    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)

    largura = 800
    altura = 600

    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Pong")

    raquete_altura = 60
    tamanho_bola = 10

    raquete_player_1 = Raquete(largura - 20, altura // 2 - raquete_altura // 2, 10, raquete_altura)
    raquete_pc = Raquete(10, altura // 2 - raquete_altura // 2, 10, raquete_altura)
    bola = Bola(largura // 2 - tamanho_bola // 2, altura // 2 - tamanho_bola // 2, tamanho_bola, 5, 5)

    vencedor = ""  
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

    last_score_time = 0

    score_player_1 = 0
    score_pc = 0

    def fim_jogo():
        nonlocal vencedor, controle
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        controle = True
                        bola.reset(largura, altura)
                        score_player_1 = 0
                        score_pc = 0
                        return

            screen.fill(PRETO)
            texto_fim = font.render(f"Vencedor: {vencedor}", True, BRANCO)
            text_fim_rect = texto_fim.get_rect(center=(largura // 2, altura // 2))
            screen.blit(texto_fim, text_fim_rect)

            pygame.display.flip()

    while rodando:
        if not controle:
            fim_jogo()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and raquete_player_1.y > 0:
                raquete_player_1.move(-5)
            if keys[pygame.K_DOWN] and raquete_player_1.y < altura - raquete_altura:
                raquete_player_1.move(5)

            # Movimento do PC
            if bola.y < raquete_pc.y:
                raquete_pc.move(-5)
            elif bola.y > raquete_pc.y + raquete_altura:
                raquete_pc.move(5)

            # Atualiza a posição da bola
            bola.update()

            # Verifica colisões com as bordas da tela
            if bola.y <= 0 or bola.y >= altura - tamanho_bola:
                bola.velocidade_y = -bola.velocidade_y
            if bola.x <= 0:
                # Ponto para o jogador
                score_player_1 += 1
                bola.reset(largura, altura)
            if bola.x >= largura:
                # Ponto para o PC
                score_pc += 1
                bola.reset(largura, altura)

            # Verifica se algum jogador venceu
            if score_player_1 >= 5:
                vencedor = "Jogador 1"
                controle = False
            elif score_pc >= 5:
                vencedor = "PC"
                controle = False

            # Verifica colisões com as raquetes
            if raquete_player_1.colide(bola) or raquete_pc.colide(bola):
                bola.velocidade_x = -bola.velocidade_x
                bola.mudar_cor()
                bola.aumentar_velocidade()

            # Limpa a tela
            screen.fill(PRETO)

            # Desenha os objetos na tela
            raquete_player_1.draw(screen, BRANCO)
            raquete_pc.draw(screen, BRANCO)
            bola.draw(screen)

            # Desenha o placar
            placar_text = placar_font.render(f"Jogador: {score_player_1}  PC: {score_pc}", True, BRANCO)
            screen.blit(placar_text, (largura // 2 - placar_text.get_width() // 2, 10))

            # Atualiza a tela
            pygame.display.flip()

            # Controle de FPS
            clock.tick(60)

            # Aumenta a velocidade da bola a cada 10 segundos
            if time.time() - last_score_time > 10:
                bola.aumentar_velocidade()
                last_score_time = time.time()

if __name__ == "__main__":
    main()
