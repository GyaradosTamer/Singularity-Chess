"""
To check the space that is in direction d from position p, use directionsDict[d][p]
For example, directionsDict[(1,6)][(1,0)] gets the space that is (1,0), or north from (1,6)

If a space p is a singularity, directionsDict[p]['Singularity'] will be True. Note that p is a tuple.
If a space p is one of the diagonal exceptions above or below the singularity, directionsDict[p]['Exception'] will be True.

Note that initializedirectionsDict() must be called first for any of this to work.
"""

directionsDict = { (0,0): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (0,1): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (0,2): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (0,3): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (0,4): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 

               (1,0): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (1,1): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (1,2): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (1,3): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (1,4): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (1,5): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (1,6): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 

               (2,0): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (2,1): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (2,2): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (2,3): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (2,4): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (2,5): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (2,6): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (2,7): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (2,8): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 

               (3,0): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,1): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,2): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,3): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,4): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,5): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,6): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,7): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,8): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,9): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (3,10): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 

               (4,0): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,1): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,2): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,3): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,4): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,5): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,6): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,7): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,8): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,9): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (4,10): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 

               (5,0): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (5,1): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (5,2): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (5,3): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (5,4): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (5,5): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (5,6): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (5,7): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (5,8): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 

               (6,0): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (6,1): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (6,2): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (6,3): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (6,4): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (6,5): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (6,6): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 

               (7,0): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (7,1): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (7,2): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (7,3): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}, 
               (7,4): {(1,0):None, (1,1):None, (0,1):None, (-1,1):None, (-1,0):None, (-1,-1):None, (0,-1):None, (1,-1):None, 'Singularity':False, 'ExceptionTop':False, 'ExceptionBottom':False}
          }

def processSingularity(col, row):
     boundaries = {0:4, 1:6, 2:8, 3:10, 4:10, 5:8, 6:6, 7:4}
     if col >= 0 and col <= 2:
          directionsDict[(col,row)][(1,0)] = (col+1, row+2)
          directionsDict[(col,row)][(1,1)] = (col+1, row+1)
          directionsDict[(col,row)][(0,1)] = (col+1, row)
          directionsDict[(col,row)][(-1,1)] = (col+1, row-1)
          directionsDict[(col,row)][(-1,0)] = (col, row-1)
          directionsDict[(col,row)][(-1,-1)] = (col-1, row-1)
          directionsDict[(col,row)][(0,-1)] = (col, row+1)
          directionsDict[(col,row)][(1,-1)] = (col+1, row+3)

     #columns 3 and 4 are the two semi-circles in the center of the board
     if col == 3:
          directionsDict[(col,row)][(1,0)] = (col+1, row)
          directionsDict[(col,row)][(1,1)] = (col+1, row)
          directionsDict[(col,row)][(0,1)] = (col+1, row)
          directionsDict[(col,row)][(-1,1)] = (col+1, row-1)
          directionsDict[(col,row)][(-1,0)] = (col, row-1)
          directionsDict[(col,row)][(-1,-1)] = (col-1, row-1)
          directionsDict[(col,row)][(0,-1)] = (col, row+1)
          directionsDict[(col,row)][(1,-1)] = (col+1, row+1)
     if col == 4:
          directionsDict[(col,row)][(1,0)] = (col-1, row)
          directionsDict[(col,row)][(1,1)] = (col-1, row+1)
          directionsDict[(col,row)][(0,1)] = (col, row+1)
          directionsDict[(col,row)][(-1,1)] = (col+1, row-1)
          directionsDict[(col,row)][(-1,0)] = (col, row-1)
          directionsDict[(col,row)][(-1,-1)] = (col-1, row-1)
          directionsDict[(col,row)][(0,-1)] = (col-1, row)
          directionsDict[(col,row)][(1,-1)] = (col-1, row)
     if col >= 5 and col <= 7:
          directionsDict[(col,row)][(1,0)] = (col-1, row+2)
          directionsDict[(col,row)][(1,1)] = (col-1, row+3)
          directionsDict[(col,row)][(0,1)] = (col, row+1)
          directionsDict[(col,row)][(-1,1)] = (col+1, row-1)
          directionsDict[(col,row)][(-1,0)] = (col, row-1)
          directionsDict[(col,row)][(-1,-1)] = (col-1, row-1)
          directionsDict[(col,row)][(0,-1)] = (col-1, row)
          directionsDict[(col,row)][(1,-1)] = (col-1, row+1)

     #eliminating positions out of bounds
     for direction in directionsDict[(col,row)].keys():
          if direction != 'Singularity' and direction != 'ExceptionTop' and direction != 'ExceptionBottom':
               c =  directionsDict[(col, row)][direction][0]
               r =  directionsDict[(col, row)][direction][1]
               if c < 0 or c > 7 or r < 0 or r > boundaries[c]:
                    directionsDict[col,row][direction] = None
     directionsDict[(col, row)]['Singularity'] = True


