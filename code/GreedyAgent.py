import random
import math
from GlobalVars import *

class GreedyAgent:
	def __init__(self, color):
		self.color = color
		self.opponentColor = "Black"
		if self.color == "Black":
			self.opponentColor = "White"

	def evaluationFunction(self, board):
		checkValue = board.isInCheck(self.opponentColor)
		if checkValue == True:
			checkValue = 3
		else: checkValue = 0
		return board.getScore(self.color) - board.getScore(self.opponentColor) + checkValue

	def getNextMove(self, board):
		moveList = board.getAllValidMoves(self.color)
		if moveList == checkmate or moveList == stalemate:
			return moveList

		bestMove = []
		bestVal = float("-inf")

		for pieceTuple in moveList:
			for move in pieceTuple[1]:
				boardCp = board.copyBoard()
				boardCp.getPieceAtPosition(pieceTuple[0]).makeMove(move, boardCp)

				testUtil = self.evaluationFunction(boardCp)
				if testUtil >= bestVal:
					bestVal = testUtil
					bestMove.append((pieceTuple[0], move))
		return random.choice(bestMove)

