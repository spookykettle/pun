"""Project: Jacob"""

import pygame
from pygame.event import Event
from menu import *

import pygame
import os
import random

from os import path
from pygame import draw
from pygame.event import event_name
from pygame.locals import *

from level1 import Level1
from level2 import Level2
from level3 import Level3
from level4 import Level4

from subprocess import call

class Game():
    def __init__(self):
        pygame.init()

        self.CURRENT_DIREC = os.getcwd()
        self.GAME_FOLDER = os.path.dirname(self.CURRENT_DIREC)
        self.IMG_FOLDER = os.path.join(self.GAME_FOLDER, "Project_Jacob")

        # running variable true when the game is on, may be game is on but not playing
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY = False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 800
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = "victor-pixel.TTF"
        self.font_face = "pixel_invaders.TTF"
        self.font_scary = "satan's island.TTF"
    
        self.BLACK, self.WHITE, self.RED = (14, 12, 64), (255, 255, 255), (166, 48, 48)
        self.main_menu = MainMenu(self)
        self.control = ControlMenu(self)
        self.credits = CreditsMenu(self)
        self.exit = ExitMenu(self)
        self.curr_menu = self.main_menu


    def game_loop(self):

        # default
        page = 1
        kbd = 0

        # testcases
        # level1Result = ("Win", kbd)   
        # level2Result = ("Win", 0, True)
        # level3Result = ('Win', kbd)
        
        self.background = pygame.transform.scale(pygame.image.load("door_bg.png"), (self.DISPLAY_W, self.DISPLAY_H))
        self.window.blit(self.background, (0,0))

        while self.playing:
            self.check_events()

            if page == 1:
                self.display.fill(self.BLACK)
                
                self.background = pygame.transform.scale(pygame.image.load("page_1.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                
                if self.ESCAPE_KEY:
                    self.playing = False
                if self.START_KEY:
                    page = 2
                    self.reset_keys()

            if page == 2:
                self.display.fill(self.BLACK)

                self.background = pygame.transform.scale(pygame.image.load("page_2.png"), (self.DISPLAY_W, self.DISPLAY_H))   
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 3
                    self.reset_keys()

            if page == 3:
                self.display.fill(self.BLACK)

                self.background = pygame.transform.scale(pygame.image.load("page_3.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))

                pygame.display.update()
                
                if self.START_KEY:
                    page = 4
                    self.reset_keys()

            if page == 4:
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_4.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                
                if self.START_KEY:
                    page = 5
                    self.reset_keys()
            
            if page == 5:
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_5.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 6
                    self.reset_keys()

            if page == 6:
                # level 1
                level1 = Level1()
                level1Result = level1.run()
                # if return win go to next level
                if level1Result[0] == 'Win':
                    page = 7
                    kbd = level1Result[1]
                    print("current kibidango: " + str(kbd))
                # if lost and want to go the main menu
                elif level1Result[0] == "mainmenu":
                # if lost and want to restart the whole game
                    self.playing = False
                elif level1Result[0] == "restart":
                    page = 1
                else:
                    pass
            
            if page == 7:
                # level 2
                level2 = Level2()
                level2Result = level2.run(kbd)
                # if tie three times go to next level with no hint
                if level2Result[0] == 'Tie':
                    page = 8
                # if lost and want to go the main menu
                elif level2Result[0] == "mainmenu":
                    self.playing = False
                # if lost and want to restart game
                elif level2Result[0] == "restart":
                    page = 1
                # if return win go to next level with hint
                elif level2Result[0] == "Win":
                    page = 8
                    
            if page == 8:
                # level 3
                level3 = Level3()
                level3Result = level3.run(level2Result[2], kbd)
                # if return win go to next level
                if level3Result[0] == "Win":
                    page = 9
                # if lost and want to go the main menu
                elif level3Result[0] == "mainmenu":
                    self.playing = False
                # if lost and want to restart the game
                elif level3Result[0] == "restart":
                    page = 1
            
            if page == 9:
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_9.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 10
                    self.reset_keys()

            if page == 10:
                # level 4
                level4 = Level4()
                level4Result = level4.run(kbd)
                # if return die go to page 16
                if level4Result == "die":
                    page = 16
                elif level4Result == "win":
                    page = 11
                elif level4Result == 'secret_ending':
                    page = 17
                

            if page == 11:
                # end scene
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_11.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 12
                    self.reset_keys()

            if page == 12:
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_12.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 13
                    self.reset_keys()
            
            if page == 13:
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_13.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 14
                    self.reset_keys()
            
            if page == 14:
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_14.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    page = 15
                    self.reset_keys()
            
            if page == 15:
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_15.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()
                if self.START_KEY:
                    self.playing = False
                    self.reset_keys()
            
            if page == 16:
                # You died page from level 4
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_16.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()

                if self.KEY_R:
                    page = 1
                    self.reset_keys()
                elif self.KEY_B: 
                    self.playing = False
                    self.reset_keys()
            
            if page == 17:
                # Secret Ending
                self.display.fill(self.BLACK)
                self.background = pygame.transform.scale(pygame.image.load("page_17.png"), (self.DISPLAY_W, self.DISPLAY_H))
                self.window.blit(self.background, (0,0))
                pygame.display.update()

                if self.KEY_R:
                    page = 1
                    self.reset_keys()
                elif self.KEY_B: 
                    self.playing = False
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
                if event.key == pygame.K_r:
                    self.KEY_R = True
                if event.key == pygame.K_b:
                    self.KEY_B = True
                

    # set back to when they dont hold key
    def reset_keys(self):
        """
        set back to when they dont hold key
        """
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY = False, False, False, False, False
        self.KEY_R, self.KEY_B = False, False

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