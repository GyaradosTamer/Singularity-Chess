# special sentinel values
black = "Black"
white = "White"
checkmate = "CHECKMATE"
stalemate = "STALEMATE"

def otherColor(color):
	if color == black:
		return white
	else:
		return black