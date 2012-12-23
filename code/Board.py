"""
This file implements the board layout which contains what
pieces are present at each place on the board.
"""

import copy
from Pieces import *
from GlobalVars import *
from directions import *

# I don't yet see how directions are necessary for the methods being implemented

class Board:
  def __init__(self, grid=None, score=None):
    # use a grid if one is given
    if grid != None:
      self.grid = grid
      assert(score != None)
      self.score = score
      return

    # otherwise set up the grid
    self.grid = [
                  [None, None, None, None, None],
                  [None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None],
                  [None, None, None, None, None]
                ]
    # whites
    self.grid[0][0] = Rook(white, (0, 0))
    self.grid[1][0] = Knight(white, (1, 0))
    self.grid[2][0] = Bishop(white, (2, 0))
    self.grid[3][0] = Queen(white, (3, 0))
    self.grid[4][0] = King(white, (4, 0))
    self.grid[5][0] = Bishop(white, (5, 0))
    self.grid[6][0] = Knight(white, (6, 0))
    self.grid[7][0] = Rook(white, (7, 0))

    self.grid[0][1] = Pawn(white, (0, 1))
    self.grid[1][1] = Pawn(white, (1, 1))
    self.grid[2][1] = Pawn(white, (2, 1))
    self.grid[3][1] = Pawn(white, (3, 1))
    self.grid[4][1] = Pawn(white, (4, 1))
    self.grid[5][1] = Pawn(white, (5, 1))
    self.grid[6][1] = Pawn(white, (6, 1))
    self.grid[7][1] = Pawn(white, (7, 1))

    # blacks
    self.grid[0][4] = Rook(black, (0, 4))
    self.grid[1][6] = Knight(black, (1, 6))
    self.grid[2][8] = Bishop(black, (2, 8))
    self.grid[3][10] = Queen(black, (3, 10))
    self.grid[4][10] = King(black, (4, 10))
    self.grid[5][8] = Bishop(black, (5, 8))
    self.grid[6][6] = Knight(black, (6, 6))
    self.grid[7][4] = Rook(black, (7, 4))

    self.grid[0][3] = Pawn(black, (0, 3))
    self.grid[1][5] = Pawn(black, (1, 5))
    self.grid[2][7] = Pawn(black, (2, 7))
    self.grid[3][9] = Pawn(black, (3, 9))
    self.grid[4][9] = Pawn(black, (4, 9))
    self.grid[5][7] = Pawn(black, (5, 7))
    self.grid[6][5] = Pawn(black, (6, 5))
    self.grid[7][3] = Pawn(black, (7, 3))


    # score setup
    self.score = {}
    self.score[black] = 0
    self.score[white] = 0

  def copyBoard(self):
    newBoard = copy.deepcopy(self.grid)
    newScore = copy.deepcopy(self.score)
    return Board(newBoard, newScore)

  def updateScore(self, color, scoreChange):
    self.score[color] += scoreChange

  def getScore(self, color):
    return self.score[color]

  def movePiece(self, fromPos, toPos):
    self.getPieceAtPosition(fromPos).makeMove(toPos, self)

  def getPieceAtPosition(self, position):
    return self.grid[position[0]][position[1]]

  def setPieceAtPosition(self, position, piece):
    self.grid[position[0]][position[1]] = piece

  def removePieceAtPosition(self, position):
    self.setPieceAtPosition(position, None)

  def isInCheck(self, color):
    moveList = self.getAllValidMoves(otherColor(color), False)
    for (position, moves) in moveList:
      for move in moves:
        pieceObject = self.getPieceAtPosition(move)
        if pieceObject != None and isinstance(pieceObject, King) and pieceObject.getColor() == color:
          return True

    return False

  def getMovesInCheck(self, color):
    moveList = self.getAllValidMoves(color, False)
    finalMoveList = []
    for (position, moves) in moveList:
      pieceMoveList = []
      for move in moves:
        boardCopy = self.copyBoard()
        boardCopy.getPieceAtPosition(position).makeMove(move, boardCopy)
        if not boardCopy.isInCheck(color):
          pieceMoveList.append(move)
      if len(pieceMoveList) > 0:
        finalMoveList.append((position, pieceMoveList))
    if len(finalMoveList) == 0: # CHECKMATE!!!!
      return checkmate
    return finalMoveList

  def getAllValidMoves(self, color, checkInCheck=True):
    if checkInCheck and self.isInCheck(color):
      checkMoveList = self.getMovesInCheck(color)
      return checkMoveList
    legalMoves = [] # list of tuples of form (piecePosition, [moves])
    for col in range(0, len(self.grid)):
      for row in range(0, len(self.grid[col])):
        position = (col, row)
        pieceAtPos = self.getPieceAtPosition(position)
        if pieceAtPos == None:
          continue
        elif pieceAtPos.getColor() == color:
          moveList = pieceAtPos.getValidMoves(self)
          if checkInCheck:
            finalMoveList = []
            for move in moveList:
              boardCopy = self.copyBoard()
              boardCopy.getPieceAtPosition(position).makeMove(move, boardCopy)
              if not boardCopy.isInCheck(color):
                finalMoveList.append(move)
            moveList = finalMoveList
          if len(moveList) > 0:
            legalMoves.append((position, moveList))
    if len(legalMoves) == 0:
      return stalemate # not in check but no valid moves
    else:
      return legalMoves

  def getAdjacentSquare(self, position, direction):
    if position == None:
      return None
    return directionsDict[position][direction]

  def getGrid(self):
    return self.grid

