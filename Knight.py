def find_Peice(Piece_list,piece):
    for p in Piece_list:
        if p == piece:
            return True
    return False
def get_WhitePieces():
    return ['wR','wK','wB','wQ','wK','wP','wN']
def get_BlackPieces():
    return ['BR','BK','BB','BQ','BK','BP','BN']
def Up_Move(chess_grid,piece,row,col,Ally_Piece_list,Opponent_Piece_List):
    moves = list()
    if row - 2 >= 0 and col + 1 <= 7:
        if ((chess_grid[row - 2][col + 1] == "" or find_Peice(Opponent_Piece_List(),chess_grid[row - 2][col + 1])) and not find_Peice(Ally_Piece_list(), chess_grid[row - 2][col + 1])):
            moves.append((row-2,col+1))
    if row - 2 >= 0 and col - 1 >= 0:
        if ((chess_grid[row - 2][col - 1] == "" or find_Peice(Opponent_Piece_List(),chess_grid[row - 2][col - 1])) and not find_Peice(Ally_Piece_list(), chess_grid[row - 2][col - 1])):
            moves.append((row-2,col-1))
    return moves
def Down_Move(chess_grid,piece,row,col,Ally_Piece_list,Opponent_Piece_List):
    moves = list()
    if row + 2 <=7 and col + 1 <= 7:
        if ((chess_grid[row + 2][col + 1] == "" or find_Peice(Opponent_Piece_List(),chess_grid[row + 2][col + 1])) and not find_Peice(Ally_Piece_list(), chess_grid[row + 2][col + 1])):
            moves.append((row+2,col+1))
    if row + 2 <=7 and col - 1 >= 0:
        if ((chess_grid[row + 2][col - 1] == "" or find_Peice(Opponent_Piece_List(),chess_grid[row + 2][col - 1])) and not find_Peice(Ally_Piece_list(), chess_grid[row + 2][col - 1])):
            moves.append((row+2,col-1))
    return moves
def Right_Move(chess_grid,piece,row,col,Ally_Piece_list,Opponent_Piece_List):
    moves = list()
    if row - 1>=0 and col + 2 <= 7:
        if ((chess_grid[row - 1][col + 2] == "" or find_Peice(Opponent_Piece_List(),chess_grid[row - 1][col + 2])) and not find_Peice(Ally_Piece_list(), chess_grid[row - 1][col + 2])):
            moves.append((row - 1,col+2))
    if row + 1<=7 and col + 2 <= 7:
        if ((chess_grid[row + 1][col + 2] == "" or find_Peice(Opponent_Piece_List(),chess_grid[row + 1][col + 2])) and not find_Peice(Ally_Piece_list(), chess_grid[row + 1][col + 2])):
            moves.append((row+1,col+2))
    return moves

def Left_Move(chess_grid,piece,row,col,Ally_Piece_list,Opponent_Piece_List):
    moves = list()
    if row - 1>=0 and col - 2>=0:
        if ((chess_grid[row - 1][col - 2] == "" or find_Peice(Opponent_Piece_List(),chess_grid[row - 1][col - 2])) and not find_Peice(Ally_Piece_list(), chess_grid[row - 1][col - 2])):
            moves.append((row - 1,col-2))
    if row + 1<=7 and col - 2 >=0:
        if ((chess_grid[row + 1][col - 2] == "" or find_Peice(Opponent_Piece_List(),chess_grid[row + 1][col - 2])) and not find_Peice(Ally_Piece_list(), chess_grid[row + 1][col - 2])):
            moves.append((row+1,col-2))
    return moves



def move_Knight(chess_grid,piece,row,col):
    totalMoves_Knight = list()
    if chess_grid[row][col]==piece:
        if piece == 'BN':
            up_moves = Up_Move(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            down_moves = Down_Move(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            left_moves  = Left_Move(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            right_moves = Right_Move(chess_grid, piece, row, col,get_BlackPieces,get_WhitePieces)
            for m in up_moves:
                totalMoves_Knight.append(m)
            for m in down_moves:
                totalMoves_Knight.append(m)
            for m in right_moves:
                totalMoves_Knight.append(m)
            for m in left_moves:
                totalMoves_Knight.append(m)

        elif piece  == 'wN':
            up_moves = Up_Move(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            down_moves = Down_Move(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            left_moves = Left_Move(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            right_moves = Right_Move(chess_grid, piece, row, col, get_WhitePieces, get_BlackPieces)
            for m in up_moves:
                totalMoves_Knight.append(m)
            for m in down_moves:
                totalMoves_Knight.append(m)
            for m in right_moves:
                totalMoves_Knight.append(m)
            for m in left_moves:
                totalMoves_Knight.append(m)


    return totalMoves_Knight





