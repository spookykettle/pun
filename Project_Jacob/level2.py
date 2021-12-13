"""Level 2 tic tac toe"""

import pygame
from random import choice
import time

import os
from os import path

class Square(pygame.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ""
        self.number = number
        self.image = pygame.image.load("sq.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        
        self.x_image = pygame.image.load("x.png")
        self.o_image = pygame.image.load("o.png")

    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, xval, yval, game):
        if self.content == "":
            if self.rect.collidepoint(xval, yval):
                self.content = game.turn
                game.board[self.number] = game.turn
                if game.turn == "x":
                    self.image = pygame.transform.scale(self.x_image, (self.width, self.height))
                    game.turn = "o"
                    game.checkWinner("x")
                    if not game.is_won:
                        game.determineComputerMove()
                else:
                    self.image = pygame.transform.scale(self.o_image, (self.width, self.height))
                    game.turn = "x"
                    game.checkWinner("o")

class Level2:
    def __init__(self) -> None:
        self.CURRENT_DIREC = os.getcwd()
        self.GAME_FOLDER = os.path.dirname(self.CURRENT_DIREC)
        self.IMG_FOLDER = os.path.join(self.GAME_FOLDER, "Project_Jacob")

        self.MAX_TIE_COUNT = 1

        self.DANGER_POSITION_1 = ['', 'x', '', '', '', 'o', '', '', '', 'x']
        self.DANGER_POSITION_2 = ['', '', '', 'x', '', 'o', '', 'x', '', '']
        self.DANGER_POSITION_3 = ['', '', '', 'x', 'x', 'o', '', '', '', '']
        self.DANGER_POSITION_4 = ['', 'x', '', '', '', 'o', 'x', '', '', '']
        self.DANGER_POSITION_5 = ['', '', '', '', 'x', 'o', '', '', '', 'x']
        self.DANGER_POSITION_6 = ['', '', '', '', '', 'o', 'x', 'x', '', '']
        self.DANGER_POSITION_7 = ['', '', '', '', '', 'o', 'x', '', 'x', '']
        self.DANGER_POSITION_8 = ['', 'x', '', '', '', 'o', '', '', 'x', '']
        self.DANGER_POSITION_9 = ['', '', '', 'x', '', 'o', '', '', 'x', '']

        self.WIDTH = 800
        self.HEIGHT = 800

        self.WINNER_MOVES = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    def determineComputerMove(self):
        self.move = True
        if self.move:
            self.setBestMove("x")
        if self.move:
            self.setBestMove("o")
        if self.move:
            self.checkDangerPos()
        if self.move == True:
            self.checkCenter()
        if self.move:
            self.checkCorner()
        if self.move:
            self.checkEdge()

        if not self.move:
            for s in self.square:
                if s.number == self.comp_move:
                    s.clicked(s.x, s.y, self)
        else:
            # exit level3, go to level 3
            self.screenUpdate()
            time.sleep(1)
           
            # empty otherwise it will be on the screen infront of self.background
            self.square_group.empty()

            print('Tie! try again')
            self.is_tie = True
                
    def draw_text(self, text, font_size, font_color, x, y):
        font = pygame.font.Font("victor-pixel.ttf", font_size)
        font_surface = font.render(text, True, font_color)
        self.window.blit(font_surface, (x,y))

    def screenUpdate(self):
        self.window.blit(self.background, (0,0))
        self.square_group.draw(self.window)
        self.square_group.update()
        pygame.display.update()

    def checkCenter(self):
        if self.board[5] == "":
            self.comp_move = 5
            self.move = False

    def setBestMove(self, player):

        for i in range(8):
            if self.board[self.WINNER_MOVES[i][0]] == player and self.board[self.WINNER_MOVES[i][1]] == player and self.board[self.WINNER_MOVES[i][2]] == "":
                self.comp_move = self.WINNER_MOVES[i][2]
                self.move = False
            elif self.board[self.WINNER_MOVES[i][0]] == player and self.board[self.WINNER_MOVES[i][1]] == "" and self.board[self.WINNER_MOVES[i][2]] == player:
                self.comp_move = self.WINNER_MOVES[i][1]
                self.move = False
            elif self.board[self.WINNER_MOVES[i][0]] == "" and self.board[self.WINNER_MOVES[i][1]] == player and self.board[self.WINNER_MOVES[i][2]] == player:
                self.comp_move = self.WINNER_MOVES[i][0]
                self.move = False

    def checkDangerPos(self):
        if self.board == self.DANGER_POSITION_1:
            self.comp_move = 2
            self.move = False
        elif self.board == self.DANGER_POSITION_2:
            self.comp_move = 4
            self.move = False
        elif self.board == self.DANGER_POSITION_3:
            self.comp_move = 1
            self.move = False
        elif self.board == self.DANGER_POSITION_4:
            self.comp_move = 4
            self.move = False
        elif self.board == self.DANGER_POSITION_5:
            self.comp_move = 7
            self.move = False
        elif self.board == self.DANGER_POSITION_6:
            self.comp_move = 9
            self.move = False
        elif self.board == self.DANGER_POSITION_7:
            self.comp_move = 9
            self.move = False
        elif self.board == self.DANGER_POSITION_8:
            self.comp_move = 7
            self.move = False
        elif self.board == self.DANGER_POSITION_9:
            self.comp_move = 9
            self.move = False

    def checkWinner(self, player):
        # check whether someone wins
        for i in range(8):
            if self.board[self.WINNER_MOVES[i][0]] == player and self.board[self.WINNER_MOVES[i][1]] == player and self.board[self.WINNER_MOVES[i][2]] == player:
                self.is_won = True
                break

        # if there's a winner
        if self.is_won:
            # update screen - set to ttt background
            self.screenUpdate()
            # remove tiles
            self.square_group.empty()

            # if Jacob win
            if player == "x":
                # set winner player to x
                self.winnerPlayer = "x"
            else:
                # set winner play to o
                self.winnerPlayer = "o"
                # set background according to player
                self.background = pygame.transform.scale(pygame.image.load(player.upper() + " Wins.png"), (self.WIDTH, self.HEIGHT))


    def checkCorner(self):

        # corner at 1,3,7,9
        # for i in range(1, 11, 2):
        #     if i == 5:
        #         pass
        #     else:
        #         if self.board[i] == "":
        #             self.comp_move = i
        #             self.move = False
        #             break

        j = choice([1,3,7,9])
        if self.board[j] == "":
            self.comp_move = j
            self.move = False

    def checkEdge(self):

        # corner at 1,3,7,9
        for i in range(2, 10, 2):
            if self.board[i] == "":
                self.comp_move = i
                self.move = False
                break

    def run(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("level 2")
        clock = pygame.time.Clock()

        self.mouse_pos = (0,0)
        pygame.mouse.set_visible(True)
        
        # set tick tac toe background
        self.background = pygame.image.load("ttt_bg.png")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))

        # check how many tie
        self.winnerPlayer = "None"
        self.tie_count = self.MAX_TIE_COUNT
        
        # ----------------------------------------------------------------------
        while self.tie_count > 0:
            # self.move = check whether the computer have to self.move or not
            self.move = True
            self.comp_move = 5

            self.square_group = pygame.sprite.Group()

            self.square = []
            self.is_tie = False
            self.is_won = False
            self.board = ["" for i in range(10)]

            # create ttt board
            num = 1
            for y in range(1, 4):
                for x in range(1, 4):
                    sq = Square(x, y, num)
                    self.square_group.add(sq)
                    self.square.append(sq)

                    num += 1

            # start with player Jacob (player x)
            self.turn = "x"

            # start game
            runn = True
            while runn:
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        runn = False
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and self.turn == "x":
                        mx, my = pygame.mouse.get_pos()
                        for s in self.square:
                            s.clicked(mx, my, self)
        
                self.screenUpdate()

                # if there's someone win
                if self.is_won or self.is_tie:
                    runn = False
                    
            # game end
            if self.winnerPlayer == "x":
                return "Win"
            elif self.winnerPlayer == "o":
                return "Lost"

            self.tie_count -= 1
           
            print(f'self.tie_count: {self.tie_count}')

        return "Tie"

if __name__ == "__main__":
    pygame.init()
    level2 = Level2()
    result = level2.run()

    print("Game result:", result)
    pygame.quit()
