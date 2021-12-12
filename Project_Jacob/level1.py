"""Level 1"""

import pygame
import os
import random

from os import path
from pygame import draw
from pygame.event import event_name
from pygame.locals import *

current_direc = os.getcwd()
game_folder = os.path.dirname(current_direc)
img_folder = os.path.join(game_folder, "Project_Jacob")

width, height = 800, 800
fps = 60

# RGB color
white = (255, 255, 255)
black = (0, 0, 0)
red = (173, 0, 0)
blue = (15, 49, 105)
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

def draw_countdown():
    global count_down, last_countdown
    now = pygame.time.get_ticks()
    if now - last_countdown > 1000 and count_down > 0:
        last_countdown = now
        count_down -= 1
    draw_text(str(count_down), 35, black, 20, 20)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("mole")
clock = pygame.time.Clock()

# game variables
mouse_pos = (0,0)
pygame.mouse.set_visible(False)
countdown = 10
last_update = pygame.time.get_ticks()
score = 0
pos = 0
kbd_score = 0
count_down = 30
last_countdown = pygame.time.get_ticks()
game_over = False

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
            if event.button == 1 and not game_over:
                if mole_rect.collidepoint(mouse_pos):
                    # see if we are clicking on the mole
                    stab.play()
                    score += 1
                    kbd_score += random.randint(0,3)
                    pos = random_mole_position()
                else:
                    pos = random_mole_position()
                sword_img = sword[1]
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                sword_img = sword[0]
        if event.type == KEYUP:
            if event.key == K_f and game_over:
                countdown = 10
                score = 0
                pos = 0
                kbd_score = 0
                count_down = 30
                game_over = False



    screen.blit(bottom_pic, (0,550))
    if countdown <= 0:
        draw_text('"You will never ', 40, (173, 0, 0), width/2 -45, 600)
        draw_text('get ME! HAHAHA!!"', 40, (173, 0, 0), width/2 -25, 635)
        draw_text(f"Minion Killed: {score}", 30, black, width/2 +61, 700)
        draw_text(f"Kibidango: {kbd_score}", 30, black, width/2 +120, 725)
    else:
        draw_text('LEVEL ONE', 60, black, width/2 -20, 620)
        draw_text('KILL 25 MINIONS', 40, blue, width/2 -25, 675)
        if countdown > 9:
            draw_text(str(countdown), 30, (122, 108, 0), 735, 740)
        else:
            draw_text(str(countdown), 30, (122, 108, 0), 745, 740)
    
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
        pass
    else:
        screen.blit(mole, mole_rect)
        if not game_over:
            draw_countdown()

    draw_grass()
 
    if count_down == 0:
        if score < 26:
            game_over = True
            draw_text("YOU DIED", 110, red, width/5 -20, height/2 -140)
            draw_text("better luck next time!", 20, red, width/3+4, height/2 - 40)
            draw_text('press "f" to restart the game', 30, white, width/5 -23, height/2)



pygame.quit()

# reference >> https://www.youtube.com/watch?v=YMLBLJhXXn8