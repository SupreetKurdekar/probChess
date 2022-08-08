
import numpy as np

import random
import copy

from piece import Piece 

from baseProbTable import baseProbTable

from square import square


class gameManager:
    def __init__(self,width = 0,height=0):
        # origin is at bottom left corner
        self.width = width
        self.height = height

        # width and height refer to width and height required for graphics

        self.board = []

        self.bPT = baseProbTable()
        self.bPT.setAllToHalf()

    def initializeBoard(self):
        
        whiteRow = {i:square(0,i,Piece(self.bPT.probTable,color=0,classId=i)) for i in range(7)}
        blackRow = {i:square(7,i,Piece(self.bPT.probTable,color=1,classId=i)) for i in range(7)}

        whitePawnRow = {i:square(0,i,Piece(self.bPT.probTable,color=0,classId=0)) for i in range(7)}
        blackPawnRow = {i:square(0,i,Piece(self.bPT.probTable,color=1,classId=0)) for i in range(7)}

        self.board = {i:{j:square(i,j) for j in range(7)} for i in range(2,6) }
        
        self.board[0] = copy.deepcopy(whiteRow)
        self.board[1] = copy.deepcopy(whitePawnRow)

        self.board[6] = copy.deepcopy(blackRow)
        self.board[7] = copy.deepcopy(blackPawnRow)

