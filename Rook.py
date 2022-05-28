def find_Peice(Piece_list,piece):
    for p in Piece_list:
        if p == piece:
            return True
    return False
def get_WhitePieces():
    return ['wR','wK','wB','wQ','wK','wP','wN']
def get_BlackPieces():
    return ['BR','BK','BB','BQ','BK','BP','BN']

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


def leftMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((col-1>=0) and  ((chess_grid[row ][col-1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row ][col-1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row ][col -1]))):
        moves.append((row,col-1))
        if find_Peice(Opponent_Piece_Finder(), chess_grid[row][col-1]):
            break
        col-=1
    return moves

def rightMove(chess_grid,piece,row,col,Ally_Piece_Finder,Opponent_Piece_Finder):
    moves = list()
    while ((col+1<=7) and  ((chess_grid[row][col+1] == "" or find_Peice(Opponent_Piece_Finder(),chess_grid[row ][col+1])) and not find_Peice(Ally_Piece_Finder(), chess_grid[row ][col+1 ]))):
        moves.append((row,col+1))
        if find_Peice(Opponent_Piece_Finder(), chess_grid[row][col+1]):
            break
        col+=1
    return moves


def move_Rook(chess_grid,piece,row,col):
    totalMoves_Rook = list()
    if chess_grid[row][col]==piece:
        if piece == "BR":
            up_moves = UpMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            down_moves = DownMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            left_moves = leftMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            right_moves = rightMove(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            for m in up_moves:
                totalMoves_Rook.append(m)
            for m in down_moves:
                totalMoves_Rook.append(m)
            for m in right_moves:
                totalMoves_Rook.append(m)
            for m in left_moves:
                totalMoves_Rook.append(m)

        elif piece == "wR":
            up_moves = UpMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            down_moves = DownMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            left_moves = leftMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            right_moves = rightMove(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            for m in up_moves:
                totalMoves_Rook.append(m)
            for m in down_moves:
                totalMoves_Rook.append(m)
            for m in right_moves:
                totalMoves_Rook.append(m)
            for m in left_moves:
                totalMoves_Rook.append(m)
    return totalMoves_Rook

