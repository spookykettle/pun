
import pygame
from os import path
import os
import time

class Level3:
    def __init__(self) -> None:
        self.CURRENT_DIREC = os.getcwd()
        self.GAME_FOLDER = os.path.dirname(self.CURRENT_DIREC)
        self.IMG_FOLDER = os.path.join(self.GAME_FOLDER, "Project_Jacob")

        self.WIDTH = 800
        self.HEIGHT = 800
    
    def clicked():
        pass

    def run(self, startWithHint:bool = False):
        print("Start lvl3 with hint" if startWithHint else 'Start lvl3 without hint')
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        clock = pygame.time.Clock()
        pygame.display.set_caption("level 3")

        self.DOOR1_1 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door1_1.png")).convert_alpha(), (340, 400))
        self.DOOR1_2 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door1_2.png")).convert_alpha(), (230, 400))
        self.DOOR2_1 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door2_1.png")).convert_alpha(), (100, 200))
        self.DOOR2_2 = pygame.transform.scale(pygame.image.load(path.join(self.IMG_FOLDER, "door2_2.png")).convert_alpha(), (100, 200))

        self.background = pygame.transform.scale(pygame.image.load("door_bg.png"), (self.WIDTH, self.HEIGHT))

        self.window.blit(self.background, (0,0))
        self.window.blit(self.DOOR1_1, (100,100))
        self.window.blit(self.DOOR1_2, (470,100))
        pygame.display.update()

        runn = True
        while runn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runn = False
                else:
                    pass
                    

if __name__ == "__main__":
    pygame.init()
    level3 = Level3()
    result = level3.run(False)

    pygame.quit()