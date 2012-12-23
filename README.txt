SINGULARITY CHESS README (CS221 FINAL PROJECT)
Miguel Francisco (SUID:miguelf), Steven Longoria (SUID: sxl1092), Roneil Rumburg (SUID: roneil)

Note: All of the code is in the "code" folder

——USAGE-----
The main entry point into our program is SingularityChess.py, which handles
setting up the program and running it with the given arguments. Its usage
information is listed below.

Usage: python SingularityChess.py whiteAgent blackAgent [simulationNum]
whiteAgent and blackAgent can be one of [RandomAgent, MinimaxAgent, MonteCarloAgent, GreedyAgent]
simulationNum, the optional parameter, determines whether or not simulation mode is used.
simulation mode disables graphics and plays out the given number of simulationNum internally if set.


——MODULES-----
Board.py holds all functions and data necessary for maintaining and updating
the game state, which is represented as a list of lists, describing what piece,
if any, is on each space.

Pieces.py contains a class for each piece, and each piece’s set of valid moves
(based on the dictionary in directions.py), point value, color, and position. 

directions.py contains a very large dictionary structure that holds the
adjacent spaces for each space and the directions from the original space to
get to those adjacent space. These directions are not the same as normal chess,
which is why we had to have this module to account for the exceptions created
by the warped nature of the middle of the board in Singularity Chess.

GlobalVars.py contains global variables that are used often across the program
and all its modules.

Graphics.py contains all functions and data to create images, draw the board
when given a game state, and to move pieces.

SingularityChess.py is the main file that executes the program, initializing
the board state, graphics, and different agents depending on the provided
command line arguments.

RandomAgent.py is an agent that returns a random move based on the set of valid
moves, given a game state.

GreedyAgent.py is an agent that returns the move that will generate the most
points based on an evaluation function. See the final report for more
documentation.

MonteCarloAgent.py is an agent that samples a set of random moves and picks the
best one to a certain depth, similar to minimax. See the final report for more
documentation.

MinimaxAgent.py is a minimax agent that looks ahead by a certain specified
depth, predicting the opponent’s future moves, and picks the most optimal move
based on that. See the final report for more documentation.
