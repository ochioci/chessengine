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
        font = pygame.font.Font('freesansbold.ttf', 20)
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")
            pieceToTrack = (2,0)
            # print(self.board[pieceToTrack[0]][pieceToTrack[1]].getMoves())
            for col in range(0,len(self.board[0])):
                for row in range(0,len(self.board)):
                    # print((row,7-col))
                    txtColor = "Blue"
                    if (col,row) == pieceToTrack: txtColor = "red"
                    pygame.draw.rect(screen,self.board[col][row].color(), pygame.Rect(col*self.squareSize,row*self.squareSize,self.squareSize,self.squareSize))
                    text = font.render(str(col)+str(row)+str(self.board[col][row].piece), False, txtColor)
                    textRect = text.get_rect()
                    textRect.center = (((col) +0.5)* self.squareSize, (row+0.5) * self.squareSize)
                    screen.blit(text,textRect)
                    
                        
            moves = self.board[pieceToTrack[0]][pieceToTrack[1]].getMoves()
            # print(moves)
            for move in moves:
                text = font.render(str(move[0])+str(move[1])+str(self.board[move[0]][move[1]].piece), False, "pink")
                textRect = text.get_rect()
                textRect.center = (((move[0]) +0.5)* self.squareSize, (move[1]+0.5) * self.squareSize)
                screen.blit(text,textRect)

            
            # flip() the display to put your work on screen
            pygame.display.flip()
            clock.tick(60)  # limits fps
        pygame.quit()
    def quit(self):
        pygame.quit()

game = Window(Board())