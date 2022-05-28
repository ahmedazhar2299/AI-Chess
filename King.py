import copy

from Pawn import *
from Knight import *
from Rook import *
from Bishop import*
from Queen import*


def find_Peice(Piece_list,piece):
    for p in Piece_list:
        if p == piece:
            return True
    return False
def get_WhitePieces():
    return ['wR','wB','wQ','wK','wP','wN']
def get_BlackPieces():
    return ['BR','BB','BQ','BK','BP','BN']
def get_Postion_Graph(grid, Opponent_Piece_Finder):
    Graph = dict()
    Pieces = Opponent_Piece_Finder()
    for x in Pieces:
        Graph[x] = list()
    for i in range(8):
        for j in range(8):
            if grid[i][j] in Pieces:
                Graph[grid[i][j]].append((i,j))
    return Graph

def Find(item,list):
    for x in list:
        if item == x:
            return True
    return False

def CheckMate(chess_grid,piece,row,col,Opponent_Piece_Finder):
    Graph  = get_Postion_Graph(chess_grid, Opponent_Piece_Finder)
    flag = False
    for key in Graph:
        if len(Graph[key])>0:
            for x in Graph[key]:
                r,c = x
                if (key!=piece and key=='BP') or (key!=piece and key=='wP'):
                    Pawn_moves = move_Pawn(chess_grid,key,r,c)
                    '''for m in Pawn_moves:
                        A,B = m
                        if A-3==1 and chess_grid[A - 3][B] == 'wP':
                            Pawn_moves.remove(m)
                        elif A-2==2 and chess_grid[A - 2][B] == 'wP':
                            Pawn_moves.remove(m)
                        elif A+2==5 and chess_grid[A + 2][B] == 'BP':
                            Pawn_moves.remove(m)
                        elif A+3==6 and chess_grid[A + 3][B] == 'BP':
                            Pawn_moves.remove(m)'''

                    if len(Pawn_moves )>0:
                        if Find((row,col),Pawn_moves):
                            flag =  True
                if (key!=piece and key=='BR') or (key!=piece and key=='wR'):
                    Rook_moves = move_Rook(chess_grid,key,r,c)
                    if len(Rook_moves)>0:
                        if Find((row,col),Rook_moves):
                            flag =  True
                if (key!=piece and key=='BN') or (key!=piece and key=='wN'):
                    Knight_moves = move_Knight(chess_grid,key,r,c)
                    if len(Knight_moves)>0:
                        if Find((row,col),Knight_moves):
                            flag =  True
                if (key!=piece and key=='BB') or (key!=piece and key=='wB'):
                    Bishop_moves = move_Bishop(chess_grid,key,r,c)
                    if len(Bishop_moves)>0:
                        if Find((row,col),Bishop_moves):
                            flag =  True
                if (key!=piece and key=='BQ') or (key!=piece and key=='wQ'):
                    Queen_moves = move_Queen(chess_grid,key,r,c)
                    if len(Queen_moves)>0:
                        if Find((row,col),Queen_moves):
                            flag =  True

    return flag


def UpRightMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    if (row-1>=0 and col+1<=7):
        Temp_Grid = copy.deepcopy(chess_grid)
        Temp_Grid[row][col] = ""
        Temp_Grid[row-1][col+1] = piece
        if (  ((chess_grid[row - 1][col+1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row - 1][col+1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row - 1][col +1])) and not CheckMate(Temp_Grid,piece,row-1,col+1,Opponent_Piece_Finder)):
           return (row-1,col+1)
    return ()

def UpLeftMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    if (row-1>=0 and col-1>=0):
        Temp_Grid = copy.deepcopy(chess_grid)
        Temp_Grid[row][col] = ""
        Temp_Grid[row-1][col-1] = piece
        if (((chess_grid[row - 1][col-1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row - 1][col-1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row - 1][col -1])) and not CheckMate(Temp_Grid,piece,row-1,col-1,Opponent_Piece_Finder)):
          return (row-1,col-1)
    return ()


def DownRightMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    if (row+1<=7 and col+1<=7):
        Temp_Grid = copy.deepcopy(chess_grid)
        Temp_Grid[row][col] = ""
        Temp_Grid[row+1][col+1] = piece
        if ( ((chess_grid[row + 1][col+1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row + 1][col+1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row + 1][col+1])) and not CheckMate(Temp_Grid,piece,row+1,col+1,Opponent_Piece_Finder)):
           return (row+1,col+1)
    return ()

def DownLeftMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    if (row+1<=7 and col-1>=0):
        Temp_Grid = copy.deepcopy(chess_grid)
        Temp_Grid[row][col] = ""
        Temp_Grid[row+1][col-1] = piece
        if (  ((chess_grid[row + 1][col-1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row + 1][col-1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row + 1][col-1])) and not CheckMate(Temp_Grid,piece,row+1,col-1,Opponent_Piece_Finder)):
           return (row+1,col-1)
    return ()

def UpMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    if (row-1>=0):
        Temp_Grid = copy.deepcopy(chess_grid)
        Temp_Grid[row][col] = ""
        Temp_Grid[row-1][col] = piece
        if (   ((chess_grid[row - 1][col] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row - 1][col])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row - 1][col ])) and not CheckMate(Temp_Grid,piece,row-1,col,Opponent_Piece_Finder)):
           return (row-1,col)
    return ()


def DownMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    if (row+1<=7):
        Temp_Grid = copy.deepcopy(chess_grid)
        Temp_Grid[row][col] = ""
        Temp_Grid[row+1][col] = piece
        if ( ((chess_grid[row + 1][col] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row + 1][col])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row + 1][col])) and not CheckMate(Temp_Grid,piece,row+1,col,Opponent_Piece_Finder)):
            return (row+1,col)
    return ()

def LeftMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    if (col-1>=0):
        Temp_Grid = copy.deepcopy(chess_grid)
        Temp_Grid[row][col] = ""
        Temp_Grid[row][col-1] = piece
        if (((chess_grid[row ][col-1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row ][col-1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row ][col -1])) and not CheckMate(Temp_Grid,piece,row,col-1,Opponent_Piece_Finder)):
            return (row,col-1)
    return ()

def RightMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    if (col+1<=7):
        Temp_Grid = copy.deepcopy(chess_grid)
        Temp_Grid[row][col] = ""
        Temp_Grid[row][col+1] = piece
        if (((chess_grid[row][col+1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row ][col+1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row ][col+1 ])) and not CheckMate(Temp_Grid,piece,row,col+1,Opponent_Piece_Finder)):
            return (row,col+1)
    return ()
def Find_Postion(Grid,piece):
    for i in range(8):
        for j in range(8):
            if piece == Grid[i][j]:
                return (i,j)
    return ()

def King_Positions(chess_grid,row,col):
    positions = list()
    if  row-1>=0 and col-1>=0 and chess_grid[row-1][col-1]=="":
        positions.append((row-1,col-1))
    if  row-1>=0 and chess_grid[row-1][col]=="":
        positions.append((row-1,col))
    if  col-1>=0 and chess_grid[row][col-1]=="":
        positions.append((row,col-1))

    if  row+1<=7 and col+1<=7  and chess_grid[row+1][col+1]=="":
        positions.append((row+1,col+1))
    if  row+1<=7 and chess_grid[row+1][col]=="":
        positions.append((row+1,col))
    if  col+1<=7  and chess_grid[row][col+1]=="":
        positions.append((row,col+1))

    if  row+1<=7 and col-1>=0 and chess_grid[row+1][col-1]=="":
        positions.append((row+1,col-1))
    if  row-1>=0 and col+1<=7  and chess_grid[row-1][col+1]=="":
        positions.append((row-1,col+1))
    return positions




def move_King(chess_grid,piece,row,col):
    wK_r,wK_C = Find_Postion(chess_grid, 'wK')
    BK_r, BK_C = Find_Postion(chess_grid, 'BK')
    Total_Valid_Moves_wK= set(Valid_King_Moves(chess_grid, "wK", wK_r, wK_C))
    Total_Valid_Moves_BK = set(Valid_King_Moves(chess_grid, "BK", BK_r, BK_C))
    if piece == 'wK':
        Total_Valid_Moves_wK = Total_Valid_Moves_wK.difference(Total_Valid_Moves_wK.intersection(Total_Valid_Moves_BK))
        BK_Possible_Moves = King_Positions(chess_grid,BK_r, BK_C)
        for m in list(Total_Valid_Moves_wK):
            if Find(m,BK_Possible_Moves):
                Total_Valid_Moves_wK.remove(m)
        return list(Total_Valid_Moves_wK)
    if piece == 'BK':
        Total_Valid_Moves_BK = Total_Valid_Moves_BK.difference(Total_Valid_Moves_BK.intersection(Total_Valid_Moves_wK))
        wK_Possible_Moves = King_Positions(chess_grid, wK_r, wK_C)
        for m in list(Total_Valid_Moves_BK):
            if Find(m, wK_Possible_Moves):
                Total_Valid_Moves_BK.remove(m)
        return list(Total_Valid_Moves_BK)

    return []



def Valid_King_Moves(chess_grid,piece,row,col):
    totalMoves_King = list()
    if chess_grid[row][col]==piece:
        if piece == "BK":
            move = UpMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            if move != ():
                totalMoves_King.append(move)
            move = DownMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            if move != ():
                totalMoves_King.append(move)
            move = LeftMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            if move != ():
                totalMoves_King.append(move)
            move = RightMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            if move != ():
                totalMoves_King.append(move)
            move = UpRightMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            if move != ():
                totalMoves_King.append(move)
            move = UpLeftMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            if move != ():
                totalMoves_King.append(move)
            move = DownLeftMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            if move != ():
                totalMoves_King.append(move)
            move = DownRightMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            if move != ():
                totalMoves_King.append(move)

        elif piece == "wK":
            move = UpMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            if move!=():
                totalMoves_King.append(move)
            move = DownMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            if move != ():
                totalMoves_King.append(move)
            move = LeftMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            if move != ():
                totalMoves_King.append(move)
            move = RightMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            if move != ():
                totalMoves_King.append(move)
            move = UpRightMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            if move != ():
                totalMoves_King.append(move)
            move = UpLeftMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            if move != ():
                totalMoves_King.append(move)
            move = DownLeftMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            if move != ():
                totalMoves_King.append(move)
            move = DownRightMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            if move != ():
                totalMoves_King.append(move)
    return totalMoves_King



