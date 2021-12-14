"""Level 1"""

import pygame
import os
import random

from os import path
from pygame import draw
from pygame.event import event_name
from pygame.locals import *

class Level1:
    def __init__(self) -> None:
        self.CURRENT_DIREC = os.getcwd()
        self.GAME_FOLDER = os.path.dirname(self.CURRENT_DIREC)
        self.IMG_FOLDER = os.path.join(self.GAME_FOLDER, "Project_Jacob")

        self.WIDTH, self.HEIGHT = 800, 800
        self.FPS = 60

        # RGB color
        self.WHITE = (255, 255, 255)
        self.black = (0, 0, 0)
        self.RED = (173, 0, 0)
        self.BLUE = (15, 49, 105)
        self.GREEN = (0, 255, 0)
        self.bg = (125, 191, 105)

        self.COLUMN = 3
        self.ROW = 3

        self.SECONDS_BEFORE_GAME_START = 1
        self.SECONDS_PER_GAME = 4
        self.MINIONS_TO_KILL = 1

    def random_mole_position(self):
        self.random_grass = random.choice(self.grass_list_rect)
        self.mole_rect.midtop = self.random_grass.midbottom
        return self.random_grass[1] - 80

    def draw_grass(self):
        x,y = 0, 0
        for i in range(self.ROW):
            x = 0
            for col in range(self.COLUMN):
                self.screen.blit(self.grass, (x*220 + 140, y*200 + 100))
                pygame.draw.rect(self.screen, self.bg, (x*220 + 140, y*200 + 140, 100, 120))
                rect = pygame.Rect(x*220 + 140, y*200 + 130, 100, 50)
                self.grass_list_rect.append(rect)
                x += 1
            y += 1

    def draw_text(self, text, font_size, font_color, x, y):
        font = pygame.font.Font("victor-pixel.ttf", font_size)
        font_surface = font.render(text, True, font_color)
        self.screen.blit(font_surface, (x,y))

    def draw_countdown(self):
        now = pygame.time.get_ticks()
        if now - self.last_countdown > 1000 and self.count_down > 0:
            self.last_countdown = now
            self.count_down -= 1
        self.draw_text(str(self.count_down), 35, self.black, 20, 20)

    def run(self):
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("mole")
        self.clock = pygame.time.Clock()

        # game variables
        self.mouse_pos = (0,0)
        pygame.mouse.set_visible(False)
        self.countdown = self.SECONDS_BEFORE_GAME_START
        self.last_update = pygame.time.get_ticks()
        self.score = 0
        self.pos = 0
        self.kbd_score = 0
        self.count_down = self.SECONDS_PER_GAME
        self.last_countdown = pygame.time.get_ticks()
        self.game_over = False

        #sound
        self.stab = pygame.mixer.Sound(path.join(self.IMG_FOLDER, "mole_sword_stab.mp3"))


        # images
        mole = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "mole_monster.png")), (85,90))
        self.mole_rect = mole.get_rect()

        self.grass = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "mole_grass.png")).convert_alpha(), (100, 45))
        self.grass_list_rect = []

        bottom_pic = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "mole_dl.png")).convert_alpha(), (800, 250))

        sword = []
        for i in range(1, 3):
            img = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "mole_sword{}.png").format(i)).convert_alpha(), (130,120))
            sword.append(img)

        sword_img = sword[0]
        sword_rect = sword_img.get_rect()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    run = False
                mouse_pos = pygame.mouse.get_pos()
                sword_rect.center = (mouse_pos[0], mouse_pos[1])
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.game_over:
                        if self.mole_rect.collidepoint(mouse_pos):
                            # see if we are clicking on the mole
                            self.stab.play()
                            self.score += 1
                            self.kbd_score += random.randint(0,3)
                            self.pos = self.random_mole_position()
                        else:
                            self.pos = self.random_mole_position()
                        sword_img = sword[1]
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        sword_img = sword[0]
                if event.type == KEYUP:
                    # i add p secretly so i can use it on the presentation
                    if event.key == K_r:
                        # go to the first scene of the game
                        return ("restart", 0)
                        
                    elif event.key == K_p:
                        self.countdown = self.SECONDS_BEFORE_GAME_START
                        self.score = 0
                        self.pos = 0
                        self.kbd_score = 0
                        self.count_down = self.SECONDS_PER_GAME
                        self.game_over = False
                    elif event.key == K_m and self.game_over:
                        # go to main menu
                        return ("mainmenu", 0)
                        # ยังไม่ได้ลองรันเพราะตอนตายไม่ขึ้น


            self.screen.blit(bottom_pic, (0,550))
            if self.countdown <= 0:
                self.draw_text('"You will never ', 40, (173, 0, 0), self.WIDTH/2 -45, 600)
                self.draw_text('get ME! HAHAHA!!"', 40, (173, 0, 0), self.WIDTH/2 -25, 635)
                self.draw_text(f"Minion Killed: {self.score}", 30, self.black, self.WIDTH/2 +61, 700)
                self.draw_text(f"Kibidango: {self.kbd_score}", 30, self.black, self.WIDTH/2 +120, 725)
            else:
                self.draw_text('LEVEL ONE', 60, self.black, self.WIDTH/2 -20, 620)
                self.draw_text('KILL 25 MINIONS', 40, self.BLUE, self.WIDTH/2 -25, 675)
                if self.countdown > 9:
                    self.draw_text(str(self.countdown), 30, (122, 108, 0), 735, 740)
                else:
                    self.draw_text(str(self.countdown), 30, (122, 108, 0), 745, 740)
            
            self.screen.blit(sword_img, sword_rect)
            pygame.display.flip()

            #draw_text(f"Minion Killed: {self.score}", 35, black, width/2 +40, 720)

            now = pygame.time.get_ticks()
            # so the mole wont start at top-left
            if now - self.last_update > 1000 and self.countdown > 0:
                self.last_update = now
                self.countdown -= 1
                self.pos = self.random_mole_position()
            
            self.mole_rect.y -= 7
            if self.mole_rect.y <= self.pos:
                self.mole_rect.y = self.pos

            self.screen.fill(self.bg)

            if self.countdown > 0:
                pass
            else:
                self.screen.blit(mole, self.mole_rect)
                if not self.game_over:
                    self.draw_countdown()

            self.draw_grass()
        
            if self.count_down == 0:
                if self.score < self.MINIONS_TO_KILL:
                    self.draw_text("YOU DIED", 110, self.RED, self.WIDTH/5 -20, self.HEIGHT/2 -140)
                    self.draw_text("better luck next time!", 20, self.RED, self.WIDTH/3+4, self.HEIGHT/2 - 40)
                    self.draw_text('press "r" to restart the game', 30, self.WHITE, self.WIDTH/5 -23, self.HEIGHT/2)
                    self.draw_text('press "b" to go back to main menu', 30, self.WHITE, self.WIDTH/5 -30, self.HEIGHT/2 + 30)
                    self.game_over = True
                else:
                    run = False

        return ("Win", self.kbd_score)       

        # reference >> https://www.youtube.com/watch?v=YMLBLJhXXn8

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    game = Level1()
    game.run()
    pygame.quit()


# รันตอนตายไม่ได้
# ตายแล้ววนลูป