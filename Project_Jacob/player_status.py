import pygame
import os
import random

from os import path
from pygame import draw
from pygame.event import event_name
from pygame.locals import *

class EatKBDButton:
    def __init__(self, game, fixed_position):
        self.button_image = pygame.transform.scale(pygame.image.load("to_eat_kbd.png"), (250 // 2 - 30, 100 // 2))
        self.button_original_image = pygame.transform.scale(pygame.image.load("to_eat_kbd.png"), (250 // 2 - 30, 100 // 2))
        self.button_image_hover = pygame.transform.scale(pygame.image.load("to_eat_kbd_2.png"), (250 // 2 - 30, 100 // 2))

        self.fixed_position = fixed_position

        self.game = game
        self.button_rect = self.button_image.get_rect(
            center=(self.fixed_position[0] + self.button_image.get_width() / 2, 
            self.fixed_position[1] + self.button_image.get_height() / 2)
        )
        
    def button_update(self):
        if self.game is not None:
            self.game.window.blit(self.button_image, self.fixed_position)
            
    def mouse_is_inside(self, position):
        # check the boundary of mouse whether it is in picture area when clicked
        if position[0] in range(self.button_rect.left, self.button_rect.right) and position[1] in range(self.button_rect.top, self.button_rect.bottom):
            return True
        else:
            return False

    def button_hover(self, position):
        if self.mouse_is_inside(position):
            self.button_image = self.button_image_hover
        else:
            self.button_image = self.button_original_image
        
        self.button_update()

class TheJacob:
    def refresh_states(self):
        # Jcob wakeup
        self.kbd = 0
        self.insanity_state = 1
        self.game = None
        self.game_screen_refresh_function = None
        self.level1_second = 0

        self.return_key_pressed = None


        self.set_button()
        self.update_insanity_image()

    def __init__(self) -> None:
        self.DISPLAY_W = 800
        self.DISPLAY_H = 800

        self.level1_second = 0

        self.CURRENT_DIREC = os.getcwd()
        self.GAME_FOLDER = os.path.dirname(self.CURRENT_DIREC)
        self.IMG_FOLDER = os.path.join(self.GAME_FOLDER, "Project_Jacob")

        self.IMAGES = {
            1: pygame.transform.scale(pygame.image.load("insane_1.png"), (800,800)),
            2: pygame.transform.scale(pygame.image.load("insane_2.png"), (800,800)),
            3: pygame.transform.scale(pygame.image.load("insane_3.png"), (800,800)),
            4: pygame.transform.scale(pygame.image.load("insane_4.png"), (800,800)),
            5: pygame.transform.scale(pygame.image.load("insane_5.png"), (800,800)),
            6: pygame.transform.scale(pygame.image.load("insane_6.png"), (800,800))
        } 

        self.refresh_states()

    def print_game_state(self):
        print('-------------------')
        print('KBD:', self.kbd)
        print('Insanity State:', self.insanity_state)
        print('-------------------')

    def set_button(self):
        self.button = EatKBDButton(self.game, (700, 10))

    def set_game_level(self, game):
        self.game = game
        self.button.game = game

    def update_insanity_image(self):
        self.current_image = self.IMAGES[self.insanity_state]

    def eat_kbd(self):
        if self.kbd > 0:
            self.kbd -= 1
            self.insanity_state += 1
            self.level1_second += 3
            self.update_insanity_image()
    
    def is_dead_by_insanity(self):
        return self.insanity_state >= 6

    def set_back_to_game_screen_function(self, fn):
        self.game_screen_refresh_function = fn

    def back_to_game_screen(self):
        # if we set continue function before
        if not (self.game_screen_refresh_function is None):
            self.game_screen_refresh_function()

    def refresh_background(self):
        self.background = self.current_image
        self.game.window.blit(self.background, (0,0))
        self.draw_text(f'Kibidango Left: {self.kbd}', 26, (0, 0, 0), 516, 13)
        pygame.display.update()
    
    def draw_text(self, text, font_size, font_color, x, y):
        font = pygame.font.Font("victor-pixel.ttf", font_size)
        font_surface = font.render(text, True, font_color)
        self.game.window.blit(font_surface, (x,y))

    def run(self):
        self.refresh_background()

        if not pygame.mouse.get_visible():
            pygame.mouse.set_visible(True)

        runn = True
        while runn:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    runn = False
                if event.type == pygame.KEYDOWN:
                    if self.insanity_state < 6:
                        if event.key == pygame.K_y:
                            self.eat_kbd()
                            self.print_game_state()
                            self.refresh_background()
                        if event.key == pygame.K_n:
                            runn = False
                            print('N')
                    else:
                        if event.key == pygame.K_r:
                            runn = False
                            self.return_key_pressed = 'R'
                        if event.key == pygame.K_b:
                            runn = False
                            self.return_key_pressed = 'B'
        
        self.back_to_game_screen()
        return self.is_dead_by_insanity()

