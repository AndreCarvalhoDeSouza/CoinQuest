import pygame.image

from src.Const import PLAYER_SIZE, ENTITY_LEVEL1_SPEED, WIN_WIDTH
from src.Entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple, walk_surface: pygame.Surface, run_surface: pygame.Surface):
        super().__init__('player_walk', position)
        new_size = PLAYER_SIZE

        self.sprite_walk = pygame.transform.scale(walk_surface, new_size)
        self.sprite_run = pygame.transform.scale(run_surface, new_size)

        self.surf = self.sprite_walk
        self.rect = self.surf.get_rect(bottomleft=position)

        self.speed_walk = ENTITY_LEVEL1_SPEED['player_walk']
        self.speed_run = ENTITY_LEVEL1_SPEED['player_run']

        self.speed_x = self.speed_walk

        self.speed_y = 0
        self.gravity = 1.2
        self.float_strength = -8
        self.max_upward_speed = -12
        self.on_the_ground = True
        self.position_ground_y = position[1]
        self.max_jump_height = self.position_ground_y - 150

    def update(self, ):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_RIGHT]:
            self.surf = self.sprite_run
            self.speed_x = self.speed_run
            self.rect.x += self.speed_x
        elif pressed_key[pygame.K_LEFT]:
            self.surf = self.sprite_walk
            self.speed_x = self.speed_walk
            self.rect.x -= self.speed_x
        else:
            self.surf = self.sprite_walk

        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH

        if self.rect.left < 0:
            self.rect.left = 0

        if pressed_key[pygame.K_SPACE] and self.rect.bottom > self.max_jump_height:
            self.on_the_ground = False
            self.speed_y += self.float_strength

            if self.speed_y < self.max_upward_speed:
                self.speed_y = self.max_upward_speed
        else:
            if self.speed_y < 0:
                self.speed_y = 0
            self.speed_y += self.gravity

        self.rect.y += self.speed_y

        if self.rect.bottom <= self.max_jump_height and pressed_key[pygame.K_SPACE]:
            self.rect.bottom = self.max_jump_height
            self.speed_y = 0

        if self.rect.bottom >= self.position_ground_y:
            self.rect.bottom = self.position_ground_y
            self.speed_y = 0
            self.on_the_ground = True

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed_y = 0

    @staticmethod
    def load_player(path_file: str, sprite_width: int, sprite_height: int, column: int, row: int):
        spritesheet = pygame.image.load(path_file).convert_alpha()

        x = column * sprite_width
        y = row * sprite_height

        player_rect = pygame.Rect(x, y, sprite_width, sprite_height)
        player_sprite = spritesheet.subsurface(player_rect)

        return player_sprite