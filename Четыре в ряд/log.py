import numpy as np
import pygame
from settings import *

height = WINDOW * (ROW+1)
width = COL * WINDOW
win_size = (width, height)
win = pygame.display.set_mode(win_size)


class Game:
    def field():
        field = np.zeros((ROW, COL))
        return field

    def drop_piece(field, row, col, chip):
        field[row][col] = chip

    def check_pos(field, col):
        return field[ROW-1][col] == 0

    def check_for_free_cell(field, col):
        for row in range(ROW):
            if field[row][col] == 0:
                return row

    def terminal_field(field):
        print(np.flip(field, 0))

    def vert_and_gor_win(field, chip):
        for col in range(COL-3):
            for row in range(ROW):
                if (field[row][col] == chip) and (field[row][col+1] == chip) and (field[row][col+2] == chip) and (field[row][col+3] == chip):
                    return True

        for col in range(COL):
            for row in range(ROW-3):
                if (field[row][col] == chip) and (field[row+1][col] == chip) and (field[row+2][col] == chip) and (field[row+3][col] == chip):
                    return True

    def field_generation(field):
        for col in range(COL):
            for row in range(ROW):
                pygame.draw.rect(win, BLUE, (col*WINDOW, row *
                                             WINDOW+WINDOW, WINDOW, WINDOW))
                pygame.draw.circle(win, WHITE, (int(
                    col*WINDOW+WINDOW/2), int(row*WINDOW+WINDOW+WINDOW/2)), CELL)

        for col in range(COL):
            for row in range(ROW):
                if field[row][col] == 1:
                    pygame.draw.circle(win, RED, (int(
                        col*WINDOW+WINDOW/2), height-int(row*WINDOW+WINDOW/2)), CELL)
                elif field[row][col] == 2:
                    pygame.draw.circle(win, FIOL, (int(
                        col*WINDOW+WINDOW/2), height-int(row*WINDOW+WINDOW/2)), CELL)
        pygame.display.update()
