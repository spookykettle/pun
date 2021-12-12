"""Level 1"""

import pygame
import os
import random

from os import path
from pygame import draw
from pygame.locals import *

current_direc = os.getcwd()
game_folder = os.path.dirname(current_direc)
img_folder = os.path.join(game_folder, "Project_Jacob")

width, height = 800, 800
fps = 60

# RGB color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
bg = (125, 191, 105)

column = 3
row = 3

def random_mole_position():
    random_grass = random.choice(grass_list_rect)
    mole_rect.midtop = random_grass.midbottom
    return random_grass[1] - 80

def draw_grass():
    x,y = 0, 0
    for i in range(row):
        x = 0
        for col in range(column):
            screen.blit(grass, (x*220 + 140, y*200 + 100))
            pygame.draw.rect(screen, bg, (x*220 + 140, y*200 + 140, 100, 120))
            rect = pygame.Rect(x*220 + 140, y*200 + 130, 100, 50)
            grass_list_rect.append(rect)
            x += 1
        y += 1

def draw_text(text, font_size, font_color, x, y):
    font = pygame.font.Font("victor-pixel.ttf", font_size)
    font_surface = font.render(text, True, font_color)
    screen.blit(font_surface, (x,y))

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("mole")
clock = pygame.time.Clock()

# game variables
mouse_pos = (0,0)
pygame.mouse.set_visible(False)
countdown = 3
last_update = pygame.time.get_ticks()
score = 0
pos = 0
kbd_score = 0

#sound
stab = pygame.mixer.Sound(path.join(img_folder, "mole_sword_stab.mp3"))


# images
mole = pygame.transform.scale(pygame.image.load(path.join(img_folder, "mole_monster.png")), (85,90))
mole_rect = mole.get_rect()

grass = pygame.transform.scale(pygame.image.load(path.join(img_folder, "mole_grass.png")).convert_alpha(), (100, 45))
grass_list_rect = []

bottom_pic = pygame.transform.scale(pygame.image.load(path.join(img_folder, "mole_dl.png")).convert_alpha(), (800, 250))

sword = []
for i in range(1, 3):
    img = pygame.transform.scale(pygame.image.load(path.join(img_folder, "mole_sword{}.png").format(i)).convert_alpha(), (130,120))
    sword.append(img)

sword_img = sword[0]
sword_rect = sword_img.get_rect()

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        mouse_pos = pygame.mouse.get_pos()
        sword_rect.center = (mouse_pos[0], mouse_pos[1])
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mole_rect.collidepoint(mouse_pos):
                    # see if we are clicking on the mole
                    stab.play()
                    score += 1
                    kbd_score += random.randint(0,3)
                    pos = random_mole_position()
                else:
                    score -= 1
                    kbd_score -= random.randint(0,3)
                    pos = random_mole_position()
                sword_img = sword[1]
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                sword_img = sword[0]

    screen.blit(bottom_pic, (0,550))
    draw_text('"You will never ', 40, (173, 0, 0), width/2 -45, 600)
    draw_text('get ME! HAHAHA!!"', 40, (173, 0, 0), width/2 -25, 635)
    draw_text(f"Minion Killed: {score}", 30, black, width/2 +61, 700)
    draw_text(f"Kibidango: {kbd_score}", 30, black, width/2 +120, 725)
    screen.blit(sword_img, sword_rect)
    pygame.display.flip()

    #draw_text(f"Minion Killed: {score}", 35, black, width/2 +40, 720)

    now = pygame.time.get_ticks()
    # so the mole wont start at top-left
    if now - last_update > 1000 and countdown > 0:
        last_update = now
        countdown -= 1
        pos = random_mole_position()
    
    mole_rect.y -= 7
    if mole_rect.y <= pos:
        mole_rect.y = pos

    screen.fill(bg)

    if countdown > 0:
        # cannot see on screen/ covered by yellow thingy
        draw_text(str(countdown), 50, white, width/2, height/2)
    else:
        screen.blit(mole, mole_rect)

    draw_grass()

pygame.quit()

# reference >> https://www.youtube.com/watch?v=YMLBLJhXXn8