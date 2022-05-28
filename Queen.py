
def find_Peice(Piece_list,piece):
    for p in Piece_list:
        if p == piece:
            return True
    return False
def get_WhitePieces():
    return ['wR','wK','wB','wQ','wK','wP','wN']
def get_BlackPieces():
    return ['BR','BK','BB','BQ','BK','BP','BN']


def UpRightMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((row-1>=0 and col+1<=7) and  ((chess_grid[row - 1][col+1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row - 1][col+1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row - 1][col +1]))):
        moves.append((row-1,col+1))
        if find_Peice(Opponent_Piece_Finder(),chess_grid[row - 1][col+1]):
            break
        row -= 1
        col +=1

    return moves


def UpLeftMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((row-1>=0 and col-1>=0) and  ((chess_grid[row - 1][col-1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row - 1][col-1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row - 1][col -1]))):
        moves.append((row-1,col-1))
        if find_Peice(Opponent_Piece_Finder(),chess_grid[row - 1][col-1]):
            break
        row -= 1
        col -=1

    return moves

def DownRightMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((row+1<=7 and col+1<=7) and  ((chess_grid[row + 1][col+1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row + 1][col+1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row + 1][col+1]))):
        moves.append((row+1,col+1))
        if find_Peice(Opponent_Piece_Finder(), chess_grid[row + 1][col+1]):
            break
        row += 1
        col += 1
    return moves

def DownLeftMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((row+1<=7 and col-1>=0) and  ((chess_grid[row + 1][col-1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row + 1][col-1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row + 1][col-1]))):
        moves.append((row+1,col-1))
        if find_Peice(Opponent_Piece_Finder(), chess_grid[row + 1][col-1]):
            break
        row += 1
        col -= 1
    return moves

def UpMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((row-1>=0) and  ((chess_grid[row - 1][col] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row - 1][col])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row - 1][col ]))):
        moves.append((row-1,col))
        if find_Peice(Opponent_Piece_Finder(),chess_grid[row - 1][col]):
            break
        row -= 1

    return moves

def DownMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((row+1<=7) and  ((chess_grid[row + 1][col] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row + 1][col])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row + 1][col]))):
        moves.append((row+1,col))
        if find_Peice(Opponent_Piece_Finder(), chess_grid[row + 1][col]):
            break
        row += 1
    return moves


def LeftMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((col-1>=0) and  ((chess_grid[row ][col-1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row ][col-1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row ][col -1]))):
        moves.append((row,col-1))
        if find_Peice(Opponent_Piece_Finder(), chess_grid[row][col-1]):
            break
        col-=1
    return moves

def RightMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((col+1<=7) and  ((chess_grid[row][col+1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row ][col+1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row ][col+1 ]))):
        moves.append((row,col+1))
        if find_Peice(Opponent_Piece_Finder(), chess_grid[row][col+1]):
            break
        col+=1
    return moves



def move_Queen(chess_grid,piece,row,col):
    totalMoves_Queen = list()
    if chess_grid[row][col]==piece:
        if piece == "BQ":
            up_moves = UpMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            down_moves = DownMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            left_moves = LeftMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            right_moves = RightMove(chess_grid, piece, row, col, get_BlackPieces, get_WhitePieces)
            upRight_moves = UpRightMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            upLeft_moves = UpLeftMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            downRight_moves = DownRightMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            downLeft_moves = DownLeftMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            for m in up_moves:
                totalMoves_Queen.append(m)
            for m in down_moves:
                totalMoves_Queen.append(m)
            for m in right_moves:
                totalMoves_Queen.append(m)
            for m in left_moves:
                totalMoves_Queen.append(m)
            for m in upRight_moves:
                totalMoves_Queen.append(m)
            for m in upLeft_moves:
                totalMoves_Queen.append(m)
            for m in downRight_moves:
                totalMoves_Queen.append(m)
            for m in downLeft_moves:
                totalMoves_Queen.append(m)

        elif piece == "wQ":
            up_moves = UpMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            down_moves = DownMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            left_moves = LeftMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            right_moves = RightMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            upRight_moves = UpRightMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            upLeft_moves = UpLeftMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            downRight_moves = DownRightMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            downLeft_moves = DownLeftMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            for m in up_moves:
                totalMoves_Queen.append(m)
            for m in down_moves:
                totalMoves_Queen.append(m)
            for m in right_moves:
                totalMoves_Queen.append(m)
            for m in left_moves:
                totalMoves_Queen.append(m)
            for m in upRight_moves:
                totalMoves_Queen.append(m)
            for m in upLeft_moves:
                totalMoves_Queen.append(m)
            for m in downRight_moves:
                totalMoves_Queen.append(m)
            for m in downLeft_moves:
                totalMoves_Queen.append(m)
    return totalMoves_Queen

