import io
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
        if (self.square.y + self.dir) in range(0,8):
            ahead = self.square.board.squareStatus(self.square.x, self.square.y + self.dir, self.color)
            if self.square.x < 7:
                diagLeft = self.square.board.squareStatus(self.square.x + 1, self.square.y + self.dir, self.color)
                if diagLeft == 2:  # enemy piece
                    moves.append((self.square.x + 1, self.square.y + self.dir))
            if self.square.x > 0:
                diagRight = self.square.board.squareStatus(self.square.x - 1, self.square.y + self.dir, self.color)
                if diagRight == 2:  # enemy piece
                    moves.append((self.square.x - 1, self.square.y + self.dir))
            if (self.square.y + self.dir + self.dir) in range(0,8): ahead2 = self.square.board.squareStatus(self.square.x, self.square.y + self.dir + self.dir, self.color)
            if ahead == 0:  # empty
                moves.append((self.square.x, self.square.y + self.dir))
                if (not self.hasMoved and ahead2 != 1):
                    moves.append((self.square.x, self.square.y + (2 * self.dir)))


        # print(ahead,ahead2)

        # print(diagLeft, diagRight)

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
    def legalMoves(self):#square status 0 is empty 1 is friendly 2 is enemy
        moves = []
        lx,ly = self.square.x, self.square.y
        for a in range(1,8-max(lx,ly)):
            st = self.square.board.squareStatus(lx+a, ly+a, self.color)
            if st != 1:
                moves.append(((lx+a),(ly+a)))
            if st != 0:
                break
        for a in range(1,8-max(7-lx,ly)):
            st = self.square.board.squareStatus(lx-a, ly+a, self.color)
            if st != 1:
                moves.append(((lx-a),(ly+a)))
            if st != 0:
                break

        for a in range(1, min(lx,ly)+1):
            st = self.square.board.squareStatus(lx-a, ly-a, self.color)
            if st != 1:
                moves.append(((lx-a),(ly-a)))
            if st != 0:
                break

        for a in range(1, min(7-lx,ly)+1):
            st = self.square.board.squareStatus(lx+a, ly-a, self.color)
            if st != 1:
                moves.append(((lx+a),(ly-a)))
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
            st = self.square.board.squareStatus(lx + a, ly + a, self.color)
            if st != 1:
                moves.append(((lx + a), (ly + a)))
            if st != 0:
                break
        for a in range(1, 8 - max(7 - lx, ly)):
            st = self.square.board.squareStatus(lx - a, ly + a, self.color)
            if st != 1:
                moves.append(((lx - a), (ly + a)))
            if st != 0:
                break

        for a in range(1, min(lx, ly) + 1):
            st = self.square.board.squareStatus(lx - a, ly - a, self.color)
            if st != 1:
                moves.append(((lx - a), (ly - a)))
            if st != 0:
                break

        for a in range(1, min(7 - lx, ly) + 1):
            st = self.square.board.squareStatus(lx + a, ly - a, self.color)
            if st != 1:
                moves.append(((lx + a), (ly - a)))
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
        # print(lx, ly, moves)
        return moves

    def __init__(self, color, square=None):
        super().__init__(color, square)
        self.val = 9
        self.char = "w"
        self.type = "queen"


class King(Piece):
    def legalMoves(self):
        moves = []
        for lx in range(self.square.x - 1, self.square.x + 2):
            for ly in range(self.square.y - 1, self.square.y + 2):
                if 0 > lx or lx > 7 or 0 > ly or ly > 7 or (lx == self.square.x and ly == self.square.y):
                    continue
                st = self.square.board.squareStatus(lx, ly, self.color)
                if st != 1:
                    moves.append((lx, ly))
        return moves
    
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
        temp.hasMoved = True
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
    def convToStr(self):
        curBoard = self.board
        newBoard = [['em','em','em','em','em','em','em','em'],
                    ['em','em','em','em','em','em','em','em'],
                    ['em','em','em','em','em','em','em','em'],
                    ['em','em','em','em','em','em','em','em'],
                    ['em','em','em','em','em','em','em','em'],
                    ['em','em','em','em','em','em','em','em'],
                    ['em','em','em','em','em','em','em','em'],
                    ['em','em','em','em','em','em','em','em']]
        
        for r in range(8):
            for c in range(8):
                sq = curBoard[r][c]
                if sq.isEmpty() == False:
                    if sq.piece.color == "w":
                        if sq.piece.type == "knight":
                            newBoard[r][c] = "bn"
                        else:
                            newBoard[r][c] = "b"+sq.piece.type[0]
                    else:
                        if sq.piece.type == "knight":
                            newBoard[r][c] = "wn"
                        else:
                            newBoard[r][c] = "w"+sq.piece.type[0]

        #newBoard = list(zip(newBoard))[::-1]
        return newBoard

    """def rotate(self, arr):
        r, c = len(arr), len(arr[0])
        newArr = [[None] * r for _ in range(c)]
        for col in range(c):
            for row in range(r-1, -1, -1):
                newArr[col-c-1][row] = arr[row][col]
        return newArr"""
    def transpose(self, A, N):
        newA = A
        for i in range(N):
            for j in range(i+1, N):
                newA[i][j], newA[j][i] = newA[j][i], newA[i][j]
        return newA
        
    def fen(self):
        curBoard = self.board
        strBoard = self.transpose(self.convToStr(), 8)
        # Use StringIO to build string more efficiently than concatenating
        with io.StringIO() as s:
            for row in strBoard:
                empty = 0
                for cell in row:
                    c = cell[0]
                    if c in ('w', 'b'):
                        if empty > 0:
                            s.write(str(empty))
                            empty = 0
                        s.write(cell[1].upper() if c == 'w' else cell[1].lower())
                    else:
                        empty += 1
                if empty > 0:
                    s.write(str(empty))
                s.write('/')
            # Move one position back to overwrite last '/'
            s.seek(s.tell() - 1)
            # If you do not have the additional information choose what to put
            s.write(' w KQkq - 0 1')
            return s.getvalue()





