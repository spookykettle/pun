"""Level 2 tic tac toe"""

import pygame as z

z.init()

class Square(z.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = " "
        self.number = number
        self.image = blank_image
        self.image = z.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, xval, yval):
        global turn
        if self.content == " ":
            if self.rect.collidepoint(xval,yval):
                self.content = turn
                board[self.number] = turn
                if turn == "x":
                    self.image = z.transform.scale(x_image, (self.width, self.height))
                    turn = "o"
                else:
                    self.image = z.transform.scale(o_image, (self.width, self.height))
                    turn = "x"
                    


def Update():
    win.blit(bg, (0,0))
    square_group.draw(win)
    square_group.update()
    z.display.update()


WIDTH = 800
HEIGHT = 800

win = z.display.set_mode((WIDTH, HEIGHT))
z.display.set_caption("level 2")
clock = z.time.Clock()

blank_image = z.image.load("sq.png")
x_image = z.image.load("x.png")
o_image = z.image.load("o.png")
bg = z.image.load("ttt_bg.png")

bg = z.transform.scale(bg, (WIDTH, HEIGHT))

square_group = z.sprite.Group()
square = []
board = [" " for i in range(10)]

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
    for event in z.event.get():
        if event.type == z.QUIT:
            runn = False
        if event.type == z.MOUSEBUTTONDOWN and turn == "x":
            mx, my = z.mouse.get_pos()
            for s in square:
                s.clicked(mx, my)

    Update()