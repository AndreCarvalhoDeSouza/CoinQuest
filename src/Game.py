import pygame

from src.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from src.Level import Level
from src.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'level1', menu_return)
                level_return = level.run()
                if level_return == 'LEVEL_CLEARED':
                    level = Level(self.window, 'level2', menu_return)
                    level_return = level.run()
                    if level_return == 'LEVEL_CLEARED':
                        print("Congratulations! You won CoinQuest!")

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                pass
