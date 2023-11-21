from classes import *
import pygame
print("imported gui")
class Window:
    def __init__ (self,board,squareSize=50):
        self.board=board.board
        self.squareSize = squareSize
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode((720, 720))
        clock = pygame.time.Clock()
        running = True
        showDebug = False
        font = pygame.font.Font('freesansbold.ttf', 20) if showDebug else pygame.font.Font('chess.ttf', 20)
        font2 = pygame.font.Font('freesansbold.ttf', 40)
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")
            pieceToTrack = (3,0)
            # print(self.board[pieceToTrack[0]][pieceToTrack[1]].getMoves())
            for col in range(0,len(self.board[0])):
                for row in range(0,len(self.board)):
                    # print((row,7-col))
                    txtColor = "white" if self.board[col][row].piece.color == "w" else "black"
                    # print(txtColor)
                    if (col,row) == pieceToTrack: txtColor = "red"
                    pygame.draw.rect(screen,self.board[col][row].color(), pygame.Rect(col*self.squareSize,(7-row)*self.squareSize,self.squareSize,self.squareSize))
                    text = font.render(str(col)+str(row)+str(self.board[col][row].piece) if showDebug else self.board[col][row].piece.char, True, txtColor)
                    textRect = text.get_rect()
                    textRect.center = (((col) +0.5)* self.squareSize, (7-row+0.5) * self.squareSize)
                    screen.blit(text,textRect)
                    
                        
            moves = self.board[pieceToTrack[0]][pieceToTrack[1]].getMoves()
            # print(moves)
            for move in moves:
                txtColor = "Orange"
                if (move[0],move[1]) == pieceToTrack: txtColor = "red"
                # print(self.board[move[0]][move[1]].piece.char)
                txtToWrite = (str(move[0])+str(move[1])+str(self.board[move[0]][move[1]].piece)) if showDebug else (self.board[move[0]][move[1]].piece.char if len(self.board[move[0]][move[1]].piece.char) > 0 else "*")
                text = font.render(txtToWrite , True, txtColor) if txtToWrite != "*" else font2.render(txtToWrite, True, "Blue")
                # print(txtToWrite)
                textRect = text.get_rect()
                textRect.center = (((move[0]) +0.5)* self.squareSize, (7-move[1]+0.5) * self.squareSize)
                screen.blit(text,textRect)

            
            # flip() the display to put your work on screen
            pygame.display.flip()
            clock.tick(5)  # for every second, at most n frames will pass
        pygame.quit()
    def quit(self):
        pygame.quit()

game = Window(Board())