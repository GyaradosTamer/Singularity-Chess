import abc
from directions import *
from GlobalVars import *

class Piece:
	__metaclass__ = abc.ABCMeta

	def __init__(self, color, position):
		self.color = color
		self.position = position
		self.moved = False

	# functions implemented by subclasses
	@abc.abstractmethod
	def getValidMoves(self, board):
		pass
	@abc.abstractmethod
	def getValue(self):
		pass

	# functions in abstract class
	def makeMove(self, newPos, board):
		if newPos not in self.getValidMoves(board):
			raise ValueError("Move not valid")
		self.moved = True
		
		toPiece = board.getPieceAtPosition(newPos)
		if toPiece != None:
	  		if toPiece.getColor() != self.getColor():
				board.updateScore(self.color, toPiece.capture(board))
	  		else:
				raise ValueError("Moving to space with piece of same color")

		board.setPieceAtPosition(self.position, None)
		board.setPieceAtPosition(newPos, self)
		self.position = newPos

	def hasBeenMoved(self):
		return self.moved

	def getPosition(self):
		return self.position

	def getColor(self):
		return self.color

	def capture(self, board):
		# remove piece from board, return point value 
		board.removePieceAtPosition(self.position)
		return self.getValue()


class Pawn(Piece):
	def makeMove(self, newPos, board):
		x = super(Pawn, self).makeMove(newPos, board)
		if newPos[1] == 0 and self.getColor() == 'Black':
			board.removePieceAtPosition(newPos)
			queen = Queen(self.getColor(), newPos)
			board.setPieceAtPosition(newPos, queen)
		if newPos[1] == 4:
			if newPos[0] == 0 or newPos[0] == 7:
				board.removePieceAtPosition(newPos)
				queen = Queen(self.getColor(), newPos)
				board.setPieceAtPosition(newPos, queen)
		if newPos[1] == 6:
			if newPos[0] == 1 or newPos[0] == 6:
				board.removePieceAtPosition(newPos)
				queen = Queen(self.getColor(), newPos)
				board.setPieceAtPosition(newPos, queen)
		if newPos[1] == 8:
			if newPos[0] == 2 or newPos[0] == 5:
				board.removePieceAtPosition(newPos)
				queen = Queen(self.getColor(), newPos)
				board.setPieceAtPosition(newPos, queen)
		if newPos[1] == 10:
			if newPos[0] == 3 or newPos[0] == 4:
				board.removePieceAtPosition(newPos)
				queen = Queen(self.getColor(), newPos)
				board.setPieceAtPosition(newPos, queen)

	def getValidMoves(self, board):
		validMoves = []
		
		direct = (1, 0)
		if self.getColor() == black:
			direct = (-1, 0)

		# forward one space or forward two spaces
		firstPos = board.getAdjacentSquare(self.position, direct)
		if firstPos != None and board.getPieceAtPosition(firstPos) == None:
			validMoves.append(firstPos)
			if not self.hasBeenMoved() and firstPos != None:
				secondPos = board.getAdjacentSquare(firstPos, direct)
				if board.getPieceAtPosition(secondPos) == None:
					validMoves.append(secondPos)
		# top right and top left if pieces there are of opposite color
		forwardLeftSquare = board.getAdjacentSquare(self.position, (direct[0], -1))
		if forwardLeftSquare != None:
			piece = board.getPieceAtPosition(forwardLeftSquare)
			if piece != None and piece.getColor() != self.getColor():
				validMoves.append(forwardLeftSquare)
		forwardRightSquare = board.getAdjacentSquare(self.position, (direct[0], 1))
		if forwardRightSquare != None:
			piece = board.getPieceAtPosition(forwardRightSquare)
			if piece != None and piece.getColor() != self.getColor():
				validMoves.append(forwardRightSquare)

		return validMoves

	def getValue(self):
		return 1

	def toString(self):
		return self.getColor() + "Pawn"


