"""Level 3 choose the door"""

import pygame
from os import path
import os
import time

from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION

class Door_as_button():
    def __init__(self, b_image, b_image_hover, b_x, b_y, game, fixed_position):
        # button variables
        super().__init__()
        self.button_image = b_image
        self.button_original_image = b_image
        self.button_image_hover = b_image_hover
        self.button_x_pos = b_x
        self.button_y_pos = b_y

        self.fixed_position = fixed_position

        self.button_update(game)
        self.button_rect = self.button_image.get_rect(
            center=(self.fixed_position[0] + self.button_x_pos, 
            self.fixed_position[1] + self.button_y_pos)
        )
        
    def button_update(self, game):
        game.window.blit(self.button_image, self.fixed_position)
        pygame.display.update()
    
    def button_check_input(self, position):
        # check the boundary of mouse whether it is in picture area
        if position[0] in range(self.button_rect.left, self.button_rect.right) and position[1] in range(self.button_rect.top, self.button_rect.bottom):
            print("button pressed")
            

    def button_hover(self, position, game):
        if position[0] in range(self.button_rect.left, self.button_rect.right) and position[1] in range(self.button_rect.top, self.button_rect.bottom):
            # door open
            self.button_image = self.button_image_hover
            print("hover!")
        else:
            # door close
            self.button_image = self.button_original_image
        
        self.button_update(game)



class Level3:
    def __init__(self):
        self.CURRENT_DIREC = os.getcwd()
        self.GAME_FOLDER = os.path.dirname(self.CURRENT_DIREC)
        self.IMG_FOLDER = os.path.join(self.GAME_FOLDER, "Project_Jacob")

        self.WIDTH = 800
        self.HEIGHT = 800

    def run(self, startWithHint:bool = False):
        print("Start lvl3 with hint" if startWithHint else 'Start lvl3 without hint')
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        clock = pygame.time.Clock()
        pygame.display.set_caption("level 3")

        self.DOOR1_1 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door1_1.png")).convert_alpha(), (340, 400))
        self.DOOR1_1_HOVER = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door1_1_hover.png")).convert_alpha(), (340, 400))
        self.DOOR1_2 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door1_2.png")).convert_alpha(), (230, 400))
        self.DOOR2_1 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door2_1.png")).convert_alpha(), (230, 400))
        self.DOOR2_2 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door2_2.png")).convert_alpha(), (340, 400))

        self.left_door = Door_as_button(self.DOOR1_1, self.DOOR1_1_HOVER, 340/2, 400/2, self, (100,100))

        self.background = pygame.transform.scale(pygame.image.load("door_bg.png"), (self.WIDTH, self.HEIGHT))

        self.window.blit(self.background, (0,0))
        #self.window.blit(self.left_door, (100,100))
        self.window.blit(self.DOOR1_2, (470,100))

        self.left_door.button_update(self)
        
        pygame.display.update()

        runn = True
        while runn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runn = False
                mouse_pos = pygame.mouse.get_pos()
                if event.type == MOUSEMOTION:
                    self.left_door.button_hover(mouse_pos, self)
                if event.type == MOUSEBUTTONDOWN:
                    self.left_door.button_check_input(mouse_pos)


if __name__ == "__main__":
    pygame.init()
    level3 = Level3()
    result = level3.run(False)

    pygame.quit()