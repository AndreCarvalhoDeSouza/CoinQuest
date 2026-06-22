from src.Const import ENTITY_LEVEL1_SPEED
from src.Entity import Entity

class Obstacle(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def update(self, ):
        self.rect.centerx -= ENTITY_LEVEL1_SPEED[self.name]