myBoard = Board()
# print("legal moves:")
# print(myBoard.board[0][0].piece.getLegalMoves())
print(myBoard.convToStr())
print(myBoard.transpose(myBoard.convToStr(), 8))
print(myBoard.fen())

class BoardValues:
    def __init__(self):
        self.Pawn = [0,  0,   0,   0,   0,   0,  0, 0,
                     5, 10,  10, -20, -20,  10, 10, 5,
                     5, -5, -10,   0,   0, -10, -5, 5,
                     0,  0,   0,  20,  20,   0,  0, 0,
                     5,  5,  10,  25,  25,  10,  5, 5,
                     10,10,  20,  30,  30,  20, 10,10,
                     50,50,  50,  50,  50,  50, 50,50,
                     0,  0,  0,    0,   0,   0,  0, 0
                     ]

        self.Knight = [-50, -40, -30, -30, -30, -30, -40, -50,
                       -40, -20,   0,   0,   0,   0, -20, -40,
                       -30,   5,  10,  15,  15,  10,   5, -30,
                       -30,   0,  15,  20,  20,  15,   0, -30,
                       -30,   5,  15,  20,  20,  15,   5, -30,
                       -30,   0,  10,  15,  15,  10,   0, -30,
                       -40, -20,   0,   5,   5,   0, -20, -40,
                       -50, -40, -30, -30, -30, -30, -40, -50
                       ]

        self.Bishop = [-20,-10,-10,-10,-10,-10,-10,-20,
                       -10,  5,  0,  0,  0,  0,  5,-10,
                       -10, 10, 10, 10, 10, 10, 10,-10,
                       -10,  0, 10, 10, 10, 10,  0,-10,
                       -10,  5,  5, 10, 10,  5,  5,-10,
                       -10,  0,  5, 10, 10,  5,  0,-10,
                       -10,  0,  0,  0,  0,  0,  0,-10,
                       -20,-10,-10,-10,-10,-10,-10,-20
                       ]

        self.Rook = [ 0, 0,  0,  5,  5,  0,  0,  0,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                      5,10, 10, 10, 10, 10, 10,  5,
                      0, 0,  0,  0,  0,  0,  0,  0
                     ]

        self.Queen = [-10,   5,   5,  5,  5,   5,   0, -10,
                      -10,   0,   5,  0,  0,   0,   0, -10,
                        0,   0,   5,  5,  5,   5,   0,  -5,
                       -5,   0,   5,  5,  5,   5,   0,  -5,
                      -10,   0,   0,  0,  0,   0,   0, -10,
                      -10,   0,   5,  5,  5,   5,   0, -10,
                      -20, -10, -10, -5, -5, -10, -10, -20,
                      -20, -10, -10, -5, -5, -10, -10, -20
                      ]

        self.KingEarly = [ 20,  30,  10,   0,   0,  10,  30,  20,
                           20,  20,   0,   0,   0,   0,  20,  20,
                          -10, -20, -20, -20, -20, -20, -20, -10,
                          -20, -30, -30, -40, -40, -30, -30, -20,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30
                          ]

        self.KingLate = [-50, -30,-30,-30,-30,-30, -30, -50,
                         -30, -30,  0,  0,  0,  0, -30, -30,
                         -30, -10, 20, 30, 30, 20, -10, -30,
                         -30, -10, 30, 40, 40, 30, -10, -30,
                         -30, -10, 30, 40, 40, 30, -10, -30,
                         -30, -10, 20, 30, 30, 20, -10, -30,
                         -30, -20,-10,  0,  0,-10, -20, -30,
                         -50, -40,-30,-20,-20,-30, -40, -50
                         ]
        