class Knight(Piece):
	def getValidMoves(self, board):
		validMoves = []
		allDirections = [(1, 0), (-1, 0),  (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		for direction in directions:
			pos = self.position
			nextSquares = []
			pos2 = board.getAdjacentSquare(pos, direction)
			if pos2 == None:
				continue
			if direction == (1,0):
				nextSquares.append(board.getAdjacentSquare(pos2, (1,1)))
				nextSquares.append(board.getAdjacentSquare(pos2, (1,-1)))
				for square in nextSquares:
					if square != None:
						if board.getPieceAtPosition(square) == None:
							validMoves.append(square)
						elif board.getPieceAtPosition(square) != None and board.getPieceAtPosition(square).getColor() != self.getColor():
							validMoves.append(square)
			elif direction == (-1,0):
				nextSquares.append(board.getAdjacentSquare(pos2, (-1,-1)))
				nextSquares.append(board.getAdjacentSquare(pos2, (-1,1)))
				for square in nextSquares:
					if square != None:
						if board.getPieceAtPosition(square) == None:
							validMoves.append(square)
						elif board.getPieceAtPosition(square) != None and board.getPieceAtPosition(square).getColor() != self.getColor():
							validMoves.append(square)
			elif direction == (0,1):
				nextSquares.append(board.getAdjacentSquare(pos2, (1,1)))
				nextSquares.append(board.getAdjacentSquare(pos2, (-1,1)))
				for square in nextSquares:
					if square != None:
						if board.getPieceAtPosition(square) == None:
							validMoves.append(square)
						elif board.getPieceAtPosition(square) != None and board.getPieceAtPosition(square).getColor() != self.getColor():
							validMoves.append(square)
			elif direction == (0,-1):
				nextSquares.append(board.getAdjacentSquare(pos2, (-1,-1)))
				nextSquares.append(board.getAdjacentSquare(pos2, (1,-1)))
				for square in nextSquares:
					if square != None:
						if board.getPieceAtPosition(square) == None:
							validMoves.append(square)
						elif board.getPieceAtPosition(square) != None and board.getPieceAtPosition(square).getColor() != self.getColor():
							validMoves.append(square)

		return validMoves

	def getValue(self):
		return 3

	def toString(self):
		return self.getColor() + 'Knight'


class Rook(Piece):
	def getValidMoves(self, board):
		validMoves = []
		allDirections = [(1, 0), (-1, 0),  (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		for direction in directions:
			pos = self.position
			lastPosition = None
			endOfMove = False
			currentDirection = direction
			while endOfMove == False:
				nextSquare = board.getAdjacentSquare(pos, currentDirection)
				if nextSquare != None:
					if nextSquare == lastPosition:
						endOfMove = True
						continue
					elif board.getPieceAtPosition(nextSquare) == None:
						validMoves.append(nextSquare)
					elif board.getPieceAtPosition(nextSquare) != None and board.getPieceAtPosition(nextSquare).getColor() != self.getColor():
						validMoves.append(nextSquare)
						endOfMove = True
						continue
					else:
						endOfMove = True
					lastPosition = pos
					pos = nextSquare
					for d in allDirections:
						square = board.getAdjacentSquare(pos, d)
						if square == lastPosition:
							currentDirection = (-1*d[0], -1*d[1])
							break
				else: endOfMove = True
		return validMoves

	def getValue(self):
		return 5

 	def toString(self):
		return self.getColor() + 'Rook'


class Bishop(Piece):
	def getValidMoves(self, board):
		validMoves = []
		allDirections = [(1, 0), (-1, 0),  (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
		directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
		for direction in directions:
			pos = self.position
			lastPosition = None
			endOfMove = False
			currentDirection = direction
			while endOfMove == False:
				nextSquare = board.getAdjacentSquare(pos, currentDirection)
				if nextSquare != None:
					if nextSquare == lastPosition:
						endOfMove = True
					elif board.getPieceAtPosition(nextSquare) == None:
						validMoves.append(nextSquare)
					elif board.getPieceAtPosition(nextSquare) != None and board.getPieceAtPosition(nextSquare).getColor() != self.getColor():
						validMoves.append(nextSquare)
						endOfMove = True
						continue
					else:
						endOfMove = True
					lastPosition = pos
					pos = nextSquare
					for d in allDirections:
						square = board.getAdjacentSquare(pos, d)
						if square == lastPosition:
							currentDirection = (-1*d[0], -1*d[1])
							break
				else: endOfMove = True
		return validMoves

	def getValue(self):
		return 3

  	def toString(self):
		return self.getColor() + 'Bishop'


class Queen(Piece):
	def getValidMoves(self, board):
		validMoves = []
		allDirections = [(1, 0), (-1, 0),  (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
		directions = allDirections
		for direction in directions:
			pos = self.position
			lastPosition = None
			endOfMove = False
			currentDirection = direction
			while endOfMove == False:
				nextSquare = board.getAdjacentSquare(pos, currentDirection)
				if nextSquare != None:
					if nextSquare == lastPosition:
						endOfMove = True
					elif board.getPieceAtPosition(nextSquare) == None:
						validMoves.append(nextSquare)
					elif board.getPieceAtPosition(nextSquare) != None and board.getPieceAtPosition(nextSquare).getColor() != self.getColor():
						validMoves.append(nextSquare)
						endOfMove = True
					else:
						endOfMove = True
					lastPosition = pos
					pos = nextSquare
					for d in allDirections:
						square = board.getAdjacentSquare(pos, d)
						if square == lastPosition:
							currentDirection = (-1*d[0], -1*d[1])
							break
				else: endOfMove = True
		return validMoves

	def getValue(self):
		return 9

  	def toString(self):
		return self.getColor() + 'Queen'


class King(Piece):
	def getValidMoves(self, board):
		validMoves = []
		allDirections = [(1, 0), (-1, 0),  (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
		directions = allDirections
		for direction in directions:
			pos = self.position
			currentDirection = direction
			nextSquare = board.getAdjacentSquare(pos, currentDirection)
			if nextSquare != None:
				if board.getPieceAtPosition(nextSquare) == None:
					validMoves.append(nextSquare)
				elif board.getPieceAtPosition(nextSquare) != None and board.getPieceAtPosition(nextSquare).getColor() != self.getColor():
					validMoves.append(nextSquare)

		return validMoves

	def getValue(self):
		return 99999

  	def toString(self):
		return self.getColor() + 'King'





