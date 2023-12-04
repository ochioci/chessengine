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
            if image != "ee":
                screen.blit(IMAGES[image], pygame.Rect(r * squareSize, (7 - c) * squareSize, squareSize, squareSize))





surfaceImage = True

# insert this into the middle of the while loop 
if surfaceImage:
    drawInterface(screen, self.squareSize, self.board)
    if clicked[0] > -1:
    moves = self.board[clicked[0]][clicked[1]].piece.legalMoves()
    for move in moves:
        color = ("Red" if len(self.board[move[0]][move[1]].piece.char) > 0 else "Blue")
        pygame.draw.rect(screen,color,((move[0] * self.squareSize, (7 - move[1]) * self.squareSize),(self.squareSize+1,self.squareSize+1)),width=2)