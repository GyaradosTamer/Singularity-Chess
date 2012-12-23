import random
from GlobalVars import *

class RandomAgent:
	def __init__(self, color):
		self.color = color

	def getNextMove(self, board): # return tuple of format (startPos, endPos) for move
		moveList = board.getAllValidMoves(self.color)
		if moveList == checkmate or moveList == stalemate:
			return moveList
		pieceTuple = random.choice(moveList)
		move = random.choice(pieceTuple[1])
		return (pieceTuple[0], move)