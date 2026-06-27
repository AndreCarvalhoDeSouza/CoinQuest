import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from src.Const import (COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, COLOR_RED,
                       COIN_GOAL_LEVEL1, COIN_GOAL_LEVEL2, COLOR_GOLD,
                       COLOR_DARK_GREEN, INSTRUCTIONS_LEVEL, COLOR_BLACK)
from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.EntityMediator import EntityMediator
from src.Obstacle import Obstacle
from src.Coin import Coin


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        self.entity_list.extend(EntityFactory.get_entity(self.name + '_background'))
        self.player = EntityFactory.get_entity('player')
        self.entity_list.append(self.player)

        self.level_start_time = pygame.time.get_ticks()
        self.last_obstacle_spawn = pygame.time.get_ticks()
        self.next_obstacle_delay = random.randint(2000, 3500)

        self.coin_spacing = 45
        self.collected_coins = 0

        self.fonts = {
            14: pygame.font.SysFont('Lucida Sans Typewriter', 14),
            16: pygame.font.SysFont('Lucida Sans Typewriter', 16),
            20: pygame.font.SysFont('Lucida Sans Typewriter', 20),
            24: pygame.font.SysFont('Lucida Sans Typewriter', 24),
            40: pygame.font.SysFont('Lucida Sans Typewriter', 40),
            50: pygame.font.SysFont('Lucida Sans Typewriter', 50),
            60: pygame.font.SysFont('Lucida Sans Typewriter', 60)
        }

        if self.name == 'level1':
            self.coins_goals = COIN_GOAL_LEVEL1
        else:
            self.coins_goals = COIN_GOAL_LEVEL2

    def show_instructions_screen(self):

        while True:
            self.window.fill(COLOR_DARK_GREEN)

            for i in range(len(INSTRUCTIONS_LEVEL)):
                self.level_text(24, INSTRUCTIONS_LEVEL[i],
                            COLOR_WHITE, ((WIN_WIDTH / 2), 50 + 40 * i), center=True)

            self.level_text(16, 'Press ENTER to continue',
                            COLOR_WHITE, ((WIN_WIDTH / 2), 430), center=True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

            pygame.display.flip()

    def show_game_over_screen(self):
        pygame.mixer_music.stop()
        death_sound = pygame.mixer.Sound('asset/death.wav')
        death_sound.play()
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill(COLOR_BLACK)

            self.level_text(60, "GAME OVER", COLOR_RED,
                            (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50), center=True)
            self.level_text(20, f"Coins collected: {self.collected_coins}",
                            COLOR_WHITE,(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 30),
                            center=True)
            self.level_text(16, "Press ENTER to return to Menu",
                            COLOR_GOLD, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 100),
                            center=True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "GAME_OVER"

            pygame.display.flip()

    def show_level_up_screen(self):
        level_up_sound = pygame.mixer.Sound('asset/level_up.wav')
        level_up_sound.play()
        start_display_time = pygame.time.get_ticks()
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            current_time = pygame.time.get_ticks()
            self.window.fill(COLOR_DARK_GREEN)

            self.level_text(60, "LEVEL UP!", COLOR_GOLD,
                            (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 30), center=True)
            self.level_text(20, "Get ready for the next challenge...",
                            COLOR_WHITE,(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 50),
                            center=True)

            if current_time - start_display_time > 2500:
                return "LEVEL_CLEARED"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

    def show_congratulations_screen(self):
        pygame.mixer_music.stop()
        victory_sound = pygame.mixer.Sound('asset/level_up.wav')  # Reusing level_up or a victory song if available
        victory_sound.play()
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill(COLOR_BLACK)

            self.level_text(50, "CONGRATULATIONS!", COLOR_GOLD,
                            (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 80), center=True)
            self.level_text(40, "YOU WON!", COLOR_GOLD,
                            (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 20), center=True)
            self.level_text(20, "You completed CoinQuest perfectly!",
                            COLOR_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 50), center=True)
            self.level_text(16, "Press ENTER to continue", COLOR_WHITE,
                            (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 120), center=True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "VICTORY"

            pygame.display.flip()

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

            if not self.player.is_visible:
                return self.show_game_over_screen()

            if self.collected_coins >= self.coins_goals:
                pygame.mixer_music.stop()
                if self.name == 'level1':
                    return self.show_level_up_screen()
                else:
                    return self.show_congratulations_screen()

            ground_y = WIN_HEIGHT - 140
            coin_floor_y = ground_y + 40

            active_obstacles = [ent for ent in self.entity_list if isinstance(ent, Obstacle)]

            if not self.player.is_dead:
                can_spawn_obstacle = False
                if not active_obstacles:
                    if current_time - self.last_obstacle_spawn > self.next_obstacle_delay:
                        can_spawn_obstacle = True
                else:
                    last_obstacle = active_obstacles[-1]
                    free_space = WIN_WIDTH - last_obstacle.rect.right
                    if ((current_time - self.last_obstacle_spawn > self.next_obstacle_delay)
                            and (free_space > 350)):
                        can_spawn_obstacle = True

                if can_spawn_obstacle:
                    if self.name == 'level1':
                        choice = random.choice(('obstacle1_level_1', 'obstacle2_level_1'))
                    else:
                        choice = random.choice(('obstacle1_level_2', 'obstacle2_level_2',
                                                'obstacle3_level_2'))
                    new_obstacle = EntityFactory.get_entity(choice)
                    self.entity_list.append(new_obstacle)

                    self.last_obstacle_spawn = current_time
                    self.next_obstacle_delay = random.randint(2000, 3800)

                active_coins = [ent for ent in self.entity_list if isinstance(ent, Coin)]

                should_spawn_coin = False
                if not active_coins:
                    should_spawn_coin = True
                elif WIN_WIDTH - active_coins[-1].rect.left >= self.coin_spacing:
                    should_spawn_coin = True

                if should_spawn_coin:
                    spawn_x = WIN_WIDTH
                    target_y = coin_floor_y

                    for obs in active_obstacles:
                        if (obs.rect.right >= spawn_x - 100 and
                                obs.rect.left <= spawn_x + 100):
                            target_y = obs.rect.top - 60
                            break

                    if self.name == 'level1':
                        coin_type = 'coin_level_1'
                    else:
                        coin_type = 'coin_level_2'

                    self.entity_list.append(Coin(coin_type, (spawn_x, target_y)))

            EntityMediator.check_collisions(self.entity_list, self.player, self)

            self.window.fill(COLOR_BLACK)

            for ent in self.entity_list:
                if ent != self.player:
                    self.window.blit(source=ent.surf, dest=ent.rect)

            if self.player.is_visible:
                self.window.blit(source=self.player.surf, dest=self.player.rect)

            if self.name == 'level1':
                display_name = 'Level 1'
            else:
                display_name = 'Level 2'

            self.level_text(14,
                            f'{display_name} - Timeout: {self.timeout / 1000 :.1f}s',
                            COLOR_WHITE, (10, 5))
            self.level_text(16,
                            f'Collected Coins: {self.collected_coins}',
                            COLOR_WHITE, (10, 30))
            self.level_text(16,
                            f'Lives Left: {self.player.lives}',
                            COLOR_RED, (10, 55))
            self.level_text(14,
                            f'fps: {clock.get_fps() :.0f}',
                            COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14,
                            f'entities: {len(self.entity_list)}',
                            COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple,
                   text_pos: tuple, center: bool = False):
        text_font: Font = self.fonts[text_size]
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        if center:
            text_rect: Rect = text_surf.get_rect(center=text_pos)
        else:
            text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)