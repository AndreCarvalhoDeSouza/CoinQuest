import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from src.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH
from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.Obstacle import Obstacle
from src.Coin import Coin


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        self.entity_list.extend(EntityFactory.get_entity('level1_background'))
        self.player = EntityFactory.get_entity('player')
        self.entity_list.append(self.player)

        self.level_start_time = pygame.time.get_ticks()
        self.last_obstacle_spawn = pygame.time.get_ticks()
        self.next_obstacle_delay = random.randint(2000, 3500)

        self.coin_spacing = 45
        self.collected_coins = 0

        self.coin_sound = pygame.mixer.Sound('asset/coin.wav')

    def run(self):
        pygame.mixer_music.load('asset/levels_song.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            current_time = pygame.time.get_ticks()

            for ent in self.entity_list:
                ent.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            ground_y = WIN_HEIGHT - 140
            coin_floor_y = ground_y + 40

            active_obstacles = [ent for ent in self.entity_list if isinstance(ent, Obstacle)]

            can_spawn_obstacle = False
            if not active_obstacles:
                if current_time - self.last_obstacle_spawn > self.next_obstacle_delay:
                    can_spawn_obstacle = True
            else:
                last_obstacle = active_obstacles[-1]
                free_space = WIN_WIDTH - last_obstacle.rect.right
                if (current_time - self.last_obstacle_spawn > self.next_obstacle_delay) and (free_space > 350):
                    can_spawn_obstacle = True

            if can_spawn_obstacle:
                choice = random.choice(('obstacle1_level_1', 'obstacle2_level_1'))
                new_obstacle = EntityFactory.get_entity(choice)
                self.entity_list.append(new_obstacle)

                self.last_obstacle_spawn = current_time
                self.next_obstacle_delay = random.randint(2000, 3800)

            active_coins = [ent for ent in self.entity_list if isinstance(ent, Coin)]

            if not active_coins or (WIN_WIDTH - active_coins[-1].rect.left >= self.coin_spacing):
                spawn_x = WIN_WIDTH
                target_y = coin_floor_y

                for obs in active_obstacles:
                    if obs.rect.right >= spawn_x - 100 and obs.rect.left <= spawn_x + 100:
                        target_y = obs.rect.top - 60
                        break

                self.entity_list.append(Coin('coin_level_1', (spawn_x, target_y)))

            player_hitbox = pygame.Rect(0, 0, 80, 120)
            player_hitbox.midbottom = self.player.rect.midbottom

            for ent in self.entity_list[:]:
                if isinstance(ent, Coin) and player_hitbox.colliderect(ent.rect):
                    self.coin_sound.play()
                    self.collected_coins += 1
                    self.entity_list.remove(ent)
                    continue

                if (isinstance(ent, Obstacle) or isinstance(ent, Coin)) and ent.rect.right < 0:
                    self.entity_list.remove(ent)

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)

            self.level_text(14, f'Level 1 - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(16, f'Collected Coins: {self.collected_coins}', COLOR_WHITE, (10, 30))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entities: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
