import pygame

from src.Const import ENTITY_LEVEL1_SPEED, COIN_SIZE
from src.Entity import Entity


class Coin(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, COIN_SIZE).convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)

    def update(self, ):
        self.rect.centerx -= ENTITY_LEVEL1_SPEED[self.name]