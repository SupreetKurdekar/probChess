from cmath import pi

import pygame
from piece import Piece
import random

class square:
    def __init__(self,row,col,*args):

        self.row = row
        self.col = col
        self.whitePieces = []
        self.blackPieces = []

        if len(args) >= 1 and isinstance(args[0],Piece):
            # check if this arg is a piece

            if args[0].color == 0:
                self.whitePieces.append(args[0])
            else:
                self.blackPieces.append(args[0]) 

        # if len(args) >= 2 and isinstance(args[1],int):

        #     if args[0].color == 0:
        #         self.whitePieces.append(args[0])
        #     else:
        #         self.blackPieces.append(args[0]) 


        # graphics
        self.length = 100
        if (self.row + self.col)%2 == 0:
            self.color = (0,255,0)
        else:
            self.color = (255,255,255)

        self.x = self.length*col
        self.y = 800 - self.length*(row+1)


            
    def addPiece(self,piece):
        if piece.color == 0:
            self.whitePieces.append(piece)
        else:
            self.blackPieces.append(piece)      

    def fight(self,piece1,piece2):
        if piece1.color == piece2.color:
            return piece1,piece2

        if piece1.color == 0:
            wPiece = piece1
            bPiece = piece2
        else:
            wPiece = piece2
            bPiece = piece1

        wProb = wPiece.damageProb[bPiece.classId]
        bProb = bPiece.damageProb[wPiece.classId]

        wProb = wProb/(wProb + bProb)
        bProb = 1 - wProb

        dice = random.random()

        if dice <= wProb:
            wPiece.attack(bPiece)
        else:
            bPiece.attack(wPiece)

        return wPiece,bPiece

    def fightUpdate(self):

        if len(self.whitePieces) > 0 and len(self.blackPieces) > 0:

            # in future this will be managed by fightSeqmanager
            # will retuurn new white and blck piece lists

            newWhitePieces = []
            newBlackPieces = []

            for wPiece in self.whitePieces:
                for bPiece in self.blackPieces:
                    wPiece,bPiece = self.fight(wPiece,bPiece)


                    if wPiece.alive:
                        newWhitePieces.append(wPiece)

                    if bPiece.alive:
                        newBlackPieces.append(bPiece)

        
            # sorting based on life left
            newWhitePieces.sort(key=lambda x: x.vitality, reverse=True)
            newBlackPieces.sort(key=lambda x: x.vitality, reverse=True)

            self.whitePieces = newWhitePieces
            self.blackPieces = newBlackPieces
        
    def probUpdate():
        # this function should update the probabilities of all its pieces

        pass


    # some button click functions to allow to select pieces

    def drawPieces(self,screen):
        if len(self.blackPieces) == 0 and len(self.whitePieces) == 0:
            pass

        elif len(self.blackPieces) == 1 and len(self.whitePieces) == 0:
            screen.blit(self.blackPieces[0].sprite,(self.x,self.y))
        else:
            screen.blit(self.whitePieces[0].sprite,(self.x,self.y))