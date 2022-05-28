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



def move_Bishop(chess_grid,piece,row,col):
    totalMoves_Rook = list()
    if chess_grid[row][col]==piece:
        if piece == "BB":
            upRight_moves = UpRightMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            upLeft_moves = UpLeftMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            downRight_moves = DownRightMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            downLeft_moves = DownLeftMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            for m in upRight_moves:
                totalMoves_Rook.append(m)
            for m in upLeft_moves:
                totalMoves_Rook.append(m)
            for m in downRight_moves:
                totalMoves_Rook.append(m)
            for m in downLeft_moves:
                totalMoves_Rook.append(m)

        elif piece == "wB":
            upRight_moves = UpRightMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            upLeft_moves = UpLeftMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            downRight_moves = DownRightMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            downLeft_moves = DownLeftMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            for m in upRight_moves:
                totalMoves_Rook.append(m)
            for m in upLeft_moves:
                totalMoves_Rook.append(m)
            for m in downRight_moves:
                totalMoves_Rook.append(m)
            for m in downLeft_moves:
                totalMoves_Rook.append(m)
    return totalMoves_Rook

