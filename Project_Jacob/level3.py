"""Level 3 choose the door"""

import pygame
import os
import random

from os import path
from random import choice
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION

from player_status import TheJacob

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
        # check the boundary of mouse whether it is in picture area when clicked
        if position[0] in range(self.button_rect.left, self.button_rect.right) and position[1] in range(self.button_rect.top, self.button_rect.bottom):
            return True
        else:
            return False

    def button_hover(self, position, game):
        if position[0] in range(self.button_rect.left, self.button_rect.right) and position[1] in range(self.button_rect.top, self.button_rect.bottom):
            # door open
            self.button_image = self.button_image_hover
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

        self.MAX_ROOMS = 4

    def randomCorrectDoor(self):
        self.which_door = choice([1,2])
        print(f'The correct door is {self.which_door}')

    def refreshBackground(self):
        self.window.blit(self.current_background, (0,0))

        if self.startWithHint:
            if self.room_number == 1:
                if self.which_door == 1:
                    self.window.blit(self.hint, (200,20))
                    #startWithHint == False
                elif self.which_door == 2:
                    self.window.blit(self.hint, (550,20))
            elif self.room_number == 2:
                if self.which_door == 1:
                    self.window.blit(self.hint, (160,20))
                    #startWithHint == False
                elif self.which_door == 2:
                    self.window.blit(self.hint, (500,20))
                    #startWithHint == False
            elif self.room_number == 3:
                if self.which_door == 1:
                    self.window.blit(self.hint, (180,20))
                    #startWithHint == False
                elif self.which_door == 2:
                    self.window.blit(self.hint, (520,20))
                    #startWithHint == False
        
        self.focus_door_1.button_update(self)
        self.focus_door_2.button_update(self)

    def _run(self):
        # self.window.blit(self.current_background, (0,0))
        hide_kbd_button_die = False

        self.refreshBackground()

        runn = True
        while runn:
            if self.thePlayerState.is_dead_by_insanity():
                return "Insane"

            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    runn = False

                mouse_pos = pygame.mouse.get_pos()
                if event.type == MOUSEMOTION:
                    # if hover on door
                    self.focus_door_1.button_hover(mouse_pos, self)
                    self.focus_door_2.button_hover(mouse_pos, self)

                    # if hover on kbd button
                    if not hide_kbd_button_die:
                        self.thePlayerState.button.button_hover(mouse_pos)
                
                if event.type == pygame.KEYUP:
                    if self.die == True:
                        if event.key == pygame.K_b:
                            return "mainmenu"
                        if event.key == pygame.K_r:
                            return "restart"

                if event.type == MOUSEBUTTONDOWN and self.no_more_clicking == False:
                    # if click kbd button
                    if event.button == 1 and self.thePlayerState.button.mouse_is_inside(mouse_pos):
                        self.thePlayerState.run()

                    # if click door
                    if ((self.which_door == 1) and self.focus_door_1.button_check_input(mouse_pos)) \
                        or ((self.which_door == 2) and self.focus_door_2.button_check_input(mouse_pos)):
                        self.thePlayerState.kbd -= random.randint(10,20)
                        # open the correct door -> to the boss room
                        return 'Win'

                    elif self.focus_door_1.button_check_input(mouse_pos) or \
                        self.focus_door_2.button_check_input(mouse_pos):
                        
                        self.room_number += 1

                        if self.room_number > 1:
                            self.randomCorrectDoor()
                            self.thePlayerState.kbd += random.randint(15,30)

                        if self.die == True:
                            # last door
                            self.window.blit(self.background2, (0,0))
                            self.current_background = self.background2
                            self.no_more_clicking = True
                        
                        if self.room_number == self.MAX_ROOMS:
                            if self.die == True:
                                self.focus_door_1 = self.blank_door
                                self.focus_door_2 = self.blank_door
                                hide_kbd_button_die = True
                                # self.refreshBackground()
                            else:
                                return 'Win'
                            
                        if self.room_number == 2:
                            # change to the new room's doors
                            self.focus_door_1 = self.door2_1
                            self.focus_door_2 = self.door2_2

                        if self.room_number == 3:
                            # change to the new room's doors
                            self.focus_door_1 = self.door3_1
                            self.focus_door_2 = self.door3_2
                            self.die = True
                        
                        if not self.thePlayerState.is_dead_by_insanity():
                            # if die and no kbd button is 
                            if self.die == False and not hide_kbd_button_die:
                                self.thePlayerState.button.button_update()
                            self.refreshBackground()

    def run(self, startWithHint:bool = False, thePlayerState:TheJacob = None):
        self.thePlayerState = thePlayerState
        self.thePlayerState.set_game_level(self)
        self.thePlayerState.set_back_to_game_screen_function(self.refreshBackground)

        print("Start lvl3 with hint" if startWithHint else 'Start lvl3 without hint')
        print(f"Start lvl3 with {self.thePlayerState.kbd} kbd")
        self.startWithHint = startWithHint

        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("level III - Finding the door")

        # background
        self.background = pygame.transform.scale(pygame.image.load("door_bg.png"), (self.WIDTH, self.HEIGHT))
        self.background2 = pygame.transform.scale(pygame.image.load("door_bg2.png"), (self.WIDTH, self.HEIGHT))

        # die or not
        self.die = False
        
        self.no_more_clicking = False

        # door viariables
        self.DOOR1_1 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door1_1.png")).convert_alpha(), (340, 400))
        self.DOOR1_2 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door1_2.png")).convert_alpha(), (230, 400))
        self.DOOR1_1_HOVER = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door1_1_hover.png")).convert_alpha(), (340, 400))
        self.DOOR1_2_HOVER = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door1_2_hover.png")).convert_alpha(), (230, 400))
        
        self.DOOR2_1 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door2_1.png")).convert_alpha(), (230, 400))
        self.DOOR2_2 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door2_2.png")).convert_alpha(), (340, 400))
        self.DOOR2_1_HOVER = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door2_1_hover.png")).convert_alpha(), (230, 400))
        self.DOOR2_2_HOVER = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door2_2_hover.png")).convert_alpha(), (340, 400))
        
        self.DOOR3_1 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door3_1.png")).convert_alpha(), (250, 400))
        self.DOOR3_2 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door3_2.png")).convert_alpha(), (250, 400))
        self.DOOR3_1_HOVER = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door3_1_hover.png")).convert_alpha(), (250, 400))
        self.DOOR3_2_HOVER = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door3_2_hover.png")).convert_alpha(), (250, 400))
        
        self.blank = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door_blank.png")).convert_alpha(), (1, 1))
        self.blank_h = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door_blank.png")).convert_alpha(), (1, 1))

        self.hint = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "hint_thisdoor.png")).convert_alpha(), (95, 70))
        
        # door at route n _ (if left then =1 , right =2)
        self.door1_1 = Door_as_button(self.DOOR1_1, self.DOOR1_1_HOVER, 340/2, 400/2, self, (80, 90))
        self.door1_2 = Door_as_button(self.DOOR1_2, self.DOOR1_2_HOVER, 230/2, 400/2, self, (480, 90))

        self.door2_1 = Door_as_button(self.DOOR2_1, self.DOOR2_1_HOVER, 230/2, 400/2, self, (90, 90))
        self.door2_2 = Door_as_button(self.DOOR2_2, self.DOOR2_2_HOVER, 340/2, 400/2, self, (370, 90))

        self.door3_1 = Door_as_button(self.DOOR3_1, self.DOOR3_1_HOVER, 250/2, 400/2, self, (100, 90))
        self.door3_2 = Door_as_button(self.DOOR3_2, self.DOOR3_2_HOVER, 250/2, 400/2, self, (430, 90))

        self.blank_door = Door_as_button(self.blank, self.blank_h, 800, 800, self, (1, 1))
        self.window.blit(self.background, (0,0))
        self.current_background = self.background
        #self.window.blit(self.door1_1, (100,100))
        #self.window.blit(self.DOOR1_2, (470,100))

        self.door1_1.button_update(self)
        self.door1_2.button_update(self)
        
        pygame.display.update()

        self.randomCorrectDoor()
        self.room_number = 1
        self.focus_door_1 = self.door1_1
        self.focus_door_2 = self.door1_2

        return self._run()

                    
if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()
    game = Level3()

    playerState = TheJacob()
    playerState.kbd = 7
    playerState.print_game_state()

    result = game.run(True, playerState)

    print("Game result: ", result)
    print("Insane key pressed: ", playerState.return_key_pressed)
    pygame.quit()
