import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Class to create a star"""

    def __init__(self, ai_game):
        """Initializing star and its starting point"""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()

  # Bu satır, yıldız dikdörtgeninin başlangıç yatay konumunu (x) kendi genişliğine ayarlar.
        self.rect.x = self.rect.width
  #Bu satır, yıldız dikdörtgeninin başlangıç dikey konumunu (y) kendi yüksekliğine ayarlar.
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
