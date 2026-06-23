import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from src.Const import COLOR_GOLD, COLOR_BLACK, WIN_WIDTH, MENU_OPTION, COLOR_BRONZE, INSTRUCTIONS, COLOR_WHITE


class Menu:
    def __init__(self, window): # Menu class constructor
        self.window = window # Window reference
        self.surf = pygame.image.load('asset/bg_menu.png').convert_alpha() # Loading the menu background
        self.rect = self.surf.get_rect(left=0, top=0)
        # Drawing the menu background from the top-left corner

    def run(self, ): # Running method
        menu_option = 0 # First menu option
        pygame.mixer_music.load('asset/menu.wav') # Music menu
        pygame.mixer_music.play(-1) # Playing the music indefinitely

        while True: # Infinite loop
            self.window.blit(source=self.surf, dest=self.rect)
            '''Drawing the menu background (self.surf) on the window top-left corner (self.rect)
            coordinates: x and y (0, 0)'''
            self.menu_text(100, "COIN", COLOR_GOLD, ((WIN_WIDTH/2), 70)) # Write the COIN word
            self.menu_text(100, "QUEST", COLOR_GOLD, ((WIN_WIDTH / 2), 140)) # Write the QUEST word

            for i in range(len(MENU_OPTION)): # For loop to write the menu options
                if i == menu_option: # Selected option will be on the color bronze
                    self.menu_text(40, MENU_OPTION[i], COLOR_BRONZE, ((WIN_WIDTH / 2), 215 + 30 * i))
                else: # If the option won't be selected, the color will be black
                    self.menu_text(40, MENU_OPTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 215 + 30 * i))

            self.menu_text(50, "INSTRUCTIONS (below)", COLOR_BLACK, ((WIN_WIDTH / 2), 360))

            for i in range(len(INSTRUCTIONS)):
                self.menu_text(30, INSTRUCTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 400 + 30 * i))

            for event in pygame.event.get():
                # Check for all event
                if event.type == pygame.QUIT: # Close the window and quit pygame
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN: # Key down (keyboard)
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1: # Avoid the selection cross the line (Key down)
                            menu_option += 1 # Allow navigation through the options
                        else:
                            menu_option = 0 # When the limit is reached, returns to the first option
                    if event.key == pygame.K_UP: #Key up (keyboard)
                        if menu_option > 0: # Avoid the selection cross the line (Key up)
                            menu_option -= 1 # Allow navigation through the options
                        else:
                            menu_option = len(MENU_OPTION) - 1 # When the limit is reached, returns to the first option
                    if event.key == pygame.K_RETURN: # Return key
                        return MENU_OPTION[menu_option]
                        # If there's no implemented option, returns to the first option when the Enter key is pressed
            pygame.display.flip() # Update all the screen content

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple): # Customize all texts
        text_font: Font = pygame.font.SysFont(name="Press Start 2P", size=text_size) # Text font and size
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() # Create the image of the text
        text_rect: Rect = text_surf.get_rect(center=text_center_pos) # Texts and images position
        self.window.blit(source=text_surf, dest=text_rect) # Draw the image text

# menu_texts parameters: text size, text, text color (RGB) and text centralization/position