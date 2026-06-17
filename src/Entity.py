from abc import ABC, abstractmethod

class Entity(ABC):

    def __init__(self):
        self.name = None
        self.surf = None
        self.rect = None
        self.speed = None

    @abstractmethod
    def update(self, ):
        pass
    @abstractmethod
    def draw(self, ):
        pass