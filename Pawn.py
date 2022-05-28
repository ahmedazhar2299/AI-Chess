def find_Peice(Piece_list,piece):
    for p in Piece_list:
        if p == piece:
            return True
    return False
def get_WhitePieces():
    return ['wR','wK','wB','wQ','wK','wP','wN']
def get_BlackPieces():
    return ['BR','BK','BB','BQ','BK','BP','BN']


def move_Pawn(chess_grid,piece,row,col):
    if chess_grid[row][col]==piece:
        if row-1 >=0:
            if piece=='BP' and row==6 and col>0 and col<7:
                if chess_grid[row-1][col]=='' and chess_grid[row-2][col]=='' and find_Peice(get_WhitePieces(),chess_grid[row-1][col-1])  and find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]):
                    return [(row-1,col),(row-2,col),(row-1,col+1),(row-1,col-1)]
                elif chess_grid[row - 1][col] == '' and chess_grid[row - 2][col] == '' and find_Peice(get_WhitePieces(),chess_grid[row - 1][col - 1]) and not find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]):
                    return [(row - 1, col), (row - 2, col), (row - 1, col - 1)]
                elif chess_grid[row - 1][col] == '' and chess_grid[row - 2][col] == '' and not find_Peice(get_WhitePieces(),chess_grid[row - 1][col - 1]) and find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]):
                    return [(row - 1, col), (row - 2, col), (row - 1, col + 1)]
                elif chess_grid[row - 1][col] == '' and chess_grid[row - 2][col] == '' and not find_Peice(get_WhitePieces(),chess_grid[row - 1][col - 1]) and not find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]):
                    return [(row - 1, col), (row - 2, col)]
                elif chess_grid[row-1][col]=='' and chess_grid[row - 2][col] != '' and  find_Peice(get_WhitePieces(),chess_grid[row - 1][col - 1]) and not find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]):
                    return [(row-1,col),(row-1,col-1)]
                elif chess_grid[row-1][col]=='' and chess_grid[row - 2][col] != '' and not find_Peice(get_WhitePieces(),chess_grid[row - 1][col - 1]) and find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]):
                    return [(row-1,col),(row-1,col+1)]
                elif chess_grid[row-1][col]=='' and chess_grid[row - 2][col] != '' and not find_Peice(get_WhitePieces(),chess_grid[row - 1][col - 1]) and not find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]):
                    return [(row-1,col)]
                else:
                    return []
            elif piece == 'BP' and row == 6 and col == 0:
                if chess_grid[row -1][col] == '' and chess_grid[row -2][col] == '' and find_Peice(get_WhitePieces(),chess_grid[row -1][col + 1]):
                    return [(row -1, col), (row -2, col), (row -1, col + 1)]
                elif chess_grid[row -1][col] == '' and chess_grid[row -2][col] == '' and not find_Peice(get_WhitePieces(),chess_grid[row -1][col + 1]):
                    return [(row -1, col), (row -2, col)]

            elif piece == 'BP' and row == 6 and col == 7:
                if chess_grid[row -1][col] == '' and chess_grid[row -2][col] == '' and find_Peice(get_WhitePieces(),chess_grid[row -1][col - 1]):
                    return [(row -1, col), (row -2, col), (row-1, col - 1)]
                elif chess_grid[row -1][col] == '' and chess_grid[row -2][col] == '' and not find_Peice(get_WhitePieces(),chess_grid[row -1][col - 1]):
                    return [(row -1, col), (row -2, col)]

            elif piece=='BP' and row!=6:
                if col+1<=7 and col-1>=0:
                    if find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]) and find_Peice(get_WhitePieces(),chess_grid[row-1][col-1]) and chess_grid[row-1][col]=='':
                        return [(row-1,col+1),(row-1,col-1),(row-1,col)]
                    elif find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]) and find_Peice(get_WhitePieces(),chess_grid[row-1][col-1]) and chess_grid[row-1][col]!='':
                        return [(row-1,col+1),(row-1,col-1)]

                    elif find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]) and not find_Peice(get_WhitePieces(),chess_grid[row-1][col-1]) and chess_grid[row-1][col]=='':
                        return [(row-1,col+1),(row-1,col)]
                    elif find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]) and not find_Peice(get_WhitePieces(),chess_grid[row-1][col-1]) and chess_grid[row-1][col]!='':
                        return [(row-1,col+1)]

                    if not find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]) and find_Peice(get_WhitePieces(),chess_grid[row-1][col-1]) and chess_grid[row-1][col]=='':
                        return [(row-1,col-1),(row-1,col)]
                    elif not find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]) and find_Peice(get_WhitePieces(),chess_grid[row-1][col-1]) and chess_grid[row-1][col]!='':
                        return [(row-1,col-1)]
                    elif chess_grid[row-1][col]=='' and not find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]) and not find_Peice(get_WhitePieces(),chess_grid[row-1][col-1]):
                        return [(row-1,col)]
                    else:
                        return []
                elif col==0:
                    if find_Peice(get_WhitePieces(),chess_grid[row-1][col+1])  and chess_grid[row-1][col]=='':
                        return [(row-1,col+1),(row-1,col)]
                    elif find_Peice(get_WhitePieces(),chess_grid[row-1][col+1])  and chess_grid[row-1][col]!='':
                        return [(row-1,col+1)]
                    elif not find_Peice(get_WhitePieces(),chess_grid[row-1][col+1]) and chess_grid[row-1][col]=='':
                        return [(row-1,col)]
                    else:
                        return []
                elif col==7:
                    if find_Peice(get_WhitePieces(),chess_grid[row-1][col-1])  and chess_grid[row-1][col]=='':
                        return [(row-1,col-1),(row-1,col)]
                    elif find_Peice(get_WhitePieces(),chess_grid[row-1][col-1])  and chess_grid[row-1][col]!='':
                        return [(row-1,col-1)]
                    elif not find_Peice(get_WhitePieces(),chess_grid[row-1][col-1]) and chess_grid[row-1][col]=='':
                        return [(row-1,col)]
                    else:
                        return []

                


        if row+1<=7:
            if piece == 'wP' and row == 1 and col>0 and col<7:
                if chess_grid[row +1][col] == '' and chess_grid[row +2][col] == '' and find_Peice(get_BlackPieces(),chess_grid[row +1][col - 1]) and find_Peice(get_BlackPieces(), chess_grid[row +1][col + 1]):
                    return [(row +1, col), (row +2, col), (row +1, col + 1), (row +1, col - 1)]
                elif chess_grid[row +1][col] == '' and chess_grid[row +2][col] == '' and find_Peice(get_BlackPieces(),chess_grid[row +1][col - 1]) and not find_Peice(get_BlackPieces(), chess_grid[row +1][col + 1]):
                    return [(row +1, col), (row +2, col), (row +1, col - 1)]
                elif chess_grid[row +1][col] == '' and chess_grid[row +2][col] == '' and not find_Peice(get_BlackPieces(), chess_grid[row +1][col - 1]) and find_Peice(get_BlackPieces(),chess_grid[row +1][col + 1]):
                    return [(row +1, col), (row +2, col), (row +1, col + 1)]
                elif chess_grid[row +1][col] == '' and chess_grid[row +2][col] == '' and not find_Peice(get_BlackPieces(), chess_grid[row +1][col - 1]) and not find_Peice(get_BlackPieces(),chess_grid[row +1][col + 1]):
                    return [(row +1, col), (row +2, col)]
                elif chess_grid[row +1][col] == '' and chess_grid[row +2][col] != '' and find_Peice(get_BlackPieces(),chess_grid[row +1][col - 1]) and not find_Peice(get_BlackPieces(), chess_grid[row +1][col + 1]):
                    return [(row +1, col), (row +1, col - 1)]
                elif chess_grid[row - 1][col] == '' and chess_grid[row +2][col] != '' and not find_Peice(get_BlackPieces(), chess_grid[row +1][col - 1]) and find_Peice(get_BlackPieces(),chess_grid[row +1][col + 1]):
                    return [(row +1, col), (row +1, col + 1)]
                elif chess_grid[row + 1][col] == '' and chess_grid[row +2][col] != '' and not find_Peice(get_BlackPieces(), chess_grid[row +1][col - 1]) and not find_Peice(get_BlackPieces(),chess_grid[row +1][col + 1]):
                    return [(row +1, col)]
                else:
                    return []
            elif piece == 'wP' and row == 1 and col == 0:
                if chess_grid[row +1][col] == '' and chess_grid[row +2][col] == '' and find_Peice(get_BlackPieces(),chess_grid[row +1][col + 1]):
                    return [(row +1, col), (row +2, col), (row +1, col + 1)]
                elif chess_grid[row +1][col] == '' and chess_grid[row +2][col] == '' and not find_Peice(get_BlackPieces(),chess_grid[row +1][col + 1]):
                    return [(row +1, col), (row +2, col)]

            elif piece == 'wP' and row == 1 and col == 7:
                if chess_grid[row +1][col] == '' and chess_grid[row +2][col] == '' and find_Peice(get_BlackPieces(),chess_grid[row +1][col - 1]):
                    return [(row +1, col), (row +2, col), (row +1, col - 1)]
                elif chess_grid[row +1][col] == '' and chess_grid[row +2][col] == '' and not find_Peice(get_BlackPieces(),chess_grid[row +1][col - 1]):
                    return [(row +1, col), (row +2, col)]

            elif piece=='wP' and row!=1:
                if col+1<=7 and col-1>=0:
                    if find_Peice(get_BlackPieces(),chess_grid[row+1][col+1]) and find_Peice(get_BlackPieces(),chess_grid[row+1][col-1]) and chess_grid[row+1][col]=='':
                        return [(row+1,col+1),(row+1,col-1),(row+1,col)]

                #Start here
                    elif find_Peice(get_BlackPieces(),chess_grid[row+1][col+1]) and find_Peice(get_BlackPieces(),chess_grid[row+1][col-1]) and chess_grid[row+1][col]!='':
                        return [(row+1,col+1),(row+1,col-1)]

                    elif find_Peice(get_BlackPieces(),chess_grid[row+1][col+1]) and not find_Peice(get_BlackPieces(),chess_grid[row+1][col-1]) and chess_grid[row+1][col]=='':
                        return [(row+1,col+1),(row+1,col)]
                    elif find_Peice(get_BlackPieces(),chess_grid[row+1][col+1]) and not find_Peice(get_BlackPieces(),chess_grid[row+1][col-1]) and chess_grid[row+1][col]!='':
                        return [(row+1,col+1)]

                    elif not find_Peice(get_BlackPieces(),chess_grid[row+1][col+1]) and find_Peice(get_BlackPieces(),chess_grid[row+1][col-1]) and chess_grid[row+1][col]=='':
                        return [(row+1,col-1),(row+1,col)]
                    elif not find_Peice(get_BlackPieces(),chess_grid[row+1][col+1]) and find_Peice(get_BlackPieces(),chess_grid[row+1][col-1]) and chess_grid[row+1][col]!='':
                        return [(row+1,col-1)]
                    elif chess_grid[row+1][col]=='' and not find_Peice(get_BlackPieces(),chess_grid[row+1][col+1]) and not find_Peice(get_BlackPieces(),chess_grid[row+1][col-1]):
                        return [(row+1,col)]
                    else:
                        return []
                elif col==0:
                    if find_Peice(get_BlackPieces(),chess_grid[row+1][col+1])  and chess_grid[row+1][col]=='':
                        return [(row+1,col+1),(row+1,col)]
                    elif find_Peice(get_BlackPieces(),chess_grid[row+1][col+1])  and chess_grid[row+1][col]!='':
                        return [(row+1,col+1)]
                    elif not find_Peice(get_BlackPieces(),chess_grid[row+1][col+1]) and chess_grid[row+1][col]=='':
                        return [(row+1,col)]
                    else:
                        return []
                elif col==7:
                    if find_Peice(get_BlackPieces(),chess_grid[row+1][col-1])  and chess_grid[row+1][col]=='':
                        return [(row+1,col-1),(row+1,col)]
                    elif find_Peice(get_BlackPieces(),chess_grid[row+1][col-1])  and chess_grid[row+1][col]!='':
                        return [(row+1,col-1)]
                    elif not find_Peice(get_BlackPieces(),chess_grid[row+1][col-1]) and chess_grid[row+1][col]=='':
                        return [(row+1,col)]
                    else:
                        return []
    return []