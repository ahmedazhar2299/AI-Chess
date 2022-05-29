import copy
import math
from Pawn import *
from Knight import *
from Rook import *
from Bishop import*
from Queen import*
from King import*
from Board import Chess_Board
import pygame




class Chess_Game_Multiplayer:
    def __init__(self,screen):
        self.screen = screen
        self.Black_Castling_Right = False
        self.Black_Castling_Left = False
        self.White_Castling_Right = False
        self.White_Castling_Left = False
        self.Black_Turn_Flag = False
        self.White_Turn_Flag = True
        self.Taking_Turn  = True

    def Mark_Possible_Moves(self,grid,chess_Moves):
        for moves in chess_Moves:
            x,y = moves
            grid[x][y]  = "x"
    def Remove_Moves(self,grid):
        for i in range(8):
            for j in range(8):
                if grid[i][j] == "x":
                    grid[i][j] = ""

    def Complete_CheckMate(self,grid,piece):
        flag = False
        if piece == 'wK':
            white_Pieces = get_WhitePieces()
            white_Pieces.remove('wk')
            for p in white_Pieces:
                r,c = Find_Postion(grid,'wK')
                flag = CheckMate(grid,'wK',r,c,get_BlackPieces)


    def Print_Moves(self,chess_Board,grid,cordX,cordY,color,func):
        Total_Moves = self.check_total_Moves(grid, cordX, cordY, func)
        for move in Total_Moves:
            chess_Board.drawCircle(self.screen, (move[1] * 100) + 45 + 50, (move[0] * 100) + 45 + 50, color, 10)
        return Total_Moves

    def check_total_Moves(self, grid, cordX, cordY, func):
        Total_Moves = list()
        flag = False
        if self.White_Turn_Flag:
            r, c = Find_Postion(grid, 'wK')
            flag = CheckMate(grid, 'wK', r, c, get_BlackPieces)
        elif self.Black_Turn_Flag:
            r, c = Find_Postion(grid, 'BK')
            flag = CheckMate(grid, 'BK', r, c, get_WhitePieces)
        if not flag:
            Total_Moves = func(grid, grid[cordX][cordY], cordX, cordY)
        return Total_Moves
    def Game_Termination(self,grid):
        if self.White_Turn_Flag and self.Taking_Turn:
            for i in range(8):
                for j in range(8):
                    if grid[i][j]=='wP':
                       moves =  self.check_total_Moves(grid, i, j, move_Pawn)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='wR':
                       moves =  self.check_total_Moves(grid, i, j, move_Rook)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='wK':
                       moves =  move_King(grid,'wK' ,i, j)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='wB':
                       moves =  self.check_total_Moves(grid, i, j, move_Bishop)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='wN':
                       moves =  self.check_total_Moves(grid, i, j, move_Knight)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='wQ':
                       moves =  self.check_total_Moves(grid, i, j, move_Queen)
                       if len(moves)>0:
                           return False
            return True
        if self.Black_Turn_Flag and self.Taking_Turn:
            for i in range(8):
                for j in range(8):
                    if grid[i][j]=='BP':
                       moves =  self.check_total_Moves(grid, i, j, move_Pawn)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='BR':
                       moves =  self.check_total_Moves(grid, i, j, move_Rook)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='BK':
                       moves =  move_King(grid,'BK' ,i, j)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='BB':
                       moves =  self.check_total_Moves(grid, i, j, move_Bishop)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='BN':
                       moves =  self.check_total_Moves(grid, i, j, move_Knight)
                       if len(moves)>0:
                           return False
                    if grid[i][j]=='BQ':
                       moves =  self.check_total_Moves(grid, i, j, move_Queen)
                       if len(moves)>0:
                           return False
            return True
        return False






    def Print_King_Castling_Moves(self,chess_Board,grid,cordX,cordY,color,func):
        Total_Moves = func(grid, grid[cordX][cordY], cordX, cordY)
        flag = self.King_Castling_Move(grid, cordX, cordY, Total_Moves)
        for move in Total_Moves:
            chess_Board.drawCircle(self.screen, (move[1] * 100) + 45 + 50, (move[0] * 100) + 45 + 50, color, 10)
        return flag,Total_Moves
    def Remove_Pawn_Moves(self,chess_Board,Pawn_Moves):
        for move in Pawn_Moves:
            x,y = move
            if (x+y)%2==0:
                chess_Board.drawCircle(self.screen, (move[1] * 100) + 45 + 50, (move[0] * 100) + 45 + 50, "#FDF6EC", 10)
            else:
                chess_Board.drawCircle(self.screen, (move[1] * 100) + 45 + 50, (move[0] * 100) + 45 + 50, "#C69B7B", 10)

    def King_Castling_Move(self,chess_grid, x, y,moves):
        flag = False
        if chess_grid[x][y] == 'wK':
            if y-3==0 and chess_grid[x][y-1]=="" and chess_grid[x][y-2]=="" and chess_grid[x][y-3]=="wR" and not self.White_Castling_Left:
                moves.append((x,y-2))
                flag = True
            elif y+3==7 and chess_grid[x][y+1]=="" and chess_grid[x][y+2]=="" and chess_grid[x][y+3]=="wR" and not self.White_Castling_Right:
                moves.append((x,y+2))
                flag = True
        if chess_grid[x][y] == 'BK':
            if y-3==0 and chess_grid[x][y-1]=="" and chess_grid[x][y-2]=="" and chess_grid[x][y-3]=="BR" and not self.Black_Castling_Left:
                moves.append((x,y-2))
                flag = True
            elif y+3==7 and chess_grid[x][y+1]=="" and chess_grid[x][y+2]=="" and chess_grid[x][y+3]=="BR" and not self.Black_Castling_Right:
                moves.append((x,y+2))
                flag = True
        return flag

    def Pawn_Promotion_Piece(self,chess_board,grid,x,y):
        chess_board.drawRectangle(self.screen, 150, 250, 150 + (3 * 125) + 25, 250, "#614124")
        chess_board.drawRectangle(self.screen, 160, 260, 125, 230, "#EDE6DB")
        chess_board.Place_Piece(self.screen, "images\Bishop_PP.png", 160 + 30, 260 + 30)
        chess_board.drawRectangle(self.screen, 160 + 125 + 10, 260, 125, 230, "#EDE6DB")
        chess_board.Place_Piece(self.screen, "images\Rook_PP.png", (160 + 125 + 20) + 25, 275)
        chess_board.drawRectangle(self.screen, 160 + (2 * 125) + 20, 260, 125, 230, "#EDE6DB")
        chess_board.Place_Piece(self.screen, "images\Knight_PP.png", (160 + (2 * 125) + 20) + 50, 325)
        chess_board.drawRectangle(self.screen, 160 + (3 * 125) + 30, 260, 125, 230, "#EDE6DB")
        chess_board.Place_Piece(self.screen, "images\Queen_PP.png", (160 + (3 * 125) + 30) + 20, 325)
        running = True
        while running:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_Clicked = pygame.mouse.get_pressed()

                    if (button_Clicked[0]):
                        mouseclick_Cordinates = list(pygame.mouse.get_pos())
                        if (mouseclick_Cordinates[0] >= 205 and mouseclick_Cordinates[0] <= 330) and (mouseclick_Cordinates[1] >= 305 and mouseclick_Cordinates[1] <= 535):
                            if self.White_Turn_Flag:
                                grid[x][y]= 'wB'
                            else:
                                grid[x][y] = 'BB'
                            return
                        if (mouseclick_Cordinates[0] >= 340 and mouseclick_Cordinates[0] <= 465) and (mouseclick_Cordinates[1] >= 305 and mouseclick_Cordinates[1] <= 535):
                            if self.White_Turn_Flag:
                                grid[x][y]= 'wR'
                            else:
                                grid[x][y] = 'BR'
                            return
                        if (mouseclick_Cordinates[0] >= 475 and mouseclick_Cordinates[0] <= 600) and (mouseclick_Cordinates[1] >= 305 and mouseclick_Cordinates[1] <= 535):
                            if self.White_Turn_Flag:
                                grid[x][y]= 'wN'
                            else:
                                grid[x][y] = 'BN'
                            return
                        if (mouseclick_Cordinates[0] >= 610 and mouseclick_Cordinates[0] <= 735) and (mouseclick_Cordinates[1] >= 305 and mouseclick_Cordinates[1] <= 535):
                            if self.White_Turn_Flag:
                                grid[x][y] = 'wQ'
                            else:
                                grid[x][y] = 'BQ'
                            return


    def Play_Multiplayer(self):
        chess_Board = Chess_Board()
        chess_Board.new_Chess_Board(self.screen)
        running = True
        Previous_Selected_Piece = "wP"
        CordX_Previous_Piece = 0
        CordY_Previous_Piece = 0
        grid = chess_Board.get_board()
        Black_previous_Checkmate_Print_X = 0
        Black_previous_Checkmate_Print_Y = 0
        Black_previous_Checkmate_print_Flag = False
        White_previous_Checkmate_Print_X = 0
        White_previous_Checkmate_Print_Y = 0
        White_previous_Checkmate_print_Flag = False

        chess_Board.Display_Text_on_Board(self.screen, "PLAYER TURN : ",300,860,25,'#FFE69A')
        Previous_State = copy.deepcopy(grid)
        moves = list()
        King_Castling_Flag = False
        Winner_Print_Flag = False
        while running:
            pygame.display.update()
            for event in pygame.event.get():
                if not self.Game_Termination(grid):
                    if self.White_Turn_Flag:
                        chess_Board.Place_Piece(self.screen, "images\C_White.png", 500, 845)
                        r,c = Find_Postion(grid,'wK')
                        if  CheckMate(grid,'wK',r,c,get_BlackPieces):
                            y =(r*100)
                            x =  (c*100)
                            chess_Board.drawRectangle(self.screen,x,y,100,100,'#B22727')
                            chess_Board.Place_Piece(self.screen, "images\wK.png", x + 60, y + 60)
                            White_previous_Checkmate_Print_X = r
                            White_previous_Checkmate_Print_Y = c
                            White_previous_Checkmate_print_Flag = True
                        else:
                            if White_previous_Checkmate_print_Flag:
                                y = (White_previous_Checkmate_Print_X * 100)
                                x = (White_previous_Checkmate_Print_Y * 100)
                                if (White_previous_Checkmate_Print_X+White_previous_Checkmate_Print_Y)%2==0:
                                    chess_Board.drawRectangle(self.screen, x, y, 100, 100, '#FDF6EC')
                                else:
                                    chess_Board.drawRectangle(self.screen, x, y, 100, 100, '#C69B7B')
                                #chess_Board.Place_Piece(self.screen, "images\wK.png", x + 60, y + 60)
                                White_previous_Checkmate_print_Flag = False

                    elif self.Black_Turn_Flag:
                        chess_Board.Place_Piece(self.screen, "images\C_Black.png", 500, 845)
                        r, c = Find_Postion(grid, 'BK')
                        if CheckMate(grid,'BK',r,c,get_WhitePieces):
                            y =(r*100)
                            x =  (c*100)
                            chess_Board.drawRectangle(self.screen,x,y,100,100,'#B22727')
                            chess_Board.Place_Piece(self.screen, "images\BK.png", x + 60, y + 60)
                            Black_previous_Checkmate_Print_X = r
                            Black_previous_Checkmate_Print_Y = c
                            Black_previous_Checkmate_print_Flag = True
                        else:
                            if Black_previous_Checkmate_print_Flag:
                                y = (Black_previous_Checkmate_Print_X * 100)
                                x = (Black_previous_Checkmate_Print_Y * 100)
                                if (Black_previous_Checkmate_Print_X+Black_previous_Checkmate_Print_Y)%2==0:
                                    chess_Board.drawRectangle(self.screen, x, y, 100, 100, '#FDF6EC')
                                else:
                                    chess_Board.drawRectangle(self.screen, x, y, 100, 100, '#C69B7B')
                                #chess_Board.Place_Piece(self.screen, "images\BK.png", x + 60, y + 60)
                                Black_previous_Checkmate_print_Flag = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button_Clicked = pygame.mouse.get_pressed()
                        if (button_Clicked[0]):
                            mouseclick_Cordinates = list(pygame.mouse.get_pos())
                            cordX = math.floor((mouseclick_Cordinates[1] - (45)) / 100)
                            cordY = math.floor((mouseclick_Cordinates[0] - (45)) / 100)
                            if (mouseclick_Cordinates[0] < 845 and mouseclick_Cordinates[1] < 845 and cordY >= 0 and cordX >= 0):
                                if (self.White_Turn_Flag and (find_Peice(get_WhitePieces(),grid[cordX][cordY]))) or (self.Black_Turn_Flag and (find_Peice(get_BlackPieces(),grid[cordX][cordY]))):
                                    if (grid[cordX][cordY]=='BP' or grid[cordX][cordY]=='wP') and (cordX!=CordX_Previous_Piece or cordY!=CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.update_UI_chess_board(self.screen,moves,(cordX,cordY))
                                        moves =  self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A",move_Pawn)
                                        if len(moves)>0:
                                            self.Taking_Turn = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY

                                        self.Mark_Possible_Moves(grid,moves)
                                        chess_Board.update_board(grid)
                                    elif  (grid[cordX][cordY]=='BN' or grid[cordX][cordY]=='wN') and (cordX!=CordX_Previous_Piece or cordY!=CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.update_UI_chess_board(self.screen,moves,(cordX,cordY))
                                        moves =  self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A",move_Knight)
                                        if len(moves)>0:
                                            self.Taking_Turn = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY

                                        self.Mark_Possible_Moves(grid,moves)
                                        chess_Board.update_board(grid)
                                    elif (grid[cordX][cordY] == 'BR' or grid[cordX][cordY] == 'wR') and (
                                            cordX != CordX_Previous_Piece or cordY != CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.update_UI_chess_board(self.screen,moves,(cordX,cordY))
                                        moves = self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A", move_Rook)
                                        if len(moves)>0:
                                            self.Taking_Turn = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY
                                        self.Mark_Possible_Moves(grid, moves)
                                        chess_Board.update_board(grid)
                                    elif (grid[cordX][cordY] == 'BB' or grid[cordX][cordY] == 'wB') and (
                                            cordX != CordX_Previous_Piece or cordY != CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.update_UI_chess_board(self.screen,moves,(cordX,cordY))
                                        moves = self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A", move_Bishop)
                                        if len(moves)>0:
                                            self.Taking_Turn = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY
                                        self.Mark_Possible_Moves(grid, moves)
                                        chess_Board.update_board(grid)
                                    elif (grid[cordX][cordY] == 'BQ' or grid[cordX][cordY] == 'wQ') and (cordX != CordX_Previous_Piece or cordY != CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.update_UI_chess_board(self.screen,moves,(cordX,cordY))
                                        moves = self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A", move_Queen)
                                        if len(moves)>0:
                                            self.Taking_Turn = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY

                                        self.Mark_Possible_Moves(grid, moves)
                                        chess_Board.update_board(grid)
                                    elif (grid[cordX][cordY] == 'BK' or grid[cordX][cordY] == 'wK') and (cordX != CordX_Previous_Piece or cordY != CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.update_UI_chess_board(self.screen,moves,(cordX,cordY))
                                        King_Castling_Flag, moves = self.Print_King_Castling_Moves(chess_Board, grid, cordX,cordY, "#A64B2A",move_King)
                                        if len(moves)>0:
                                            self.Taking_Turn = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY
                                        self.Mark_Possible_Moves(grid, moves)
                                        chess_Board.update_board(grid)

                                if  (self.White_Turn_Flag and find_Peice(get_WhitePieces(),Previous_Selected_Piece)) or (self.Black_Turn_Flag and find_Peice(get_BlackPieces(),Previous_Selected_Piece)):
                                    if grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='wP' or Previous_Selected_Piece=="BP"):
                                        grid[cordX][cordY] = Previous_Selected_Piece
                                        grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        moves.remove((cordX, cordY))
                                        self.Remove_Moves(grid)
                                        Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        Previous_State[cordX][cordY] = Previous_Selected_Piece
                                        grid = copy.deepcopy(Previous_State)
                                        Previous_Selected_Piece = ""
                                        if self.White_Turn_Flag and cordX==7:
                                            self.Pawn_Promotion_Piece(chess_Board,grid,cordX,cordY)
                                            Previous_State = copy.deepcopy(grid)
                                            chess_Board.update_board(grid)
                                            chess_Board.new_Chess_Board(self.screen)
                                        elif self.Black_Turn_Flag and cordX==0:
                                            self.Pawn_Promotion_Piece(chess_Board,grid,cordX,cordY)
                                            Previous_State = copy.deepcopy(grid)
                                            chess_Board.update_board(grid)
                                            chess_Board.new_Chess_Board(self.screen)
                                        chess_Board.update_board(grid)
                                        moves.append((CordX_Previous_Piece, CordY_Previous_Piece))
                                        chess_Board.update_UI_chess_board(self.screen, moves, (cordX, cordY))
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True
                                        self.Taking_Turn = True

                                    elif grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='BN' or Previous_Selected_Piece=="wN"):
                                        grid[cordX][cordY] = Previous_Selected_Piece
                                        grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        moves.remove((cordX, cordY))
                                        self.Remove_Moves(grid)
                                        Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        Previous_State[cordX][cordY] = Previous_Selected_Piece
                                        grid = copy.deepcopy(Previous_State)
                                        Previous_Selected_Piece = ""
                                        chess_Board.update_board(grid)
                                        moves.append((CordX_Previous_Piece, CordY_Previous_Piece))
                                        chess_Board.update_UI_chess_board(self.screen, moves, (cordX, cordY))
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True
                                        self.Taking_Turn = True

                                    elif grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='BR' or Previous_Selected_Piece=="wR"):
                                        grid[cordX][cordY] = Previous_Selected_Piece
                                        grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        moves.remove((cordX, cordY))
                                        self.Remove_Moves(grid)
                                        Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        Previous_State[cordX][cordY] = Previous_Selected_Piece
                                        grid = copy.deepcopy(Previous_State)
                                        Previous_Selected_Piece = ""
                                        chess_Board.update_board(grid)
                                        moves.append((CordX_Previous_Piece, CordY_Previous_Piece))
                                        chess_Board.update_UI_chess_board(self.screen, moves, (cordX, cordY))
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True
                                        self.Taking_Turn = True


                                    elif grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='BB' or Previous_Selected_Piece=="wB"):
                                        grid[cordX][cordY] = Previous_Selected_Piece
                                        grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        moves.remove((cordX, cordY))
                                        self.Remove_Moves(grid)
                                        Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        Previous_State[cordX][cordY] = Previous_Selected_Piece
                                        grid = copy.deepcopy(Previous_State)
                                        Previous_Selected_Piece = ""
                                        chess_Board.update_board(grid)
                                        moves.append((CordX_Previous_Piece, CordY_Previous_Piece))
                                        chess_Board.update_UI_chess_board(self.screen, moves, (cordX, cordY))
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True
                                        self.Taking_Turn = True



                                    elif grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='BQ' or Previous_Selected_Piece=="wQ"):

                                        grid[cordX][cordY] = Previous_Selected_Piece
                                        grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        moves.remove((cordX, cordY))
                                        self.Remove_Moves(grid)
                                        Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        Previous_State[cordX][cordY] = Previous_Selected_Piece
                                        grid = copy.deepcopy(Previous_State)
                                        Previous_Selected_Piece = ""
                                        chess_Board.update_board(grid)
                                        moves.append((CordX_Previous_Piece, CordY_Previous_Piece))
                                        chess_Board.update_UI_chess_board(self.screen, moves, (cordX, cordY))
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True
                                        self.Taking_Turn = True



                                    elif grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='BK' or Previous_Selected_Piece=="wK"):
                                        if not King_Castling_Flag:
                                            grid[cordX][cordY] = Previous_Selected_Piece
                                            grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                            moves.remove((cordX, cordY))
                                            self.Remove_Moves(grid)
                                            Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                            Previous_State[cordX][cordY] = Previous_Selected_Piece
                                            grid = copy.deepcopy(Previous_State)
                                            Previous_Selected_Piece = ""
                                            chess_Board.update_board(grid)
                                            moves.append((CordX_Previous_Piece, CordY_Previous_Piece))
                                            chess_Board.update_UI_chess_board(self.screen, moves, (cordX, cordY))
                                            CordX_Previous_Piece = None
                                            CordY_Previous_Piece = None
                                            if self.White_Turn_Flag:
                                                self.White_Turn_Flag = False
                                                self.Black_Turn_Flag = True
                                            elif self.Black_Turn_Flag:
                                                self.Black_Turn_Flag = False
                                                self.White_Turn_Flag = True
                                            self.Taking_Turn = True
                                        else:
                                            grid[cordX][cordY] = Previous_Selected_Piece
                                            grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                            Previous_State[cordX][cordY] = Previous_Selected_Piece
                                            Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                            if Previous_Selected_Piece=='BK':
                                                if grid[cordX][cordY+1]=='BR' and not self.Black_Castling_Right:
                                                    grid[cordX][cordY + 1] = ''
                                                    grid[CordX_Previous_Piece][CordY_Previous_Piece+1] = 'BR'
                                                    Previous_State[cordX][cordY + 1] = ''
                                                    Previous_State[CordX_Previous_Piece][CordY_Previous_Piece + 1] = 'BR'
                                                    self.Black_Castling_Right = True
                                                    moves.append((cordX, cordY + 1))

                                                elif grid[cordX][cordY-1]=='BR' and not self.Black_Castling_Left:
                                                    grid[cordX][cordY - 1] = ''
                                                    grid[CordX_Previous_Piece][CordY_Previous_Piece-1] = 'BR'
                                                    Previous_State[cordX][cordY - 1] = ''
                                                    Previous_State[CordX_Previous_Piece][CordY_Previous_Piece - 1] = 'BR'
                                                    moves.append((cordX, cordY - 1))
                                                    self.Black_Castling_Left = True

                                            elif Previous_Selected_Piece=='wK':
                                                if grid[cordX][cordY + 1] == 'wR' and not self.White_Castling_Right:
                                                    grid[cordX][cordY + 1] = ''
                                                    grid[CordX_Previous_Piece][CordY_Previous_Piece + 1] = 'wR'
                                                    Previous_State[cordX][cordY + 1] = ''
                                                    Previous_State[cordX][cordY + 1] = 'wR'
                                                    self.White_Castling_Right = True
                                                    moves.append((cordX, cordY + 1))

                                                elif grid[cordX][cordY - 1] == 'wR' and not self.White_Castling_Left:
                                                    grid[cordX][cordY - 1] = ''
                                                    grid[CordX_Previous_Piece][CordY_Previous_Piece - 1] = 'wR'
                                                    Previous_State[cordX][cordY - 1] = ''
                                                    Previous_State[CordX_Previous_Piece][CordY_Previous_Piece - 1] = 'wR'
                                                    self.White_Castling_Left = True
                                                    moves.append((cordX, cordY-1))
                                            moves.remove((cordX, cordY))
                                            self.Remove_Moves(grid)
                                            grid = copy.deepcopy(Previous_State)
                                            Previous_Selected_Piece = ""
                                            chess_Board.update_board(grid)
                                            moves.append((CordX_Previous_Piece, CordY_Previous_Piece))
                                            chess_Board.update_UI_chess_board(self.screen, moves, (cordX, cordY))
                                            CordX_Previous_Piece = None
                                            CordY_Previous_Piece = None
                                            if self.White_Turn_Flag:
                                                self.White_Turn_Flag = False
                                                self.Black_Turn_Flag = True
                                            elif self.Black_Turn_Flag:
                                                self.Black_Turn_Flag = False
                                                self.White_Turn_Flag = True
                                            self.Taking_Turn = True
                else:
                    if self.White_Turn_Flag and not Winner_Print_Flag:
                        chess_Board.Display_Text_on_Board(self.screen, "BLACK WON!",375, 20, 25, '#FFEBC1')
                        Winner_Print_Flag = True
                    elif self.Black_Turn_Flag and not Winner_Print_Flag:
                        chess_Board.Display_Text_on_Board(self.screen, "WHITE WON!", 375, 20, 25, '#FFEBC1')
                        Winner_Print_Flag = True








                if event.type == pygame.QUIT:
                    running = False

