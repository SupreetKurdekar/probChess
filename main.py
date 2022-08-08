# from piece import Piece

# piece1 = Piece(attack=20)

# piece2 = Piece(attack=10)


# while(piece1.alive and piece2.alive):
#     piece1.attack(piece2)
#     piece2.attack(piece1)

#     print("Piece1 health: ",piece1.vitality)
#     print("Piece2 health: ",piece2.vitality)



from gameManager import gameManager

gm = gameManager()

gm.initializeBoard()

print(gm.board)