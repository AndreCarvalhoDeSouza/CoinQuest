import pygame

from src.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from src.Level import Level
from src.Menu import Menu
from src.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

        self.score = Score(self.window)
        self.level1_result = None

    def run(self):
        while True:

            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'level1', menu_return)
                level_return = level.run()
                if level_return == 'LEVEL_CLEARED':
                    self.level1_result = {
                        "coins": level.collected_coins,
                        "lives": level.player.lives,
                        "level": "Level 1"
                    }
                    level = Level(self.window, 'level2', menu_return)
                    level_return = level.run()
                    if level_return == 'VICTORY':
                        name = self.score.input_name()

                        self.score.save(
                            name=name,
                            level=self.level1_result["level"],
                            coins=self.level1_result["coins"],
                            lives=self.level1_result["lives"]
                        )

                        self.score.save(
                            name=name,
                            level="Level 2",
                            coins=level.collected_coins,
                            lives=level.player.lives
                        )

                        self.score.show()


            elif menu_return == MENU_OPTION[1]:
                self.score.show()

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                pass
