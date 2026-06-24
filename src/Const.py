import pygame

#Coin
COIN_SIZE = (32, 32)
COIN_GOAL_LEVEL1 = 100
COIN_GOAL_LEVEL2 = 200

#Colors
COLOR_GOLD = (162, 169, 29)
COLOR_BLACK = (0, 0, 0)
COLOR_BRONZE = (205, 127, 50)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_DARK_GREEN = (0, 100, 0)

#Entities
ENTITY_LEVEL1_SPEED = {
    'level1_background0': 0,
    'level1_background1': 4,
    'level1_background2': 8,
    'level1_background3': 12,
    'level1_background4': 16,
    'level2_background0': 0,
    'level2_background1': 4,
    'level2_background2': 8,
    'level2_background3': 12,
    'level2_background4': 16,
    'level2_background5': 20,
    'level2_background6': 24,
    'player_walk': 3,
    'player_run': 9,
    'obstacle1_level_1': 2,
    'obstacle2_level_1': 2,
    'obstacle1_level_2': 2,
    'obstacle2_level_2': 2,
    'obstacle3_level_2': 2,
    'coin_level_1': 2,
    'coin_level_2': 2
}

#Event Coin
EVENT_COIN = pygame.USEREVENT + 2

#Event Obstacles
EVENT_OBSTACLE = pygame.USEREVENT + 1

#Instructions
INSTRUCTIONS = ("Left Arrow Key - Run forward",
    "Right Arrow Key - Move backwards and avoid obstacles",
    "Up and Down Arrow Key - Navigate the menu options",
    "Space (pressed) - Jump and float",
)

#Menu
MENU_OPTION = ("Game - With Player",
               "Score",
                "Exit")

#Player
PLAYER_SIZE = (256, 256)

#Spawn Time
SPAWN_TIME = 1000

#Windows
WIN_WIDTH = 960
WIN_HEIGHT = 540