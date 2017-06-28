class chessBoard:
    def __init__(self,name,board):
        self.name=name
        self.board = [x for x in range(8)]

        for x in range(8):
            self.board[x]=[y for y in range()]
            for y in range(8):
                if ((x==0 and y==0) or (y==7 or (x==7 and (y==0 or y==7)))):
                    self.board[x][y]='rook'
                if (x==1 or x==6):
                    self.board[x][y]='pawn'