def processOtherException(col, row):
     singularities = {0:2, 1:3, 2:4, 3:5, 4:5, 5:4, 6:3, 7:2}
     boundaries = {0:4, 1:6, 2:8, 3:10, 4:10, 5:8, 6:6, 7:4}
     
     directionsDict[(col,row)][(1,0)] = (col, row+1)
     directionsDict[(col,row)][(1,1)] = (col+1, row+1)
     directionsDict[(col,row)][(0,1)] = (col+1, row)
     directionsDict[(col,row)][(-1,1)] = (col+1, row-1)
     directionsDict[(col,row)][(-1,0)] = (col, row-1)
     directionsDict[(col,row)][(-1,-1)] = (col-1, row-1)
     directionsDict[(col,row)][(0,-1)] = (col-1, row)
     directionsDict[(col,row)][(1,-1)] = (col-1, row+1)

     if row == singularities[col]-1:
          if col >= 0 and col <= 3:
               directionsDict[(col, row)][(1,-1)] = (col, row+2)
          if col >= 4 and col <= 7:
               directionsDict[(col, row)][(1,1)] = (col, row+2)
          directionsDict[(col, row)]['ExceptionBottom'] = True

     if row == singularities[col]+1:
          if col >= 0 and col <= 3:
               directionsDict[(col, row)][(-1,-1)] = (col, row-2)
          if col >= 4 and col <= 7:
               directionsDict[(col, row)][(-1,1)] = (col, row-2)
          directionsDict[(col, row)]['ExceptionTop'] = True

     for direction in directionsDict[(col,row)].keys():
          if direction != 'Singularity' and direction != 'ExceptionTop' and direction != 'ExceptionBottom':
               c =  directionsDict[(col,row)][direction][0]
               r =  directionsDict[(col, row)][direction][1]
               if c < 0 or c > 7 or r < 0 or r > boundaries[c]:
                    directionsDict[(col,row)][direction] = None


def initializedirectionsDict():
     boundaries = {0:4, 1:6, 2:8, 3:10, 4:10, 5:8, 6:6, 7:4}
     singularities = {0:2, 1:3, 2:4, 3:5, 4:5, 5:4, 6:3, 7:2}

     for pos in directionsDict.keys():
          for direction in directionsDict[pos].keys():
               if direction != 'Singularity' and direction != 'ExceptionTop' and direction != 'ExceptionBottom':
                    col = pos[0]+direction[1]
                    row = pos[1]+direction[0]
                    if singularities[pos[0]] == pos[1]:
                         processSingularity(pos[0], pos[1])
                         continue

                    if singularities[pos[0]] == pos[1]+1 or singularities[pos[0]] == pos[1]-1:
                         processOtherException(pos[0], pos[1])
                         continue

                    if pos[1] <= boundaries[pos[0]]/2:
                         if col >= 0 and col <= 7 and row >= 0 and row <= boundaries[col]:
                              directionsDict[pos][direction] = (col, row)
                    else:
                         if pos[0] <= 3:
                              directionsDict[(pos[0],pos[1])][(1,0)] = (pos[0], pos[1]+1)
                              directionsDict[(pos[0],pos[1])][(1,1)] = (pos[0]+1, pos[1]+3)
                              directionsDict[(pos[0],pos[1])][(0,1)] = (pos[0]+1, pos[1]+2)
                              directionsDict[(pos[0],pos[1])][(-1,1)] = (pos[0]+1, pos[1]+1)
                              directionsDict[(pos[0],pos[1])][(-1,0)] = (pos[0], pos[1]-1)
                              directionsDict[(pos[0],pos[1])][(-1,-1)] = (pos[0]-1, pos[1]-3)
                              directionsDict[(pos[0],pos[1])][(0,-1)] = (pos[0]-1, pos[1]-2)
                              directionsDict[(pos[0],pos[1])][(1,-1)] = (pos[0]-1, pos[1]-1)
                              for direction in directionsDict[(pos[0],pos[1])].keys():
                                   if direction != 'Singularity' and direction != 'ExceptionTop' and direction != 'ExceptionBottom':
                                        c =  directionsDict[(pos[0],pos[1])][direction][0]
                                        r =  directionsDict[(pos[0], pos[1])][direction][1]
                                        if c < 0 or c > 7 or r < 0 or r > boundaries[c]:
                                             directionsDict[(pos[0],pos[1])][direction] = None
                         else:
                              directionsDict[(pos[0],pos[1])][(1,0)] = (pos[0], pos[1]+1)
                              directionsDict[(pos[0],pos[1])][(1,1)] = (pos[0]+1, pos[1]-1)
                              directionsDict[(pos[0],pos[1])][(0,1)] = (pos[0]+1, pos[1]-2)
                              directionsDict[(pos[0],pos[1])][(-1,1)] = (pos[0]+1, pos[1]-3)
                              directionsDict[(pos[0],pos[1])][(-1,0)] = (pos[0], pos[1]-1)
                              directionsDict[(pos[0],pos[1])][(-1,-1)] = (pos[0]-1, pos[1]+1)
                              directionsDict[(pos[0],pos[1])][(0,-1)] = (pos[0]-1, pos[1]+2)
                              directionsDict[(pos[0],pos[1])][(1,-1)] = (pos[0]-1, pos[1]+3)
                              for direction in directionsDict[(pos[0],pos[1])].keys():
                                   if direction != 'Singularity' and direction != 'ExceptionTop' and direction != 'ExceptionBottom':
                                        c =  directionsDict[(pos[0],pos[1])][direction][0]
                                        r =  directionsDict[(pos[0], pos[1])][direction][1]
                                        if c < 0 or c > 7 or r < 0 or r > boundaries[c]:
                                             directionsDict[(pos[0],pos[1])][direction] = None

#initializedirectionsDict()
#print directionsDict







