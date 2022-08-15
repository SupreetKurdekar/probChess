
from turtle import back
import numpy as np

import random
import copy

from piece import Piece 

from baseProbTable import baseProbTable

from square import square as sq

import pygame


class gameManager:
    def __init__(self,winSize = 800):
        # origin is at bottom left corner
        self.winSize = winSize
        # width and height refer to width and height required for graphics

        self.board = {}

        self.bPT = baseProbTable()
        self.bPT.setAllToHalf()



    def initializeBoard(self):
        
        whiteRow = {i:sq(0,i,Piece(self.bPT.probTable,color=0,classId=i)) for i in range(8)}
        blackRow = {i:sq(7,i,Piece(self.bPT.probTable,color=1,classId=i)) for i in range(8)}

        whitePawnRow = {i:sq(1,i,Piece(self.bPT.probTable,color=0,classId=0)) for i in range(8)}
        blackPawnRow = {i:sq(6,i,Piece(self.bPT.probTable,color=1,classId=0)) for i in range(8)}

        self.board = {i:{j:sq(i,j) for j in range(8)} for i in range(2,6) }
        
        self.board[0] = copy.deepcopy(whiteRow)
        self.board[1] = copy.deepcopy(whitePawnRow)

        self.board[7] = copy.deepcopy(blackRow)
        self.board[6] = copy.deepcopy(blackPawnRow)

    def graphicsInit(self):
        #graphics
        win_size = self.winSize
        pygame.init()
        self.screen = pygame.display.set_mode((win_size, win_size))
        pygame.display.set_caption("Prob Chess")

        self.backGround = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Pieces/board.jpg"),(win_size,win_size)),False,True)

        #initialize the sprites in all the pieces
        for row in list(self.board.values()):
            for square in list(row.values()):
                for piece in square.blackPieces:
                    piece.graphicsInit("Pieces")
                for piece in square.whitePieces:
                    piece.graphicsInit("Pieces")

    def drawBoard(self):
        for row in list(self.board.values()):
            for square in list(row.values()):
                square.drawPieces(self.screen)

    def drawGame(self):
        self.screen.blit(self.backGround,(0,0))
        self.drawBoard()

        pygame.time.delay(100)
        pygame.display.update()

        # print(pygame.mouse.get_pos())

    # def getEmptyBoard(self):
    #     if len(self.board) == 0:
    #         self.initializeBoard()

    #     for row in list(self.board.values()):
    #         for square in list(row.values()):
    #             surf = pygame.Surface((square.length, square.length))
        
    #             surf.fill(square.color)
        
    #             rect = surf.get_rect()
    #             self.screen.blit(surf, (square.x, square.y))

    def startGame(self):
        run = True
        
        self.graphicsInit()

        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.drawGame()

        pygame.quit()
        




