import pygame

class Raquete:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def move(self, dy):
        self.y += dy

    def draw(self, screen, cor):
        pygame.draw.rect(screen, cor, (self.x, self.y, self.largura, self.altura))

    def colide(self, bola):
        return pygame.Rect(self.x, self.y, self.largura, self.altura).colliderect(
            pygame.Rect(bola.x, bola.y, bola.tamanho, bola.tamanho)
        )