class Eval():

    def __init__(self, board, color):
        self.board = board
        self.color = color
        self.boardValues = BoardValues()
        self.lateGameWhite = False
        self.lateGameBlack = False

        #Cretes empty BoardLayout list from where comparisons can be made.
        self.boardLayout = [None] * 64

        # Actually populate boardLayout with data from boardString.
        self.populate()

    def populate(self):

        boardString = self.board.fen()

        # Gets rid of unnecessary data at end of string
        boardString = boardString[0:boardString.find(' ')]
        boardString = boardString + '/'

        # Basic String manipulation to determine where every piece on the board should be positioned
        counter = 0

        for y in range(8):
            dash = boardString.find('/')
            rawCode = boardString[0:dash]
            boardString = boardString[dash + 1:len(boardString)]

            for char in rawCode:
                if char.isdigit():
                    counter += int(char)
                else:
                    self.boardLayout[counter] = char
                    counter += 1

    def materialComp(self):

        total = 0
        boardString = self.board.fen()

        # Gets rid of unnecessary data at end of string
        boardString = boardString[0:boardString.find(' ')]

        # Basic String manipulation to determine where every piece on the board should be positioned
        for i in boardString:
            if str(i) == "P": total += 100
            elif str(i) == "N": total += 320
            elif str(i) == "B": total += 330
            elif str(i) == "R": total += 500
            elif str(i) == "Q": total += 900
            elif str(i) == "K": total += 20000

            elif str(i) == "p": total -= 100
            elif str(i) == "n": total -= 320
            elif str(i) == "b": total -= 330
            elif str(i) == "r": total -= 500
            elif str(i) == "q": total -= 900
            elif str(i) == "k": total -= 20000
            else: pass

        return total

    def development(self):
        total = 0
        counter = 0
        # GamePos determines whether it is early or late game that determines how aggressive the king should be.
        # 1 Means it is Late game and 0 it is Early to mid Game.

        numberOfMinorPiecesWhite = 0
        numberOfMinorPiecesBlack = 0

        for piece in self.boardLayout:
            if piece != None:
                if str(piece) == "P":
                    total += self.boardValues.Pawn[-(counter-63)]
                elif str(piece) == "N":
                    total += self.boardValues.Knight[-(counter-63)]
                    numberOfMinorPiecesWhite += 1
                elif str(piece) == "B":
                    total += self.boardValues.Bishop[-(counter-63)]
                    numberOfMinorPiecesWhite += 1
                elif str(piece) == "R":
                    total += self.boardValues.Rook[-(counter-63)]
                    numberOfMinorPiecesWhite += 1
                elif str(piece) == "Q":
                    total += self.boardValues.Queen[-(counter-63)]
                    numberOfMinorPiecesWhite += 1

                #######################################################################

                elif str(piece) == "p":
                    total -= self.boardValues.Pawn[counter]
                elif str(piece) == "n":
                    total += self.boardValues.Knight[counter]
                    numberOfMinorPiecesBlack += 1
                elif str(piece) == "b":
                    total += self.boardValues.Bishop[counter]
                    numberOfMinorPiecesBlack += 1
                elif str(piece) == "r":
                    total += self.boardValues.Rook[counter]
                    numberOfMinorPiecesBlack += 1
                elif str(piece) == "q":
                    total += self.boardValues.Queen[counter]
                    numberOfMinorPiecesBlack += 1

            counter += 1

        counter = 0
        for piece in self.boardLayout:
            if piece != None:
                # If True it is still early game.
                if str(piece) == "k":
                    if (numberOfMinorPiecesBlack >= 3):
                        total += self.boardValues.KingEarly[counter]
                    else:
                        total += self.boardValues.KingLate[counter]
                        self.lateGameBlack = True
                        print("Black LAte")

                # If True it is still early game.
                elif str(piece) == "K":
                    if (numberOfMinorPiecesWhite >= 3):
                        total += self.boardValues.KingEarly[-(counter - 63)]
                    else:
                        total += self.boardValues.KingLate[-(counter - 63)]
                        self.lateGameWhite = True

            counter += 1

        return total

    def checkmate(self):

        total = 0

        if self.board.is_checkmate:
            if self.color == "W":
                total += 50000
            else:
                total -= 50000

        return total

    def is_late_game(self):
        self.development()
        if (self.lateGameBlack) and (self.lateGameWhite):
            return True
        else:
            return False

    def result(self):
        total = 0

        #1 Material Comp gives int val to board acording to what pieces is still on the board
        total += self.materialComp()

        #2 Develompent gives int val to board acording to where on board pieces is located uses Piece_Development_Values.py
        total += self.development()

        #3 Gives int value if the current move could put the opposite player in checkmate
        total += self.checkmate()

        return total
