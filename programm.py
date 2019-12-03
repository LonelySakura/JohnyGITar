import pygame
from board import Board


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.colors = [None, pygame.Color('blue'), pygame.Color('red')]
        self.select = None

    def on_click(self, cell_coords):
        col, row = cell_coords
        if self.select:
            if self.board[row][col] == 2:
                self.board[row][col] = 1
                self.select = None
            if self.board[row][col] == 0:
                if self.has_path(*self.select, col, row):
                    self.board[row][col] = 1
                    self.board[self.select[1]][self.select[0]] = 0
                    self.select = None
        else:
            if self.board[row][col] == 0:
                self.board[row][col] = 1
            elif self.board[row][col] == 1:
                self.select = col, row
                self.board[row][col] = 2

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size, self.cell_size
                )
                color = self.colors[self.board[row][col]]
                if color:
                    pygame.draw.circle(screen, color, rect.center, self.cell_size // 2 - 2)
        super().render(screen)

    def has_path(self, x1, y1, x2, y2):
        return True


pygame.init()
w, h = 10, 10
size = width, height = 20 + w * 30, 20 + h * 30
screen = pygame.display.set_mode(size)
board = Lines(w, h)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
pygame.quit()

