from Tkinter import *
from Board import *

class BoardGraphics:
    spacePolygons = {} #The polygons used to bound the clickable area of a space
    highlightedSpaceImages = {} #Images corresponding to currently highlighted spaces
    lastHighlighted = [] #Coordinates of last highlighted spaces
    pieceImages = {}

    #Centers of each space to draw chess pieces
    spaceCenters = {    'A1':(157,583), 'A2':(157,507), 'A3':(157,350), 'A4':(157,192), 'A5':(157,115),
                        
                        'B1':(212,620), 'B2':(212,553), 'B3':(212,481), 'B4':(212,350), 'B5':(212,218), 
                        'B6':(212,145), 'B7':(212,81),
                        
                        'C1':(267,642), 'C2':(267,583), 'C3':(267,523), 'C4':(267,458), 'C5':(267,350), 
                        'C6':(267,242), 'C7':(267,177), 'C8':(267,118), 'C9':(267,59),
                        
                        'D1':(321,652), 'D2':(321,596), 'D3':(321,542), 'D4':(321,484), 'D5':(321,427), 
                        'D6':(321,350), 'D7':(321,274), 'D8':(321,217), 'D9':(321,162), 'D10':(321,107), 'D11':(321,51),
                        
                        'E1':(376,652), 'E2':(376,596), 'E3':(376,542), 'E4':(376,484), 'E5':(376,427), 
                        'E6':(376,350), 'E7':(376,274), 'E8':(376,217), 'E9':(376,162), 'E10':(376,107), 'E11':(376,51),
                        
                        'F1':(431,642), 'F2':(431,583), 'F3':(431,523), 'F4':(431,458), 'F5':(431,350), 
                        'F6':(431,242), 'F7':(431,177), 'F8':(431,118), 'F9':(431,59),
                        
                        'G1':(486,620), 'G2':(486,553), 'G3':(486,481), 'G4':(486,350), 'G5':(486,218), 
                        'G6':(486,145), 'G7':(486,81),
                        
                        'H1':(541,583), 'H2':(541,507), 'H3':(541,350), 'H4':(541,192), 'H5':(541,115)}

    #Bounding coordinates of each space to draw polygons
    coords = {  'A1':[(132,594),(183,633),(184,573),(132,522)], 'A2':[(185,569),(185,498),(150,445),(132,393),(132,518)], 
                'A3':[(185,493),(148,432),(132,359),(143,283),(184,210)], 'A4':[(133,186),(186,134),(185,205),(149,260),(132,317)], 
                'A5':[(132,182), (184,128), (184,70), (133,106)],
                
                'B1':[(187,638),(188,576),(241,606),(241,662)], 'B2':[(187,570),(187,502),(239,543),(239,601)], 
                'B3':[(187,496),(241,540),(241,476),(210,439),(187,386)], 'B4':[(240,472),(198,411),(186,352),(198,293),(239,231)], 
                'B5':[(187,327),(209,265),(239,227),(239,164),(187,206)], 'B6':[(187,132),(239,101),(239,159),(188,198)], 
                'B7':[(187,67),(241,41),(241,99),(187,127)],
                
                'C1':[(242,660),(242,605),(294,622),(296,676)], 'C2':[(242,603),(242,546),(294,566),(295,620)], 
                'C3':[(242,541),(295,561),(293,507),(242,479)], 'C4':[(242,474),(295,504),(295,448),(263,420),(243,382)], 
                'C5':[(295,443),(255,402),(241,351),(253,302),(294,258)], 'C6':[(242,325),(242,231),(295,199),(294,254),(263,284)], 
                'C7':[(243,223),(242,162),(294,141),(294,193)], 'C8':[(242,157),(242,101),(295,84),(295,136)], 
                'C9':[(243,96),(243,40),(294,29),(295,81)],
                
                'D1':[(297,676),(297,624),(350,629),(350,680)], 'D2':[(297,618),(297,567),(349,573),(350,624)], 
                'D3':[(297,563),(296,511),(350,517),(351,569)], 'D4':[(297,505),(297,451),(350,463),(350,513)], 
                'D5':[(297,447),(297,370),(312,394),(350,407),(350,459)], 'D6':[(296,353),(316,393),(349,403),(347,300),(310,315)], 
                'D7':[(297,328),(297,258),(350,243),(350,294),(316,306)], 'D8':[(297,252),(297,198),(349,188),(350,239)], 
                'D9':[(297,194),(297,140),(350,133),(350,184)], 'D10':[(298,135),(297,83),(349,78),(350,130)], 
                'D11':[(297,81),(297,28),(350,23),(350,75)],
                
                'E1':[(352,681),(352,628),(404,623),(404,676)], 'E2':[(352,626),(352,573),(405,567),(406,620)], 
                'E3':[(352,569),(352,518),(404,510),(404,561)], 'E4':[(352,515),(352,464),(406,450),(406,505)], 
                'E5':[(353,460),(352,409),(383,397),(403,373),(405,446)], 'E6':[(352,406),(352,298),(388,313),(405,350),(386,392)], 
                'E7':[(352,294),(352,243),(404,256),(404,257),(404,332)], 'E8':[(352,240),(352,189),(406,198),(406,253)], 
                'E9':[(352,184),(352,134),(403,140),(405,194)], 'E10':[(352,80),(352,132),(406,137),(405,83)], 
                'E11':[(352,74),(353,22),(404,27),(405,80)],
                
                'F1':[(407,676),(407,623),(461,606),(461,662)], 'F2':[(407,619),(408,565),(459,545),(459,601)], 
                'F3':[(407,562),(407,509),(461,477),(460,541)], 'F4':[(408,504),(407,448),(436,422),(458,381),(460,473)], 
                'F5':[(407,445),(407,258),(445,296),(460,350),(447,404)], 'F6':[(408,256),(408,199),(459,230),(459,324),(443,287)], 
                'F7':[(407,196),(408,141),(461,163),(460,225)], 'F8':[(408,137),(408,84),(459,100),(460,158)], 
                'F9':[(407,81),(407,28),(461,42),(460,98)],
                
                'G1':[(463,659),(462,606),(514,575),(514,636)], 'G2':[(462,603),(462,543),(515,503),(515,570)], 
                'G3':[(463,539),(462,475),(497,430),(514,388),(515,496)], 'G4':[(462,472),(462,231),(502,287),(515,351),(500,420)], 
                'G5':[(462,229),(462,163),(516,208),(513,315),(488,255)], 'G6':[(462,162),(462,101),(515,134),(515,204)], 
                'G7':[(462,100),(462,43),(515,67),(515,129)],
                
                'H1':[(518,637),(516,574),(571,522),(570,598)], 'H2':[(518,569),(517,498),(547,452),(569,390),(570,516)], 
                'H3':[(517,496),(517,210),(556,276),(571,350),(556,429)], 'H4':[(517,207),(517,134),(570,189),(570,319),(546,242)], 
                'H5':[(517,133),(517,69),(570,107),(571,183)]}

    def __init__(self, master=None):
        self.boardGIF = PhotoImage(file="Images/Board.gif")
        
        self.boardCanvas = Canvas(master, width=700, height=700, bg='black', highlightthickness=0)
        self.boardCanvas.create_image((350, 350), image=self.boardGIF, state=DISABLED)
        
        for coord in self.coords.keys():
            self.spacePolygons[coord] = self.boardCanvas.create_polygon(self.coords[coord], fill='', tag=('space',coord))
            self.highlightedSpaceImages[coord] = PhotoImage(file="Images/"+coord+".gif")

        colors = ("White", "Black")
        types = ("Pawn", "Knight", "Bishop", "Rook", "Queen", "King")
        for c in colors:
            for t in types:
                self.pieceImages[c+t] = PhotoImage(file="Images/"+c+t+".gif")

        self.boardCanvas.pack()

    def spaceClicked(self, event):

        nullAreaFailSafe = self.lastHighlighted
        for space in self.lastHighlighted:
            item = self.boardCanvas.find_withtag(space+'_HL')
            self.boardCanvas.delete(item)
        self.lastHighlighted = []

        item = self.boardCanvas.find_closest(event.x, event.y)
        tags = self.boardCanvas.gettags(item)
        if tags.__len__() > 0 and (tags[0] == 'space' or tags[0] == 'piece'):
            print "Clicked space", tags[1], event.y
            l = [tags[1]]
            self.highlightSpaces(l)
            return tags[1]
        else: 
            self.highlightSpaces(nullAreaFailSafe)
            return ""

    def highlightSpaces(self, spaces):
        """
        Highlights all spaces in the parameter spaces, which is a list.
        """

        for space in spaces:
            self.boardCanvas.create_image((350,350), image=self.highlightedSpaceImages[space], tags=space+'_HL')
            self.lastHighlighted.append(space)

    #def animate(self, start, end):


    def movePiece(self, start, end):
        """
        Moves the piece at space start to space end. 
        start and end are space names such as A1, B3, etc.
        """
        piece = self.boardCanvas.find_closest(self.spaceCenters[start][0], self.spaceCenters[start][1])
        tags = self.boardCanvas.gettags(piece)
        if tags.__len__() > 0 and tags[0] == 'piece':
            self.boardCanvas.delete(piece)
            self.boardCanvas.create_image(self.spaceCenters[end], image=self.pieceImages[tags[2]], tag=('piece', end, tags[2]))

    def tupleToCoord(self, pos):
        mappings = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}
        return mappings[pos[0]] + str(pos[1]+1) 

    def drawBoard(self, board):
        for space in self.spaceCenters.values():
            item = self.boardCanvas.find_closest(space[0], space[1])
            tags = self.boardCanvas.gettags(item)
            if tags.__len__() > 0 and tags[0] == 'piece':
                self.boardCanvas.delete(item)
        for x in range(8):
            for y in range(board[x].__len__()):
                if board[x][y] != None:
                    coordString = self.tupleToCoord((x,y))
                    pieceString = board[x][y].toString()
                    self.boardCanvas.create_image(self.spaceCenters[coordString], image=self.pieceImages[pieceString], 
                                                    tag=('piece', coordString, pieceString))

    def getCanvas(self):
        return self.boardCanvas


def callback(event):
    print "Clicked at: ", event.x, event.y  




