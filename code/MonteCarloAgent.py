import random
import math
from GlobalVars import *

class MonteCarloAgent:
	def __init__(self, color, depth=1, numSamples=5):
		self.color = color
		self.opponentColor = "Black"
		if self.color == "Black":
			self.opponentColor = "White"
		self.depth = depth
		self.numSamples = numSamples

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

		for i in range(self.numSamples):
			boardCp = board.copyBoard()
			pieceTuple = random.choice(moveList)
			move = random.choice(pieceTuple[1])
			boardCp.getPieceAtPosition(pieceTuple[0]).makeMove(move, boardCp)

			testUtil = self.minValue(boardCp, self.depth)
			if testUtil > bestVal:
				bestVal = testUtil
				bestMove.append((pieceTuple[0], move))
		return random.choice(bestMove)

	def maxValue(self, board, count):
		moveList = board.getAllValidMoves(self.color)
		if moveList == checkmate or moveList == stalemate:
			return self.evaluationFunction(board)
		if count == 0:
			return self.evaluationFunction(board)

		bestVal = float("-inf")
		for i in range((int)(self.numSamples*1/math.pow(2,self.depth-count))):
			boardCp = board.copyBoard()
			pieceTuple = random.choice(moveList)
			move = random.choice(pieceTuple[1])
			boardCp.getPieceAtPosition(pieceTuple[0]).makeMove(move, boardCp)

			testUtil = self.minValue(boardCp, count)
			if testUtil > bestVal:
				bestVal = testUtil

		return bestVal

	def minValue(self, board, count):
		moveList = board.getAllValidMoves(self.opponentColor)
		if moveList == checkmate or moveList == stalemate:
			return self.evaluationFunction(board)
		if count == 0:
			return self.evaluationFunction(board)

		bestVal = float("inf")
		for i in range((int)(self.numSamples/math.pow(2, self.depth-count))):
			boardCp = board.copyBoard()
			pieceTuple = random.choice(moveList)
			move = random.choice(pieceTuple[1])
			boardCp.getPieceAtPosition(pieceTuple[0]).makeMove(move, boardCp)

			testUtil = self.maxValue(boardCp, count-1)
			if testUtil < bestVal:
				bestVal = testUtil

		return bestVal

