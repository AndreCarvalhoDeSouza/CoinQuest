from datetime import datetime

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from src.Const import COLOR_BLACK, WIN_WIDTH, COLOR_GOLD


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/bg_menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.scores = []

        self.fonts = {
            16: pygame.font.SysFont('Lucida Sans Typewriter', 16),
            18: pygame.font.SysFont('Lucida Sans Typewriter', 18),
            24: pygame.font.SysFont('Lucida Sans Typewriter', 24),
            28: pygame.font.SysFont('Lucida Sans Typewriter', 28),
            48: pygame.font.SysFont('Lucida Sans Typewriter', 48)
        }

    def save(self, name: str, level: str, coins: int, lives: int):

        self.scores.append({
            "name": name,
            "coins": coins,
            "lives": lives,
            "level": level,
            "datetime": get_formatted_date()
        })

    def show(self):
        pygame.mixer_music.load('asset/score.wav')
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            self.window.blit(self.surf, self.rect)

            self.score_text(48, "SCORE", COLOR_BLACK, (WIN_WIDTH / 2, 40))
            self.score_text(18, "*Press ESC to return to the menu", COLOR_GOLD, (WIN_WIDTH / 2 , 75))

            self.score_text(28, "LEVEL 1", COLOR_BLACK, (WIN_WIDTH / 2, 120))
            self.score_text_left(18, "NAME", COLOR_BLACK, (120, 150))
            self.score_text_left(18, "COINS", COLOR_BLACK, (320, 150))
            self.score_text_left(18, "LIVES", COLOR_BLACK, (470, 150))
            self.score_text_left(18, "DATE", COLOR_BLACK, (650, 150))

            y = 180

            for score in self.scores:

                if score["level"] == "Level 1":
                    self.score_text_left(
                        18,
                        score["name"],
                        COLOR_BLACK,
                        (120, y)
                    )

                    self.score_text_left(
                        18,
                        str(score["coins"]),
                        COLOR_BLACK,
                        (320, y)
                    )

                    self.score_text_left(
                        18,
                        str(score["lives"]),
                        COLOR_BLACK,
                        (470, y)
                    )

                    self.score_text_left(
                        18,
                        score["datetime"],
                        COLOR_BLACK,
                        (650, y)
                    )

                    y += 35

            y += 40

            self.score_text(28, "LEVEL 2", COLOR_BLACK, (WIN_WIDTH / 2, y))

            y += 30

            self.score_text_left(18, "NAME", COLOR_BLACK, (120, y))
            self.score_text_left(18, "COINS", COLOR_BLACK, (320, y))
            self.score_text_left(18, "LIVES", COLOR_BLACK, (470, y))
            self.score_text_left(18, "DATE", COLOR_BLACK, (650, y))

            y += 30

            for score in self.scores:

                if score["level"] == "Level 2":
                    self.score_text_left(
                        18,
                        score["name"],
                        COLOR_BLACK,
                        (120, y)
                    )

                    self.score_text_left(
                        18,
                        str(score["coins"]),
                        COLOR_BLACK,
                        (320, y)
                    )

                    self.score_text_left(
                        18,
                        str(score["lives"]),
                        COLOR_BLACK,
                        (470, y)
                    )

                    self.score_text_left(
                        18,
                        score["datetime"],
                        COLOR_BLACK,
                        (650, y)
                    )

                    y += 25

            self.score_text(
                16,
                "Press ESC to return",
                COLOR_BLACK,
                (WIN_WIDTH / 2, 560)
            )

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()

    def input_name(self):
        pygame.mixer_music.stop()

        name = ""
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            self.window.blit(self.surf, self.rect)

            self.score_text(
                48,
                "CONGRATULATIONS!",
                COLOR_BLACK,
                (WIN_WIDTH / 2, 60)
            )

            self.score_text(
                24,
                "Enter your name:",
                COLOR_BLACK,
                (WIN_WIDTH / 2, 140)
            )

            self.score_text(
                28,
                name + "_",
                COLOR_BLACK,
                (WIN_WIDTH / 2, 200)
            )

            self.score_text(
                18,
                "Press ENTER to confirm",
                COLOR_BLACK,
                (WIN_WIDTH / 2, 260)
            )

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        if len(name.strip()) > 0:
                            return name

                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]

                    else:
                        if len(name) < 15 and event.unicode.isprintable():
                            name += event.unicode

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = self.fonts[text_size]
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def score_text_left(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter",size=text_size)
        text_surf: Surface = text_font.render(text,True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], centery=text_pos[1])
        self.window.blit(text_surf, text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
