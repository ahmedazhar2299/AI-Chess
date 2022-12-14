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




class Chess_Game:
    def __init__(self,screen):
        self.screen = screen
        self.Black_Castling_Right = False
        self.Black_Castling_Left = False
        self.White_Castling_Right = False
        self.White_Castling_Left = False
        self.Black_Turn_Flag = False
        self.White_Turn_Flag = True

        self.Pawn_Move_Flag = True
        self.King_Move_Flag = True
        self.Queen_Move_Flag = True
        self.Rook_Move_Flag = True
        self.Bishop_Move_Flag = True
        self.Knight_Move_Flag = True

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
                            chess_Board.Place_Piece(self.screen, "images\wK.png", x + 60, y + 60)
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
                            chess_Board.Place_Piece(self.screen, "images\BK.png", x + 60, y + 60)
                            Black_previous_Checkmate_print_Flag = False

                if (self.Pawn_Move_Flag or self.King_Move_Flag or self.Queen_Move_Flag or self.Rook_Move_Flag or self.Bishop_Move_Flag or self.Knight_Move_Flag):
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
                                        chess_Board.new_Chess_Board(self.screen)
                                        moves =  self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A",move_Pawn)
                                        if len(moves)>0:
                                            self.Pawn_Move_Flag = True
                                        else:
                                            self.Pawn_Move_Flag = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY

                                        self.Mark_Possible_Moves(grid,moves)
                                        chess_Board.update_board(grid)
                                    elif  (grid[cordX][cordY]=='BN' or grid[cordX][cordY]=='wN') and (cordX!=CordX_Previous_Piece or cordY!=CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        moves =  self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A",move_Knight)
                                        if len(moves)>0:
                                            self.Knight_Move_Flag = True
                                        else:
                                            self.Knight_Move_Flag = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY

                                        self.Mark_Possible_Moves(grid,moves)
                                        chess_Board.update_board(grid)
                                    elif (grid[cordX][cordY] == 'BR' or grid[cordX][cordY] == 'wR') and (
                                            cordX != CordX_Previous_Piece or cordY != CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        moves = self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A", move_Rook)
                                        if len(moves)>0:
                                            self.Rook_Move_Flag = True
                                        else:
                                            self.Rook_Move_Flag = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY
                                        self.Mark_Possible_Moves(grid, moves)
                                        chess_Board.update_board(grid)
                                    elif (grid[cordX][cordY] == 'BB' or grid[cordX][cordY] == 'wB') and (
                                            cordX != CordX_Previous_Piece or cordY != CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        moves = self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A", move_Bishop)
                                        if len(moves)>0:
                                            self.Bishop_Move_Flag = True
                                        else:
                                            self.Bishop_Move_Flag = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY
                                        self.Mark_Possible_Moves(grid, moves)
                                        chess_Board.update_board(grid)
                                    elif (grid[cordX][cordY] == 'BQ' or grid[cordX][cordY] == 'wQ') and (cordX != CordX_Previous_Piece or cordY != CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        moves = self.Print_Moves(chess_Board, grid, cordX, cordY, "#A64B2A", move_Queen)
                                        if len(moves)>0:
                                            self.Queen_Move_Flag = True
                                        else:
                                            self.Queen_Move_Flag = False
                                        Previous_Selected_Piece = grid[cordX][cordY]
                                        CordX_Previous_Piece = cordX
                                        CordY_Previous_Piece = cordY

                                        self.Mark_Possible_Moves(grid, moves)
                                        chess_Board.update_board(grid)
                                    elif (grid[cordX][cordY] == 'BK' or grid[cordX][cordY] == 'wK') and (cordX != CordX_Previous_Piece or cordY != CordY_Previous_Piece):
                                        grid = copy.deepcopy(Previous_State)
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        King_Castling_Flag, moves = self.Print_King_Castling_Moves(chess_Board, grid, cordX,cordY, "#A64B2A",move_King)
                                        if len(moves)>0:
                                            self.King_Move_Flag = True
                                        else:
                                            self.King_Move_Flag = False
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
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True

                                    elif grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='BN' or Previous_Selected_Piece=="wN"):
                                        grid[cordX][cordY] = Previous_Selected_Piece
                                        grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        moves.remove((cordX, cordY))
                                        self.Remove_Moves(grid)
                                        Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        Previous_State[cordX][cordY] = Previous_Selected_Piece
                                        grid = copy.deepcopy(Previous_State)
                                        Previous_Selected_Piece = ""
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True

                                    elif grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='BR' or Previous_Selected_Piece=="wR"):
                                        grid[cordX][cordY] = Previous_Selected_Piece
                                        grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        moves.remove((cordX, cordY))
                                        self.Remove_Moves(grid)
                                        Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        Previous_State[cordX][cordY] = Previous_Selected_Piece
                                        grid = copy.deepcopy(Previous_State)
                                        Previous_Selected_Piece = ""
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True


                                    elif grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='BB' or Previous_Selected_Piece=="wB"):
                                        grid[cordX][cordY] = Previous_Selected_Piece
                                        grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        moves.remove((cordX, cordY))
                                        self.Remove_Moves(grid)
                                        Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        Previous_State[cordX][cordY] = Previous_Selected_Piece
                                        grid = copy.deepcopy(Previous_State)
                                        Previous_Selected_Piece = ""
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True



                                    elif grid[cordX][cordY]=="x" and (Previous_Selected_Piece=='BQ' or Previous_Selected_Piece=="wQ"):

                                        grid[cordX][cordY] = Previous_Selected_Piece
                                        grid[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        moves.remove((cordX, cordY))
                                        self.Remove_Moves(grid)
                                        Previous_State[CordX_Previous_Piece][CordY_Previous_Piece] = ""
                                        Previous_State[cordX][cordY] = Previous_Selected_Piece
                                        grid = copy.deepcopy(Previous_State)
                                        Previous_Selected_Piece = ""
                                        CordX_Previous_Piece = None
                                        CordY_Previous_Piece = None
                                        chess_Board.update_board(grid)
                                        chess_Board.new_Chess_Board(self.screen)
                                        if self.White_Turn_Flag:
                                            self.White_Turn_Flag = False
                                            self.Black_Turn_Flag = True
                                        elif self.Black_Turn_Flag:
                                            self.Black_Turn_Flag = False
                                            self.White_Turn_Flag = True



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
                                            CordX_Previous_Piece = None
                                            CordY_Previous_Piece = None
                                            chess_Board.update_board(grid)
                                            chess_Board.new_Chess_Board(self.screen)
                                            if self.White_Turn_Flag:
                                                self.White_Turn_Flag = False
                                                self.Black_Turn_Flag = True
                                            elif self.Black_Turn_Flag:
                                                self.Black_Turn_Flag = False
                                                self.White_Turn_Flag = True
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
                                                elif grid[cordX][cordY-1]=='BR' and not self.Black_Castling_Left:
                                                    grid[cordX][cordY - 1] = ''
                                                    grid[CordX_Previous_Piece][CordY_Previous_Piece-1] = 'BR'
                                                    Previous_State[cordX][cordY - 1] = ''
                                                    Previous_State[CordX_Previous_Piece][CordY_Previous_Piece - 1] = 'BR'
                                                    self.Black_Castling_Left = True
                                            elif Previous_Selected_Piece=='wK':
                                                if grid[cordX][cordY + 1] == 'wR' and not self.White_Castling_Right:
                                                    grid[cordX][cordY + 1] = ''
                                                    grid[CordX_Previous_Piece][CordY_Previous_Piece + 1] = 'wR'
                                                    Previous_State[cordX][cordY + 1] = ''
                                                    Previous_State[CordX_Previous_Piece][CordY_Previous_Piece + 1] = 'wR'
                                                    self.White_Castling_Right = True
                                                elif grid[cordX][cordY - 1] == 'wR' and not self.White_Castling_Left:
                                                    grid[cordX][cordY - 1] = ''
                                                    grid[CordX_Previous_Piece][CordY_Previous_Piece - 1] = 'wR'
                                                    Previous_State[cordX][cordY - 1] = ''
                                                    Previous_State[CordX_Previous_Piece][CordY_Previous_Piece - 1] = 'wR'
                                                    self.White_Castling_Left = True
                                            moves.remove((cordX, cordY))
                                            self.Remove_Moves(grid)
                                            grid = copy.deepcopy(Previous_State)
                                            Previous_Selected_Piece = ""
                                            CordX_Previous_Piece = None
                                            CordY_Previous_Piece = None
                                            chess_Board.update_board(grid)
                                            chess_Board.new_Chess_Board(self.screen)
                                            if self.White_Turn_Flag:
                                                self.White_Turn_Flag = False
                                                self.Black_Turn_Flag = True
                                            elif self.Black_Turn_Flag:
                                                self.Black_Turn_Flag = False
                                                self.White_Turn_Flag = True
                else:
                    if self.White_Turn_Flag and not Winner_Print_Flag:
                        chess_Board.Display_Text_on_Board(self.screen, "BLACK WON!",375, 20, 25, '#FFEBC1')
                        Winner_Print_Flag = True
                    elif self.Black_Turn_Flag and not Winner_Print_Flag:
                        chess_Board.Display_Text_on_Board(self.screen, "WHITE WON!", 375, 20, 25, '#FFEBC1')
                        Winner_Print_Flag = True








                if event.type == pygame.QUIT:
                    running = False

