"""Project: Jacob"""

import pygame
from pygame.event import Event
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        # running variable true when the game is on, may be game is on but not playing
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800,550
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = "victor-pixel.TTF"
        self.font_face = "pixel_invaders.TTF"
        # or if want default then use = pygame.font.get_default_font_()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.control = ControlMenu(self)
        self.credits = CreditsMenu(self)
        self.exit = ExitMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text("thank you for playing!", 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            # reset the screen by setting it black since the frame before is not deleted
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    # check the player input to see what they press
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    # set back to when they dont hold key
    def reset_keys(self):
        """
        set back to when they dont hold key
        """
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
     
    def draw_text(self, text, size, x, y):
        """
        Show text on the screen

        Args:
            text ([str]): [what we wannna say]
            size ([int]): [size of text]
            x ([int]): [position x]
            y ([int]): [position y]
        """
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
    
    def draw_pixel_invader(self, text, size, x, y):
        """
        Show monster face font on the screen

        Args:
            text ([str]): [what face we want]
            size ([int]): [size of face]
            x ([int]): [position x]
            y ([int]): [position y]
        """
        font = pygame.font.Font(self.font_face, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)