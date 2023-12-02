print("imported classes")
w = 8
h = 8


class Piece:
    def __init__(self, color="empty", square=None):
        self.dir = 1 if color == "w" else -1
        self.char = ""
        self.square = square
        self.hasMoved = False
        self.color = color
        self.type = "empty"
        self.val = 0

    def __str__(self):
        return self.type[0:1] + self.color[0:1]

    def isEmpty(self):
        return self.type == "empty"

    def legalMoves(self):
        return []
    def setSquare(self,sq):
        self.square=sq

class Pawn(Piece):
    def __init__(self, color, square=None):
        super().__init__(color, square)
        self.val = 1
        self.char = "o"
        self.type = "pawn"

    def legalMoves(self):  # working
        moves = []
        ahead = self.square.board.squareStatus(self.square.x, self.square.y + self.dir, self.color)
        ahead2 = self.square.board.squareStatus(self.square.x, self.square.y + self.dir + self.dir, self.color)
        # print(ahead,ahead2)
        diagLeft = self.square.board.squareStatus(self.square.x + 1, self.square.y + self.dir, self.color)
        diagRight = self.square.board.squareStatus(self.square.x - 1, self.square.y + self.dir, self.color)
        # print(diagLeft, diagRight)
        if ahead == 0:  # empty
            moves.append((self.square.x, self.square.y + self.dir))
            if (not self.hasMoved and ahead2 != 1):
                moves.append((self.square.x, self.square.y + (2 * self.dir)))
        if diagRight == 2:  # enemy piece
            moves.append((self.square.x - 1, self.square.y + self.dir))
        if diagLeft == 2:  # enemy piece
            moves.append((self.square.x + 1, self.square.y + self.dir))
        moves = filter((lambda move: not (move[0] >= w or move[1] >= h or move[0] < 0 or move[1] < 0)), moves)
        return list(moves)


class Knight(Piece):
    def legalMoves(self):
        moves = filter(lambda move: self.square.board.squareStatus(move[0], move[1], self.color) != 1,
                       self.square.getMoves())
        return list(moves)

    def __init__(self, color, square=None):
        super().__init__(color, square)
        self.val = 3
        self.char = "j"
        self.type = "knight"


class Rook(Piece):
    def legalMoves(self):
        moves = []
        lx,ly = self.square.x, self.square.y
        for i in range(0, ly)[::-1]:
            st = self.square.board.squareStatus(lx, i,self.color)
            if st != 1:
                moves.append((lx,i))
            if st != 0:
                break
        for i in range(ly+1, 8):
            st = self.square.board.squareStatus(lx, i,self.color)
            if st != 1:
                moves.append((lx,i))
            if st != 0:
                break
        for i in range(0, lx)[::-1]:
            st = self.square.board.squareStatus(i, ly,self.color)
            if st != 1:
                moves.append((i,ly))
            if st != 0:
                break
        for i in range(lx+1, 8):
            st = self.square.board.squareStatus(i, ly, self.color)
            if st != 1:
                moves.append((i,ly))
            if st != 0:
                break

        return moves
    def __init__(self, color, square=None):
        super().__init__(color, square)
        self.val = 5
        self.char = "t"
        self.type = "rook"


