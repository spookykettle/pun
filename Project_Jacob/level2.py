"""Level 2 tic tac toe"""

import pygame
from random import choice
import time

import os
from os import path

current_direc = os.getcwd()
game_folder = os.path.dirname(current_direc)
img_folder = os.path.join(game_folder, "Project_Jacob")

pygame.init()

class Square(pygame.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ""
        self.number = number
        self.image = blank_image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, xval, yval):
        global turn, won
        if self.content == "":
            if self.rect.collidepoint(xval,yval):
                self.content = turn
                board[self.number] = turn
                if turn == "x":
                    self.image = pygame.transform.scale(x_image, (self.width, self.height))
                    turn = "o"
                    checkWinner("x")
                    if not won:
                        CompMove()
                else:
                    self.image = pygame.transform.scale(o_image, (self.width, self.height))
                    turn = "x"
                    checkWinner("o")


def CompMove():
    global move, bg
    move = True
    if move:
        Winner("x")
    if move:
        Winner("o")
    if move:
        checkDangerPos()
    if move == True:
        checkCenter()
    if move:
        checkCorner()
    if move:
        checkEdge()
    if not move:
        for s in square:
            if s.number == comp_move:
                s.clicked(s.x, s.y)
    else:
        # go to level 3
        Update()
        time.sleep(1)
        
        # empty otherwise it will be on the screen infront of bg
        square_group.empty()

        bg = pygame.transform.scale(pygame.image.load("Tie Game.png"), (WIDTH, HEIGHT))

def draw_text(text, font_size, font_color, x, y):
    font = pygame.font.Font("victor-pixel.ttf", font_size)
    font_surface = font.render(text, True, font_color)
    win.blit(font_surface, (x,y))

def Update():
    global won, move
    win.blit(bg, (0,0))

    square_group.draw(win)
    square_group.update()
    pygame.display.update()

def checkCenter():
    global comp_move, move

    if board[5] == "":
        comp_move = 5
        move = False

def Winner(player):
    global comp_move, move
    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == "":
            comp_move = winners[i][2]
            move = False
        elif board[winners[i][0]] == player and board[winners[i][1]] == "" and board[winners[i][2]] == player:
            comp_move = winners[i][1]
            move = False
        elif board[winners[i][0]] == "" and board[winners[i][1]] == player and board[winners[i][2]] == player:
            comp_move = winners[i][0]
            move = False

def checkDangerPos():
    global move, comp_move
    if board == dangerPos1:
        comp_move = 2
        move = False
    elif board == dangerPos2:
        comp_move = 4
        move = False
    elif board == dangerPos3:
        comp_move = 1
        move = False
    elif board == dangerPos4:
        comp_move = 4
        move = False
    elif board == dangerPos5:
        comp_move = 7
        move = False
    elif board == dangerPos6:
        comp_move = 9
        move = False
    elif board == dangerPos7:
        comp_move = 9
        move = False
    elif board == dangerPos8:
        comp_move = 7
        move = False
    elif board == dangerPos9:
        comp_move = 9
        move = False

def checkWinner(player):
    global bg, won, win_win
    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == player:
            won = True
            break
    if won:
        Update()
        # empty otherwise it will be on the screen infront of bg
        square_group.empty()
        if player == "x":
            # if you win monster will tell you which door is the right one
            pass
        else:
            bg = pygame.transform.scale(pygame.image.load(player.upper() + " Wins.png"), (WIDTH,HEIGHT))


def checkCorner():
    global comp_move, move

    # corner at 1,3,7,9
    # for i in range(1, 11, 2):
    #     if i == 5:
    #         pass
    #     else:
    #         if board[i] == "":
    #             comp_move = i
    #             move = False
    #             break

    j = choice([1,3,7,9])
    if board[j] == "":
        comp_move = j
        move = False

def checkEdge():
    global comp_move, move

    # corner at 1,3,7,9
    for i in range(2, 10, 2):
        if board[i] == "":
            comp_move = i
            move = False
            break

WIDTH = 800
HEIGHT = 800


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("level 2")
clock = pygame.time.Clock()

blank_image = pygame.image.load("sq.png")
x_image = pygame.image.load("x.png")
o_image = pygame.image.load("o.png")
bg = pygame.image.load("ttt_bg.png")

count_score = False

score = 0

bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# move = check whether the computer have to move or not
move = True
comp_move = 5

square_group = pygame.sprite.Group()

square = []
won = False
winners = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
board = ["" for i in range(10)]

dangerPos1 = ['', 'x', '', '', '', 'o', '', '', '', 'x']
dangerPos2 = ['', '', '', 'x', '', 'o', '', 'x', '', '']
dangerPos3 = ['', '', '', 'x', 'x', 'o', '', '', '', '']
dangerPos4 = ['', 'x', '', '', '', 'o', 'x', '', '', '']
dangerPos5 = ['', '', '', '', 'x', 'o', '', '', '', 'x']
dangerPos6 = ['', '', '', '', '', 'o', 'x', 'x', '', '']
dangerPos7 = ['', '', '', '', '', 'o', 'x', '', 'x', '']
dangerPos8 = ['', 'x', '', '', '', 'o', '', '', 'x', '']
dangerPos9 = ['', '', '', 'x', '', 'o', '', '', 'x', '']

num = 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        square.append(sq)

        num += 1

turn = "x"

runn = True

while runn:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runn = False
        if event.type == pygame.MOUSEBUTTONDOWN and turn == "x":
            mx, my = pygame.mouse.get_pos()
            for s in square:
                s.clicked(mx, my)

    Update()
