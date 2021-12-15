"""menu"""

import pygame

pygame.display.set_caption('Jacob')

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_pixel_invader("T", 25, self.cursor_rect.x + 20, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.controlx, self.controly = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.exitx, self.exity = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

        self.background = pygame.transform.scale(pygame.image.load("menu.png"), (self.game.DISPLAY_W, self.game.DISPLAY_H))

    def display_menu(self):
        """
        display the menu
        """
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.window.blit(self.background, (0,0))
            
            self.game.draw_text("Main Menu", 30, self.mid_w, self.mid_h -120)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Controls", 20, self.controlx, self.controly)
            self.game.draw_text("Credit", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Exit", 20, self.exitx, self.exity)

            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.controlx + self.offset, self.controly)
                self.state = "Controls"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credit"
            elif self.state == "Credit":
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"

        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Credit":
                self.cursor_rect.midtop = (self.controlx + self.offset, self.controly)
                self.state = "Controls"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credit"

    def check_input(self):
        """
        check the input
        """
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Controls":
                self.game.curr_menu = self.game.control
            elif self.state == "Credit":
                self.game.curr_menu = self.game.credits
            elif self.state == "Exit":
                self.game.curr_menu = self.game.exit
            self.run_display = False

class ControlMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Controls"
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

        self.background = pygame.transform.scale(pygame.image.load("creditandcontrol.png"), (self.game.DISPLAY_W, self.game.DISPLAY_H))
        self.current_background = self.background

        self.background_controls = pygame.transform.scale(pygame.image.load("controls.png"), (self.game.DISPLAY_W, self.game.DISPLAY_H))
        self.background_gameplay = pygame.transform.scale(pygame.image.load("gameplay.png"), (self.game.DISPLAY_W, self.game.DISPLAY_H))

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.window.blit(self.current_background, (0,0))

            if self.state != 'Control_Enter' and self.state != 'Gameplay_Enter':
                self.game.draw_text("Controls", 30, self.mid_w, self.mid_h - 30)
                self.game.draw_text("Controls", 20, self.volx, self.voly)
                self.game.draw_text("Gameplay", 20, self.controlsx, self.controlsy)
                self.draw_cursor()

            self.blit_screen()

    def check_input(self):
        """for control menu, player have to return to main menu"""
        if self.game.BACK_KEY:
            if self.state == "Control_Enter" or self.state == "Gameplay_Enter":
                self.current_background = self.background
            else:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.state = "Controls"

        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Controls':
                self.state = 'Gameplay'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Gameplay':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            if self.state == "Controls":
                self.state = "Control_Enter"
                self.current_background = self.background_controls

            elif self.state == "Gameplay":
                self.state = "Gameplay_Enter"
                self.current_background = self.background_gameplay
                
class ExitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "YES"
        self.yes_x, self.voly = self.mid_w, self.mid_h + 20
        self.no_x, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.yes_x + self.offset, self.voly)
        self.background = pygame.transform.scale(pygame.image.load("menu.png"), (self.game.DISPLAY_W, self.game.DISPLAY_H))

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.window.blit(self.background, (0,0))
            self.game.draw_text("DO YOU REALLY WANT TO EXIT?", 30, self.mid_w, self.mid_h - 30)
            self.game.draw_text("YES YES YES", 20, self.yes_x, self.voly)
            self.game.draw_text("NO NO NO", 20, self.no_x, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        """for control menu, player have to return to main menu"""
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'YES':
                self.state = 'NO'
                self.cursor_rect.midtop = (self.no_x + self.offset, self.controlsy)
            elif self.state == 'NO':
                self.state = 'YES'
                self.cursor_rect.midtop = (self.yes_x + self.offset, self.voly)
        elif self.game.START_KEY:
            if self.state == "YES":
                self.game.running = False
            elif self.state == "NO":
                self.game.curr_menu = self.game.main_menu
            self.run_display = False
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.background = pygame.transform.scale(pygame.image.load("creditandcontrol.png"), (self.game.DISPLAY_W, self.game.DISPLAY_H))


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.window.blit(self.background, (0,0))
            self.game.draw_text('Credit', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by Pun Rojanamontien (64011588)', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()