import copy

import pygame

class Chess_Board:
    def __init__(self):
        self.Pos_Array = self.Chess_InitialPosition()

    def drawRectangle(self,screen, cordx1, cordy1, cordx2, cordy2, box_color):  # A function to draw rectangle
        pygame.draw.rect(screen, box_color, (cordx1 + 45, cordy1 + 45, cordx2, cordy2))  # box
        pygame.display.update()
    def drawgrid(self,board):
        chess_icon = pygame.image.load("images\icon_chess.png")
        pygame.display.set_icon(chess_icon)
        x = 0
        y = 0
        grid_dimension = 8 #chess board has size of 8x8
        Alt_rect_flag  = False
        for i in range(grid_dimension):
            x = 0
            for j in range(grid_dimension):
                if Alt_rect_flag==False:
                    self.drawRectangle(board, x, y, 100, 100, "#FDF6EC")
                else:
                    self.drawRectangle(board, x, y, 100, 100, "#C69B7B")
                x += 100
                if Alt_rect_flag == False:
                    Alt_rect_flag=True
                else:
                    Alt_rect_flag=False
            if Alt_rect_flag == False:
                Alt_rect_flag = True
            else:
                Alt_rect_flag = False
            y += 100

    def Display_Text_on_Board(self,screen, string, coordx, coordy, fontSize, color):  # Prints Text on Screen
        text_font = pygame.freetype.Font('arial.ttf', fontSize)
        text_surface, rect = text_font.render(string, color)
        screen.blit(text_surface, (coordx, coordy))

    def Chess_InitialPosition(self):
        Positions = list()
        Row1 = ['wR','wN','wB','wQ','wK','wB','wN','wR']
        Row2 = ['wP','wP','wP','wP','wP','wP','wP','wP']
        Positions.append(Row1)
        Positions.append(Row2)
        for i in range(4):
            Positions.append(['','','','','','','',''])
        Row7 = ['BP','BP','BP','BP','BP','BP','BP','BP']
        Row8 = ['BR','BN','BB','BQ','BK','BB','BN','BR']
        Positions.append(Row7)
        Positions.append(Row8)
        return Positions

    def drawCircle(self,board, cordx, cordy, color, radus):  # Draws a circle on Screen
        pygame.draw.circle(board, color, [cordx, cordy], radus)
        pygame.display.update()

    def Place_Piece(self,board,imagePath,x,y):      #Uses image from provided image path and places it on x,y coord on board
        pieceImage = pygame.image.load(imagePath)
        board.blit(pieceImage,(x,y))
        pygame.display.flip()
    def Position_Pieces(self,board,Pos_Array):
        grid_dimension = 8
        x = 0
        y = 0
        for i in range(grid_dimension):
            x = 0
            for j in range(grid_dimension):
            #White Pieces
                if Pos_Array[i][j]=='wR':
                    self.Place_Piece(board,"images\wR.png",x+60,y+60)
                if Pos_Array[i][j]=='wN':
                    self.Place_Piece(board,"images\wN.png",x+60,y+60)
                if Pos_Array[i][j]=='wB':
                    self.Place_Piece(board,"images\wB.png",x+60,y+60)
                if Pos_Array[i][j]=='wQ':
                    self.Place_Piece(board,"images\wQ.png",x+60,y+60)
                if Pos_Array[i][j]=='wK':
                    self.Place_Piece(board,"images\wK.png",x+60,y+60)
                if Pos_Array[i][j]=='wP':
                    self.Place_Piece(board, "images\wP.png", x + 60, y + 60)
            #Black Pieces
                if Pos_Array[i][j]=='BR':
                    self.Place_Piece(board,"images\BR.png",x+60,y+60)
                if Pos_Array[i][j]== 'BN':
                    self.Place_Piece(board,"images\BN.png",x+60,y+60)
                if Pos_Array[i][j]=='BB':
                    self.Place_Piece(board,"images\BB.png",x+60,y+60)
                if Pos_Array[i][j]=='BQ':
                    self.Place_Piece(board,"images\BQ.png",x+60,y+60)
                if Pos_Array[i][j]=='BK':
                    self.Place_Piece(board,"images\BK.png",x+60,y+60)
                if Pos_Array[i][j]=='BP':
                    self.Place_Piece(board, "images\BP.png", x + 60, y + 60)
                x += 100
            y += 100
    def new_Chess_Board(self,board):
        self.drawgrid(board)
        self.drawgrid(board)
        self.Position_Pieces(board,self.Pos_Array)
    def update_UI_chess_board(self,board,Position_Positions,Position_New):

        for pos in Position_Positions:
            Prev_Y,Prev_X = pos
            if Prev_X!=None or Prev_Y!=None:
                if (Prev_X+Prev_Y)%2==0:
                    self.drawRectangle(board, Prev_X*100, Prev_Y*100, 100, 100, "#FDF6EC")
                else:
                    self.drawRectangle(board, Prev_X*100, Prev_Y*100, 100, 100, "#C69B7B")
        New_Y, New_X = Position_New
        if New_X != None or New_Y != None:
            if (New_X+New_Y)%2==0:
                self.drawRectangle(board, New_X*100, New_Y*100, 100, 100, "#FDF6EC")
            else:
                self.drawRectangle(board, New_X*100, New_Y*100, 100, 100, "#C69B7B")
        self.Position_Pieces(board, self.Pos_Array)



    def get_board(self):
        return self.Pos_Array
    def update_board(self,grid):
        self.Pos_Array = copy.deepcopy(grid)