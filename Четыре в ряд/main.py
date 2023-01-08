import pygame
import math
from log import *
from settings import *

g = Game
gen_field = g.field()
g.terminal_field(gen_field)
flag_end = False
move = 0

pygame.init()
g.field_generation(gen_field)
pygame.display.update()
win_phrase = pygame.font.SysFont("Arial", 82)

while not flag_end:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(win, WHITE, (150, 150, width, WINDOW))
            if move == 0:
                x = event.pos[0]
                col = int(math.floor(x/WINDOW))

                if g.check_pos(gen_field, col):
                    row = g.check_for_free_cell(gen_field, col)
                    g.drop_piece(gen_field, row, col, 1)

                    if g.vert_and_gor_win(gen_field, 1):
                        label = win_phrase.render("Победил красный", 0, RED)
                        win.blit(label, (40, 10))
                        flag_end = True
            else:
                x = event.pos[0]
                col = int(math.floor(x/WINDOW))

                if g.check_pos(gen_field, col):
                    row = g.check_for_free_cell(gen_field, col)
                    g.drop_piece(gen_field, row, col, 2)

                    if g.vert_and_gor_win(gen_field, 2):
                        label = win_phrase.render(
                            "Победил фиолетовый", 0, FIOL)
                        win.blit(label, (40, 10))
                        flag_end = True
            g.terminal_field(gen_field)
            g.field_generation(gen_field)

            move += 1
            move = move % 2

            if flag_end:
                pygame.time.wait(900)
