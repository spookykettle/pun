"""Project: Jacob"""

import pygame
from pygame.event import Event
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        # running variable true when the game is on, may be game is on but not playing
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY = False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800,550
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = "victor-pixel.TTF"
        self.font_face = "pixel_invaders.TTF"
        self.font_scary = "satan's island.TTF"
        # or if want default then use = pygame.font.get_default_font_()
        self.BLACK, self.WHITE, self.RED = (0, 0, 0), (255, 255, 255), (166, 48, 48)
        self.main_menu = MainMenu(self)
        self.control = ControlMenu(self)
        self.credits = CreditsMenu(self)
        self.exit = ExitMenu(self)
        # self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        # self.curr_menu = self.main_menu

        # self.state = "yes"
        # self.cursor_rect.midtop = (self.DISPLAY_W/2 -130, self.DISPLAY_H/2 +20)
    
    # def draw_cursor(self, x, y):
    #     self.draw_pixel_invader("T", 25, self.DISPLAY_W/2 +x, self.DISPLAY_H/2 +y)

    def game_loop(self):
        page = 1
        while self.playing:
            self.check_events()

            if page == 1:
                self.display.fill(self.BLACK)
                self.draw_text("JACOB: ...", 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
                self.window.blit(self.display, (0,0))
                pygame.display.update()
                if self.ESCAPE_KEY:
                    self.playing = False
                if self.START_KEY:
                    page = 2
                    self.reset_keys()

            if page == 2:
            # reset the screen by setting it black since the frame before is not deleted
                self.display.fill(self.BLACK)
                self.draw_text("JACOB: Balla? Where are you?", 20, self.DISPLAY_W/2, self.DISPLAY_H/2)    
                self.window.blit(self.display, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 3
                    self.reset_keys()

            if page == 3:
                self.display.fill(self.BLACK)
                self.draw_text("YOU FOUND A suspicious-looking letter on the bed...", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 - 60)
                self.draw_text("you pick it up and open it with no hesitation...", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 -30)
                self.draw_text("JACOB: Let's see what this is all about", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 +20)
                # self.draw_text("DO YOU WANT TO READ IT?", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 -30)
                # self.draw_text("SURE. WHY NOT...", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 +20)
                # self.draw_text("NO. THAT'S SUSSY", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 +40)

                # self.draw_cursor(-130, 20)
                # if self.UP_KEY or self.DOWN_KEY:
                #     if self.state == 'yes':
                #         self.draw_cursor(-130, 20)
                #         self.UP_KEY = False
                #         self.state = 'no'
                            
                #     elif self.state == 'no':
                #         self.draw_cursor(-130, 40)
                #         self.state = 'yes'
                #         self.UP_KEY = False

                if self.START_KEY:
                    # if self.state == "yes":
                    page = 4
                    self.reset_keys()
                    # if self.state == "no":
                    #     page = 2
                    #     self.reset_keys()
                self.window.blit(self.display, (0,0))
                pygame.display.update()

            if page == 4:
                self.display.fill(self.BLACK)
                self.draw_text_demon("I'M TAKING HER. DONT TRY TO FIND US", 30, self.DISPLAY_W/2, self.DISPLAY_H/2 - 100)  
                self.draw_text_demon("- ALMIGHTY DEMON LORD", 30, self.DISPLAY_W/2 + 70, self.DISPLAY_H/2 -65)
                self.draw_text("JACOB: OH NO! I NEED TO SAVE HER NOW!", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 +50)

                self.window.blit(self.display, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 5
                    self.reset_keys()
            
            if page == 5:
                self.display.fill(self.BLACK)
                self.draw_text("You travel miles and miles.. finally!", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 - 60)
                self.draw_text("You are here at the lord's castle!!", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 -30)
                self.draw_text("JACOB: Let's defeat the lord and take my bella back!", 20, self.DISPLAY_W/2, self.DISPLAY_H/2 +50)

                self.window.blit(self.display, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 6
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
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True

    # set back to when they dont hold key
    def reset_keys(self):
        """
        set back to when they dont hold key
        """
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY = False, False, False, False, False
     
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
    
    def draw_text_demon(self, text, size, x, y):
        """
        Show text on the screen

        Args:
            text ([str]): [what we wannna say]
            size ([int]): [size of text]
            x ([int]): [position x]
            y ([int]): [position y]
        """
        font = pygame.font.Font(self.font_scary, size)
        text_surface = font.render(text, True, self.RED)
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