class Bishop(Piece):
    def legalMoves(self):#1 is friendly 2 is enemy
        moves = []
        lx,ly = self.square.x, self.square.y
        for a in range(1,8-max(lx,ly)):
            st = self.square.board.squareStatus(lx+a, ly+a)
            if st != 1:
                moves.append(((lx+a),(ly+a)))
            if st != 0:
                break
        for a in range(1,8-max(7-lx,ly)):
            st = self.square.board.squareStatus(lx-a, ly+a)
            if st != 1:
                moves.append(((lx-a),(ly+a)))
            if st != 0:
                break

        for a in range(1, min(lx,ly)+1):
            st = self.square.board.squareStatus(lx-a, ly-a)
            if st != 1:
                moves.append(((lx-a),(ly-a)))
            if st != 0:
                break

        for a in range(1, min(7-lx,ly)+1):
            st = self.square.board.squareStatus(lx+a, ly-a)
            if st != 1:
                moves.append(((lx+a),(ly-a)))
            if st != 0:
                break
        for i in range(0, ly)[::-1]:
            st = self.square.board.squareStatus(lx, i, self.color)
            if st != 1:
                moves.append((lx, i))
            if st != 0:
                break
        for i in range(ly + 1, 8):
            st = self.square.board.squareStatus(lx, i, self.color)
            if st != 1:
                moves.append((lx, i))
            if st != 0:
                break
        for i in range(0, lx)[::-1]:
            st = self.square.board.squareStatus(i, ly, self.color)
            if st != 1:
                moves.append((i, ly))
            if st != 0:
                break
        for i in range(lx + 1, 8):
            st = self.square.board.squareStatus(i, ly, self.color)
            if st != 1:
                moves.append((i, ly))
            if st != 0:
                break
        return moves



    def __init__(self, color, square=None):
        super().__init__(color, square)
        self.val = 3
        self.char = "n"
        self.type = "bishop"


class Queen(Piece):
    def legalMoves(self):
        moves = []
        lx, ly = self.square.x, self.square.y
        for a in range(1, 8 - max(lx, ly)):
            st = self.square.board.squareStatus(lx + a, ly + a)
            if st != 1:
                moves.append(((lx + a), (ly + a)))
            if st != 0:
                break
        for a in range(1, 8 - max(7 - lx, ly)):
            st = self.square.board.squareStatus(lx - a, ly + a)
            if st != 1:
                moves.append(((lx - a), (ly + a)))
            if st != 0:
                break

        for a in range(1, min(lx, ly) + 1):
            st = self.square.board.squareStatus(lx - a, ly - a)
            if st != 1:
                moves.append(((lx - a), (ly - a)))
            if st != 0:
                break

        for a in range(1, min(7 - lx, ly) + 1):
            st = self.square.board.squareStatus(lx + a, ly - a)
            if st != 1:
                moves.append(((lx + a), (ly - a)))
            if st != 0:
                break
        # print(lx, ly, moves)
        return moves

    def __init__(self, color, square=None):
        super().__init__(color, square)
        self.val = 9
        self.char = "w"
        self.type = "queen"


class King(Piece):
    def __init__(self, color, square=None):
        super().__init__(color, square)
        self.val = 3
        self.char = "l"
        self.type = "king"


class Square:
    def isEmpty(self):
        return self.piece.type == "empty"
    def getMoves(self):
        moves = []
        pieceType = self.piece.type
        match pieceType:  # working i think?
            case "pawn":  # missing en passant
                moves.append((self.x, self.y + (1 if self.piece.color == "w" else -1)))
                if self.piece.hasMoved == False: moves.append((self.x, self.y + (2 if self.piece.color == "w" else -2)))
            case "king":
                moves = [(self.x + i, self.y + n) for i in range(-1, 2) for n in range(-1, 2)]
            case "bishop":
                moves = [(self.x + i, self.y + i) for i in range(-7, 8)] + [(self.x - i, self.y + i) for i in range(-7, 8)]
            case "knight":
                moves = [(self.x + i + i, self.y + i) for i in range(-1, 2)] + [(self.x + i, self.y + i + i) for i in range(-1, 2)] + [(self.x + i + i, self.y - i) for i in range(-1, 2)] + [(self.x + i, self.y - i - i) for i in range(-1, 2)]
            case "rook":
                moves = [(self.x + i, self.y) for i in range(-7, 8)] + [(self.x, self.y + i) for i in range(-7, 8)]
            case "queen":
                moves = [(self.x + i, self.y + i) for i in range(-7, 8)] + [(self.x - i, self.y + i) for i in range(-7, 8)] + [(self.x + i, self.y) for i in range(-7, 8)] + [(self.x, self.y + i) for i in range(-7, 8)]
            case default:
                pass
        moves = filter((lambda move: not (move[0] >= w or move[1] >= h or move[0] < 0 or move[1] < 0)), moves)
        # print(list(moves))
        return list(moves)

    def color(self):
        return "forestgreen" if self.clr == 1 else "tan"

    def setPiece(self, piece):
        self.piece = piece

    def __init__(self, board, x, y, color, piece):
        self.board = board
        self.clr = color
        self.x = x
        self.y = y
        self.piece = piece

    def __str__(self):
        return (self.piece.type)[0:1] + self.piece.color[0:1] if self.piece.type != "empty" else self.color()[0:2]


