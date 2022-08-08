from gameData import pieceAttack as pak 
from gameData import pieceClassId as pid
from baseProbTable import baseProbTable

import numpy as np

class Piece:
    def __init__(self, probTable = np.zeros((9,9)),attack=10,vitality=100,color=0,classId = 0):
        self.damage = attack
        self.vitality = vitality
        self.alive = True
        self.color = color # 0 is white/ 1 is black

        self.classId = classId

        self.damage = pak[self.classId]
        self.damageProb = probTable[self.classId]

    def updateState(self):
        if self.vitality <= 0:
            self.vitality = 0
            self.alive = False

    def reduceVitality(self, damage=0):
        if self.alive == True:
            self.vitality -= damage
            self.updateState()

    def attack(self,anotherPiece):
        # another piece is an object of class Piece

        if not isinstance(anotherPiece,Piece):
            raise Exception("Piece can only attack another piece")

        anotherPiece.reduceVitality(damage=self.damage)

    
        



