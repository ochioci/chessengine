w=8
h=8
class Piece:
    def __init__(self,color,square=None):
        self.square = square
        self.hasMoved=False
        self.color="empty"
        self.type="empty"
    def __str__(self):
        return self.type[0:1]+self.color[0:1]
    # def isMoveLegal(x,y):
class Pawn(Piece):
    def __init__(self,color,square=None):
        super().__init__(color,square)
        self.type="pawn"
class Knight(Piece):
    def __init__(self,color,square=None):
        super().__init__(color,square)
        self.type="knight"
class Rook(Piece):
    def __init__(self,color,square=None):
        super().__init__(color,square)
        self.type="rook"

class Bishop(Piece):
    def __init__(self,color,square=None):
        super().__init__(color,square)
        self.type="bishop"
class Queen(Piece):
    def __init__(self,color,square=None):
        super().__init__(color,square)
        self.type="queen"
class King(Piece):
    def __init__(self,color,square=None):
        super().__init__(color,square)
        self.type="king"


class Square:
    def getMoves(self):
        moves = []
        pieceType = self.piece.type
        match pieceType:
            case "pawn": moves.append((self.x,self.y+(1 if self.piece.color=="w" else -1)))
            case "king": moves = [(self.x+i,self.y+n) for i in range(-1,2) for n in range(-1,2)]
            case "bishop": moves = [(self.x+i,self.y+n) for i in range(-7,8) for n in range(-7,8)] + [(self.x+i,self.y+n) for i in range(-7,8)[::-1] for n in range(-7,8)[::-1]]
            case "knight": moves = [(self.x+(2*i),self.y+n) for i in range(-1,2) for n in range(-1,2)] + [(self.x+i,self.y+(2*n)) for i in range(-1,2) for n in range(-1,2)]
            case "rook": moves = [(self.x+i,self.y) for i in range(-7,8)] + [(self.x,self.y+i) for i in range(-7,8)]
            case "queen": moves = [(self.x+i,self.y) for i in range(-7,8)] + [(self.x,self.y+i) for i in range(-7,8)] + [(self.x+i,self.y+n) for i in range(-7,8) for n in range(-7,8)] + [(self.x+i,self.y+n) for i in range(-7,8)[::-1] for n in range(-7,8)[::-1]]
            case default: pass
        return list(set(list(map((lambda move : (min(7, max(move[0],0)), min(7, max(move[1],0)))),moves))))
    def color(self):
        return ("black" if self.clr == 0 else "white")
    def setPiece(self,piece):
        self.piece = piece
    def __init__(self,board,x,y,color,piece):
        self.clr = color
        self.x=x
        self.y=y
        self.piece=piece
    def __str__(self):
        return (self.piece.type if self.piece.type != "empty" else self.color())[0:2]
class Board:
    def __init__(self,w=8,h=8):
        self.board=[]
        self.w=w
        self.h=h
        class Codes: wPieces,bPieces,wPawn,bPawn,lRook,rRook,lKnight,rKnight,lBishop,rBishop,qu,ki=0,h-1,1,h-2,0,w-1,1,w-2,2,w-3,3,4
        for x in range(0,w):
            col = []
            for y in range(0,h):
                clr = (x+y)%2
                piece = Piece("") 
                sq = Square(self,x,y,clr,piece)
                match y:
                    case Codes.wPawn|Codes.bPawn:
                        piece=Pawn("w" if y==Codes.wPawn else "b",sq)
                    case Codes.wPieces|Codes.bPieces:
                        match x:
                            case Codes.lRook|Codes.rRook:
                                piece=Rook("w" if y ==Codes.wPieces else "b",sq)
                            case Codes.lKnight|Codes.rKnight:
                                piece=Knight("w" if y == Codes.wPieces else "b",sq)
                            case Codes.lBishop|Codes.rBishop:
                                piece=Bishop("w" if y == Codes.wPieces else "b",sq)
                            case Codes.qu:
                                piece=Queen("w" if y == Codes.wPieces else "b",sq)
                            case Codes.ki:
                                piece=King("w" if y == Codes.wPieces else "b",sq)
                            case default:
                                pass
                    case default:
                        pass
                sq.setPiece(piece)
                col.append(sq)
            self.board.append(col)
    def __str__(self):
        allStr = ""
        for col in range(0,len(self.board[0]))[::-1]:
            rowStr =""
            for row in range(0,len(self.board)):
                rowStr += str(self.board[row][col])
                print(self.board[row][col].getMoves())
            allStr += rowStr + "\n"
        return allStr
    def displayRowMajor(self):
        out="each square is displayed as i,n representing board[i][n]\n"
        for i in range(0,len(self.board)):
            r=""
            for n in range(0,len(self.board[i])):
                r+=str(i)+str(n)
            out+=r+'\n'
        out+="\n\n"
        for i in self.board:
            r=""
            for n in i:
                r+=str(n)
            out+=r+'\n'
        return out

print(Board().displayRowMajor())