class Board:
    def movePiece(self, x1, y1, x2, y2):
        temp = self.board[x1][y1].piece
        temp.square = self.board[x2][y2]
        self.board[x1][y1].piece = Piece(square=self.board[x1][y1])
        self.board[x2][y2].piece = temp


    def squareStatus(self, x, y, clr="w"):
        # print(x,y, self.board[x][y].piece.color) 
        # print()
        if self.board[x][y].piece.color == clr:
            return 1  # friendly piece
        elif self.board[x][y].piece.color == "empty":
            return 0
        else:
            return 2 # enemy piece

    def getEval(self):
        z = self.getSquareWeights()
        return round(sum([sum(z[i]) for i in range(0, len(z))]), 3)

    def getSquareWeights(self, wClr="w"):
        return [[round((((h) - ((((i - 3.5) ** 2) + ((n - 3.5) ** 2)) ** 0.33)) / 6) * (
            1 if self.board[n][i].piece.color == wClr else -1) * self.board[n][i].piece.val, 3) for i in range(0, 8)]
                for n in range(0, 8)]

    def eval(self):
        pass

    def __init__(self, w=8, h=8, buildPawns=True):
        self.board = []
        self.w = w
        self.h = h

        class Codes:
            wPieces, bPieces, wPawn, bPawn, lRook, rRook, lKnight, rKnight, lBishop, rBishop, qu, ki = 0, h - 1, 1, h - 2, 0, w - 1, 1, w - 2, 2, w - 3, 3, 4

        for x in range(0, w):
            col = []
            for y in range(0, h):
                clr = ((x + y) % 2) + 1
                piece = Piece(color="empty")
                sq = Square(self, x, y, clr, piece)
                match y:
                    case Codes.wPawn | Codes.bPawn:
                        if buildPawns: piece = Pawn("w" if y == Codes.wPawn else "b", sq)
                        pass
                    case Codes.wPieces | Codes.bPieces:
                        match x:
                            case Codes.lRook | Codes.rRook:
                                piece = Rook("w" if y == Codes.wPieces else "b", sq)
                            case Codes.lKnight | Codes.rKnight:
                                piece = Knight("w" if y == Codes.wPieces else "b", sq)
                            case Codes.lBishop | Codes.rBishop:
                                piece = Bishop("w" if y == Codes.wPieces else "b", sq)
                            case Codes.qu:
                                piece = Queen("w" if y == Codes.wPieces else "b", sq)
                            case Codes.ki:
                                piece = King("w" if y == Codes.wPieces else "b", sq)
                            case default:
                                pass
                    case default:
                        pass
                sq.setPiece(piece)
                col.append(sq)
            self.board.append(col)

    def __str__(self):
        allStr = ""
        datStr = ""
        for col in range(0, len(self.board[0]))[::-1]:
            rowStr = ""
            rowStr2 = ""
            for row in range(0, len(self.board)):
                # print(self.board[row][col].piece.isMoveLegal(0,0))
                rowStr += str(self.board[row][col])
                rowStr2 += str(row) + str(col)
                # print(self.board[row][col].getMoves())
            allStr += rowStr + "\n"
            datStr += rowStr2 + "\n"
        return allStr + "\n" + "\n" + datStr

    def displayRowMajor(self):
        out = "each square is displayed as i,n representing board[i][n]\n"
        for i in range(0, len(self.board)):
            r = ""
            for n in range(0, len(self.board[i])):
                r += str(i) + str(n)
            out += r + '\n'
        out += "\n\n"
        for i in self.board:
            r = ""
            for n in i:
                r += str(n)
            out += r + '\n'
        return out

# myBoard = Board()
# print("legal moves:")
# print(myBoard.board[0][0].piece.getLegalMoves())
