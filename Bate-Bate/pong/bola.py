import random
import pygame

class Bola:
    def __init__(self, x, y, tamanho, velocidade_x, velocidade_y):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.cor = (255, 255, 255)

    def update(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, pygame.Rect(self.x, self.y, self.tamanho, self.tamanho))
        
    def mudar_cor(self):
        self.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def aumentar_velocidade(self):
        self.velocidade_x *= 1.1
        self.velocidade_y *= 1.1

    def reset(self, largura, altura):
        self.x = largura // 2 - self.tamanho // 2
        self.y = altura // 2 - self.tamanho // 2
        self.velocidade_x *= random.choice([-1, 1])
        self.velocidade_y *= random.choice([-1, 1])
import random
import pygame

class Bola:
    def __init__(self, x, y, tamanho, velocidade_x, velocidade_y):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.cor = (255, 255, 255)

    def update(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, pygame.Rect(self.x, self.y, self.tamanho, self.tamanho))
        
    def mudar_cor(self):
        self.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def aumentar_velocidade(self):
        self.velocidade_x *= 1.1
        self.velocidade_y *= 1.1

    def reset(self, largura, altura):
        self.x = largura // 2 - self.tamanho // 2
        self.y = altura // 2 - self.tamanho // 2
        self.velocidade_x *= random.choice([-1, 1])
        self.velocidade_y *= random.choice([-1, 1])
