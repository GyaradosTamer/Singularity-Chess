from Graphics import *
from Board import *
from Pieces import *
from GlobalVars import *
from RandomAgent import *
from MonteCarloAgent import *
from GreedyAgent import *
from MinimaxAgent import *
from directions import *
import sys

def printUsage():
	print "Usage: python SingularityChess.py whiteAgent blackAgent [simulationNum]"
	print "whiteAgent and blackAgent can be one of [RandomAgent, MinimaxAgent, MonteCarloAgent, GreedyAgent]"
	print "simulationNum, the optional parameter, determines whether or not simulation mode is used."
	print "simulation mode disables graphics and plays out the given number of simulationNum internally if set."
	sys.exit(1)

def getAgentFromArg(arg, color, simulation):
	if arg == "RandomAgent":
		return RandomAgent(color)
	elif arg == "MinimaxAgent":
		return MinimaxAgent(color)
	elif arg == "MonteCarloAgent":
		return MonteCarloAgent(color)
	elif arg == "GreedyAgent":
		return GreedyAgent(color)
	elif arg == "MinimaxAgent":
		return MinimaxAgent(color)
	else:
		print "Error: Unrecognized agent '" + arg + "', please enter a valid agent name"
		printUsage()

def getColorForMove(numMoves):
	if numMoves % 2 == 1:
		return white
	else:
		return black

def getAgentForMove(numMoves, whiteAgent, blackAgent):
	if numMoves % 2 == 1:
		return whiteAgent
	else:
		return blackAgent

def printWinMessage(numMoves):
	print getColorForMove(numMoves-1) + " checkmated " + getColorForMove(numMoves),
	print "in " + str(numMoves-1) + " moves."

def printStalemateMessage(numMoves):
	print "White and black have stalemated after " + str(numMoves) + " moves."

def checkForStalemate():
	global timeSinceCapture, priorScore, board
	currentScore = board.getScore(black) + board.getScore(white)
	if currentScore == priorScore:
		timeSinceCapture += 1
	else:
		timeSinceCapture = 0
		priorScore = currentScore

	if timeSinceCapture > 50:
		return True
	else:
		return False

# global vars for getAndDrawNextMove
numMoves = 0
board = None
blackAgent = None
whiteAgent = None
boardGraphics = None
root = None

# stalemate tracking
timeSinceCapture = 0
priorScore = 0

def getAndDrawNextMove():
	global numMoves, board, whiteAgent, blackAgent, boardGraphics
	numMoves += 1
	agt = getAgentForMove(numMoves, whiteAgent, blackAgent)
	moveTuple = agt.getNextMove(board)
	if moveTuple == checkmate:
		printWinMessage(numMoves)
		sys.exit(0)
	elif moveTuple == stalemate or checkForStalemate():
		printStalemateMessage(numMoves)
		sys.exit(0)
	board.movePiece(moveTuple[0], moveTuple[1])
	boardGraphics.drawBoard(board.getGrid())
	root.after(1000, getAndDrawNextMove)

if __name__ == "__main__":
	initializedirectionsDict()

	if len(sys.argv) != 3 and len(sys.argv) != 4:
		print "Error: Incorrect number of arguments"
		printUsage()

	simulation = False
	if len(sys.argv) == 4:
		simulation = True
		simulationNum = int(sys.argv[3])

	whiteAgent = getAgentFromArg(sys.argv[1], white, simulation)
	blackAgent = getAgentFromArg(sys.argv[2], black, simulation)

	if simulation: # don't use graphics
		whiteWins = 0
		blackWins = 0
		stalemates = 0
		for simulation in range(simulationNum):
			# global vars for getAndDrawNextMove
			numMoves = 0
			board = Board()

			# stalemate tracking
			timeSinceCapture = 0
			priorScore = 0

			while True:
				numMoves += 1
				agt = getAgentForMove(numMoves, whiteAgent, blackAgent)
				moveTuple = agt.getNextMove(board)
				if moveTuple == checkmate:
					printWinMessage(numMoves)
					if getColorForMove(numMoves) == white: # the loser
						blackWins += 1
					else:
						whiteWins += 1
					break
				elif moveTuple == stalemate or checkForStalemate():
					printStalemateMessage(numMoves)
					stalemates += 1
					break
				board.movePiece(moveTuple[0], moveTuple[1])

		print "Game statistics:"
		print "Games: %d" % simulationNum
		print "White wins: %d" % whiteWins
		print "Black wins: %d" % blackWins
		print "Stalemates: %d" % stalemates
	else: # use graphics
		root = Tk()
		boardGraphics = BoardGraphics(root)
		board = Board()
		boardGraphics.drawBoard(board.getGrid())

		root.after(1000, getAndDrawNextMove)
		root.mainloop()
