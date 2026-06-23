import pygame

from src.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from src.Level import Level
from src.Menu import Menu

class Game:
    def __init__(self): # Game class constructor
        pygame.init() # Pygame initialization
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        # Defining the width and the height of the pygame window

    def run(self): # Running method
        while True: # infinite loop unless the 'close window' command be clicked
            menu = Menu(self.window) # Menu class instantiation
            menu_return = menu.run() # Running the menu class

            if menu_return == MENU_OPTION[0]: # First option
                level = Level(self.window, 'Level', menu_return) #Level class instantiation
                level.run() #Running the level class
            elif menu_return == MENU_OPTION[2]: # Fourth option
                pygame.quit() # Close the window
                quit() # Quit pygame
            else:
                pass
