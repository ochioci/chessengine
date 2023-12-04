from classes import *
import pygame

print("imported gui")


# images file is required for this function
def drawInterface(screen, squareSize, board):
    IMAGES = {}
    images = ['wp', 'wr', 'wn', 'wb', 'wk', 'wq', 'bp', 'br', 'bn', 'bb', 'bk', 'bq', 'wBoard', 'bBoard']
    for image in images:
        IMAGES[image] = pygame.transform.scale(pygame.image.load("images/" + image + ".png"),(squareSize, squareSize))
    for r in range(8):
        for c in range(8):
            if (c + r) % 2 == 0:
                screen.blit(IMAGES['bBoard'], pygame.Rect(r * squareSize, (7 - c) * squareSize, squareSize, squareSize))
            else:
                screen.blit(IMAGES['wBoard'], pygame.Rect(r * squareSize, (7 - c) * squareSize, squareSize, squareSize))
            image = str(board[r][c].piece)[::-1]
            if board[r][c].piece.type == "knight": image = image.replace("k","n")
            if image != "ee":
                screen.blit(IMAGES[image], pygame.Rect(r * squareSize, (7 - c) * squareSize, squareSize, squareSize))


class Window:
    def __init__(self, board, squareSize=90, pieceToTrack=(0, 0)):
        self.board = board.board
        self.squareSize = squareSize
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode((720, 720))
        clock = pygame.time.Clock()
        running = True
        showSurfaceImage = True
        showDebug = True
        showLoc = True
        font = pygame.font.Font('freesansbold.ttf', 15) if showDebug else pygame.font.Font('chess.ttf', 20)
        font2 = pygame.font.Font('freesansbold.ttf', 40)
        clicked = (-1, 0)
        lastClicked = (-1, 0)
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    xc, yc = pygame.mouse.get_pos()
                    xc = min(7, max(xc // squareSize, 0))
                    yc = min(7, max(7 - (yc // squareSize), 0))
                    lastClicked = clicked
                    clicked = (xc, yc)
                    if clicked in self.board[lastClicked[0]][lastClicked[1]].piece.legalMoves():
                        board.movePiece(*lastClicked, *clicked)
                        clicked, lastClicked = (-1, 0), (-1, 0)
                    # print(self.board[xc][yc].isEmpty())
                    if lastClicked == clicked:
                        clicked, lastClicked = (-1, 0), (-1, 0)

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")
            self.pieceToTrack = pieceToTrack
            # print(self.board[pieceToTrack[0]][pieceToTrack[1]].getMoves())
            weights = board.getSquareWeights()
            for col in range(0, len(self.board[0])):
                for row in range(0, len(self.board)):
                    # print((row,7-col))
                    txtColor = "white" if self.board[col][row].piece.color == "w" else (
                        "black" if self.board[col][row].piece.color == "b" else "blue")
                    # print(txtColor)
                    if (col, row) == clicked and not self.board[col][row].isEmpty(): txtColor = "red"
                    if (col, row) == lastClicked and not self.board[col][row].isEmpty(): txtColor = "pink"
                    pygame.draw.rect(screen, self.board[col][row].color(),
                                     pygame.Rect(col * self.squareSize, (7 - row) * self.squareSize, self.squareSize,
                                                 self.squareSize))
                    text = font.render((str(col) + str(row) + str(self.board[col][row].piece)) if showLoc else str(
                        weights[col][row]) if showDebug else self.board[col][row].piece.char, True, txtColor)
                    textRect = text.get_rect()
                    textRect.center = (((col) + 0.5) * self.squareSize, (7 - row + 0.5) * self.squareSize)
                    screen.blit(text, textRect)

            drawInterface(screen, self.squareSize, self.board)

            if clicked[0] > -1:
                moves = self.board[clicked[0]][clicked[1]].piece.legalMoves()
                for move in moves:
                    if not showSurfaceImage:
                        txtColor = "Orange"
                        # if (move[0],move[1]) == self.pieceToTrack: txtColor = "red"
                        # print(self.board[move[0]][move[1]].piece.char)
                        txtToWrite = (str(move[0]) + str(move[1]) + str(
                            self.board[move[0]][move[1]].piece)) if showDebug else (
                            self.board[move[0]][move[1]].piece.char if len(
                                self.board[move[0]][move[1]].piece.char) > 0 else "*")
                        text = font.render(txtToWrite, True, txtColor) if txtToWrite != "*" else font2.render(txtToWrite,
                                                                                                              True, "Blue")
                        # print(txtToWrite)
                        textRect = text.get_rect()
                        textRect.center = (((move[0]) + 0.5) * self.squareSize, (7 - move[1] + 0.5) * self.squareSize)
                        screen.blit(text, textRect)
                    else:
                        color = (pygame.Color(207,0,86) if len(self.board[move[0]][move[1]].piece.char) > 0 else pygame.Color(48,60,102))
                        pygame.draw.rect(screen,color,((move[0] * self.squareSize-3, (7 - move[1]) * self.squareSize),(self.squareSize+3,self.squareSize+3)),width=4,border_radius=2)

            # if clicked[0] > -1:
            #     pygame.draw.rect(screen, "pink", pygame.Rect(clicked[0] * self.squareSize, (7 - clicked[1]) * self.squareSize, self.squareSize, self.squareSize))
            # if lastClicked[0] > -1:
            #     pygame.draw.rect(screen, "red", pygame.Rect(lastClicked[0] * self.squareSize, (7 - lastClicked[1]) * self.squareSize, self.squareSize, self.squareSize))

            # flip() the display to put your work on screen
            pygame.display.flip()
            clock.tick(60)  # for every second, at most n frames will pass
        pygame.quit()

    def quit(self):
        pygame.quit()


myBoard = Board()
x1, y1 = 3, 3
# print("moves:")
# print(myBoard.board[x1][y1].getMoves())
# print("legal moves")
# myBoard.movePiece(0,0,3,3)
# myBoard.movePiece(2,6,2,2)
a = myBoard.board[x1][y1].piece.legalMoves()
print("legal moves")
print(a)
game = Window(myBoard)
