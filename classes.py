class Piece:
    def __init__(self,color):
        self.color="empty"
        self.type="empty"
    def __str__(self):
        return self.type[0:1]+self.color[0:1]
class Pawn(Piece):
    def __init__(self,color):
        self.type="pawn"
        self.color=color
class Knight(Piece):
    def __init__(self,color):
        self.type="knight"
        self.color=color
class Rook(Piece):
    def __init__(self,color):
        self.type="rook"
        self.color = color
class Bishop(Piece):
    def __init__(self,color):
        self.type="bishop"
        self.color = color
class Queen(Piece):
    def __init__(self,color):
        self.type="queen"
        self.color = color
class King(Piece):
    def __init__(self,color):
        self.type="king"
        self.color=color


class Square:
    def __init__(self,board,x,y,color,piece):
        self.x=x
        self.y=y
        self.color=color
        self.piece=piece
    def __str__(self):
        return (self.piece.__class__.__name__)[0:2]
class Board:
    def __init__(self,w=8,h=8):
        self.board=[]
        self.w=w
        self.h=h
        class Codes: wPieces,bPieces,wPawn,bPawn,lRook,rRook,lKnight,rKnight,lBishop,rBishop,qu,ki=0,h-1,1,h-2,0,w-1,1,w-2,2,w-3,4,5
        for x in range(0,w):
            col = []
            for y in range(0,h):
                clr = ((x%2)+(y%2))%2
                piece = Piece("") 
                match y:
                    case Codes.wPawn|Codes.bPawn:
                        piece=Pawn("w" if y==Codes.wPawn else "b")
                    case Codes.wPieces|Codes.bPieces:
                        match x:
                            case Codes.lRook|Codes.rRook:
                                piece=Rook("w" if y ==Codes.wPieces else "b")
                            case Codes.lKnight|Codes.rKnight:
                                piece=Knight("w" if y == Codes.wPieces else "b")
                            case Codes.lBishop|Codes.rBishop:
                                piece=Bishop("w" if y == Codes.wPieces else "b")
                            case Codes.qu:
                                piece=Queen("w" if y == Codes.wPieces else "b")
                            case Codes.ki:
                                piece=King("w" if y == Codes.wPieces else "b")
                            case default:
                                pass
                    case default:
                        pass
                col.append(Square(self,x,y,clr,piece))
            self.board.append(col)
    def __str__(self):
        allStr = ""
        for col in range(0,len(self.board[0]))[::-1]:
            rowStr =""
            for row in range(0,len(self.board)):
                rowStr += str(self.board[row][col].piece)
            allStr += rowStr + "\n"
        return allStr

print(Board())