import pygame

#C
COIN_SIZE = (32, 32)
COIN_GOAL_LEVEL1 = 100
COIN_GOAL_LEVEL2 = 200

COLOR_GOLD = (162, 169, 29)
COLOR_BLACK = (0, 0, 0)
COLOR_BRONZE = (205, 127, 50)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_DARK_GREEN = (0, 100, 0)

#E
ENTITY_LEVEL1_SPEED = {
    'level1_background0': 0,
    'level1_background1': 1,
    'level1_background2': 2,
    'level1_background3': 3,
    'level1_background4': 4,
    'level2_background0': 0,
    'level2_background1': 1,
    'level2_background2': 2,
    'level2_background3': 3,
    'level2_background4': 4,
    'level2_background5': 5,
    'level2_background6': 6,
    'player_walk': 3,
    'player_run': 6,
    'obstacle1_level_1': 3,
    'obstacle2_level_1': 3,
    'obstacle1_level_2': 3,
    'obstacle2_level_2': 3,
    'obstacle3_level_2': 3,
    'coin_level_1': 3,
    'coin_level_2': 3
}

EVENT_COIN = pygame.USEREVENT + 2

EVENT_OBSTACLE = pygame.USEREVENT + 1

#I
INSTRUCTIONS_MENU = ("Left Arrow Key - Run forward  (Player)",
    "Right Arrow Key - Move backwards  (Player)",
    "Up and Down Arrow Key - Navigate the menu options",
    "Space (pressed) - Jump and float to avoid obstacles (Player)",
)

INSTRUCTIONS_LEVEL = ("1. At level 1, the player must collect 100 coins",
    "2. But at level 2, the player must collect 200 coins",
    "3. By level, the player has 3 lives",
    "4. If the player hits an obstacle, he will lose a life",
    "5. If the player loses all 3 lives, the game is over"
)

#M
MENU_OPTION = ("Game - With Player",
               "Score",
                "Exit")

#P
PLAYER_SIZE = (256, 256)

#S
SPAWN_TIME = 1000

#W
WIN_WIDTH = 960
WIN_HEIGHT = 540