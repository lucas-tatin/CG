import pygame
import sys

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Definição da Raquete
raquete_largura = 10
raquete_altura = 60
tamanho_bola = 10

# Posição da Raquete do pc
pc_x = 10
pc_y = altura // 2 - raquete_altura // 2

# Posição da Raquete do player
player_1_x = largura - 20
player_1_y = altura // 2 - raquete_altura // 2

# Posição da bola
bola_x = largura // 2 - tamanho_bola // 2
bola_y = altura // 2 - tamanho_bola // 2

# Velocidade da raquete
raquete_player_1_dy = 5
raquete_pc_dy = 5

# velocidade da bola
velocidade_bola_x = 3
velocidade_bola_y = 3

#Define score
score_player_1 = 0
score_pc = 0

font_file = "font/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_file, 36 )

clock = pygame.time.Clock()

rodando = False
def menu_principal():
    global rodando
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rodando = True  
                    return

        #Renderiza o texto do menu
        screen.fill(PRETO)
        texto_menu = font.render("Pong", True, BRANCO)
        text_menu_rect = texto_menu.get_rect(center=(largura // 2, altura // 2))
        screen.blit(texto_menu, text_menu_rect)

        tempo = pygame.time.get_ticks()
        #Pressione Space para jogar
        if tempo % 2000 < 1000:
           texto_iniciar = font.render("Pressione Espaço", True, BRANCO)
           texto_iniciar_rect = texto_iniciar.get_rect(center=(largura // 2, 450))
           screen.blit(texto_iniciar, texto_iniciar_rect)

        pygame.display.flip()

menu_principal()
        

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.fill(PRETO)

    # Movendo a bola
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    # Retângulos de Colisão
    bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola)
    raquete_pc_rect = pygame.Rect(pc_x, pc_y, raquete_largura, raquete_altura)
    raquete_player_1_rect = pygame.Rect(
        player_1_x, player_1_y, raquete_largura, raquete_altura
    )

    # Colisão da bola com a raquete do pc e a raquete do player
    if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(
        raquete_player_1_rect
    ):
        velocidade_bola_x = -velocidade_bola_x

    # Colisão da bola com as bordas da tela
    if bola_y <= 0 or bola_y >= altura - tamanho_bola:
        velocidade_bola_y = -velocidade_bola_y

    # Posicionar a bola no inicio do jogo
    if bola_x <= 0:
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola // 2
        velocidade_bola_x = -velocidade_bola_x
        score_player_1 += 1
        print(f"Score Player_1: {score_player_1}")

    if bola_x >= largura - tamanho_bola:
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola // 2
        velocidade_bola_x = -velocidade_bola_x
        score_pc += 1
        print(f"Score PC: {score_pc}")


    # Movendo a raquete do pc pra seguir a bola
    if pc_y + raquete_altura // 2 < bola_y:
        pc_y += raquete_pc_dy
    elif pc_y + raquete_altura // 2 > bola_y:
        pc_y -= raquete_pc_dy

    # Evitar que a raquete do pc saia da área
    if pc_y < 0:
        pc_y = 0
    elif pc_y > altura - raquete_altura:
        pc_y = altura - raquete_altura

    # Mostrando Score no Jogo
    font = pygame.font.Font(font_file, 16)
    score_texto = font.render(f"Score PC: {score_pc}           Score Player_1: {score_player_1} ", True, BRANCO)

    score_rect = score_texto.get_rect(center=(largura // 2, 30))

    screen.blit(score_texto, score_rect)

    #assets (objetos)
    pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raquete_largura, raquete_altura))
    pygame.draw.rect(
        screen, BRANCO, (player_1_x, player_1_y, raquete_largura, raquete_altura)
    )
    pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tamanho_bola, tamanho_bola))
    pygame.draw.aaline(screen, BRANCO, (largura // 2, 0), (largura // 2, altura))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_1_y > 0:
        player_1_y -= raquete_player_1_dy
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:
        player_1_y += raquete_player_1_dy

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
  