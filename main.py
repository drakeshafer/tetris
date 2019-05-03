## ----------------------------------------------------------------------- ##
#
#   A Tetirs clone, made for fun, definitely not optimized.
#   Code written by Drake Shafe in April, 2019.
#
## ----------------------------------------------------------------------- ##


# -- Imports -- #
import sys
import pygame
# -- Inits -- #
pygame.init()


### ----- VARIABLES AND DEFINITIONS AND THINGS LIKE THAT ---- ###

## ----------------------------------------------------------------------- ##
#   Lots of colors
## ----------------------------------------------------------------------- ##
# -- Grays -- #
BLACK = (0, 0, 0)
V_DARK_GRAY = (45, 45, 45)
DARK_GRAY = (76, 76, 76)
M_DARK_GRAY = (111, 111, 111)
GRAY = (165, 165, 165)
LIGHT_GRAY = (200, 200, 200)
V_LIGHT_GRAY = (229, 229, 229)
WHITE = (255, 255, 255)
# -- Colors -- #
PINK = (208, 45, 130)
ELEC_PINK = (255, 76, 175)
BLUE = (45, 130, 208)
ELEC_BLUE = (45, 205, 208)
GREEN = (130, 210, 45)

## ----------------------------------------------------------------------- ##
#   Screen dimmensions
## ----------------------------------------------------------------------- ##
WIN_WIDTH = 1024
WIN_HEIGHT = 768
CENTER_X = WIN_WIDTH / 2
CENTER_Y = WIN_HEIGHT / 2
# -- Play area, arbitrary dimmensions, just looked good to me -- #
PLAY_RECT = pygame.Rect(WIN_WIDTH * 7 / 24, WIN_HEIGHT * 3 / 24, WIN_WIDTH * 5 / 12, WIN_HEIGHT * 5 / 6)
# -- Pieces area -- #
PIECES_RECT = pygame.Rect(WIN_WIDTH * 3 / 96, WIN_HEIGHT / 5, WIN_WIDTH * 21 / 96, WIN_HEIGHT * 2 / 3)
SCORE_RECT = pygame.Rect(WIN_WIDTH * 72 / 96, WIN_HEIGHT / 4, WIN_WIDTH * 21 / 96, WIN_HEIGHT * 1 / 5)
NEXT_RECT = pygame.Rect(WIN_WIDTH * 72 / 96, WIN_HEIGHT * 3 / 5, WIN_WIDTH * 21 / 96, WIN_HEIGHT * 1 / 5)


## ----------------------------------------------------------------------- ##
#   Fonts
## ----------------------------------------------------------------------- ##
title_font = pygame.font.SysFont(None, int(WIN_HEIGHT / 6), True)
label_font = pygame.font.SysFont(None, int(WIN_HEIGHT / 12))



### ----- SCREEN INITIALIZTION ---- ###

## ----------------------------------------------------------------------- ##
#   Game window
## ----------------------------------------------------------------------- ##
# -- Create Window -- #
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('---  TETRIS  by  DRAKE  ---')
win.fill(BLACK)



### ----- THE FUNCTIONS GO HERE ---- ###

## ----------------------------------------------------------------------- ##
#   Setup the game window
## ----------------------------------------------------------------------- ##
def setup_game_window():
    # -- Main board window -- #
    draw_with_border_and_shadow(win, PLAY_RECT, V_DARK_GRAY, V_LIGHT_GRAY, 5, BLUE, 5, 7)
    # -- Title -- #
    disp_text(win, title_font, 'TETRIS', BLUE, (CENTER_X - 5, PLAY_RECT[1] / 2 + 5))
    disp_text(win, title_font, 'TETRIS', V_LIGHT_GRAY, (CENTER_X, PLAY_RECT[1] / 2))
    # -- Pieces window -- #
    draw_with_border_and_shadow(win, PIECES_RECT, V_DARK_GRAY, V_LIGHT_GRAY, 5, BLUE, 5, 7)
    # -- Pieces Label -- #
    disp_text(win, label_font, 'PIECES', BLUE, (PLAY_RECT[0] / 2 - int(0.015 * WIN_WIDTH) - 3, PIECES_RECT[1] - int(0.04 * WIN_HEIGHT) + 3))
    disp_text(win, label_font, 'PIECES', V_LIGHT_GRAY, (PLAY_RECT[0] / 2 -int(0.015 * WIN_WIDTH), PIECES_RECT[1] - int(0.04 * WIN_HEIGHT)))
    # -- Stats Window -- #
    draw_with_border_and_shadow(win, SCORE_RECT, V_DARK_GRAY, V_LIGHT_GRAY, 5, BLUE, 5, 7)
    # -- Stats Label -- #
    disp_text(win, label_font, 'SCORE', BLUE, ((WIN_WIDTH + SCORE_RECT[0]) / 2 - int(0.035 * WIN_WIDTH) - 3, SCORE_RECT[1] - int(0.04 * WIN_HEIGHT)+ 3))
    disp_text(win, label_font, 'SCORE', V_LIGHT_GRAY, ((WIN_WIDTH + SCORE_RECT[0]) / 2 - int(0.035 * WIN_WIDTH), SCORE_RECT[1] - int(0.04 * WIN_HEIGHT)))
    # -- Next Piece Window -- #
    draw_with_border_and_shadow(win, NEXT_RECT, V_DARK_GRAY, V_LIGHT_GRAY, 5, BLUE, 5, 7)
    # -- Next Piece Label -- #
    disp_text(win, label_font, 'NEXT', BLUE, ((WIN_WIDTH + NEXT_RECT[0]) / 2 - int(0.05 * WIN_WIDTH) - 3, NEXT_RECT[1] - int(0.04 * WIN_HEIGHT) + 3))
    disp_text(win, label_font, 'NEXT', V_LIGHT_GRAY, ((WIN_WIDTH + NEXT_RECT[0]) / 2 - int(0.05 * WIN_WIDTH), NEXT_RECT[1] - int(0.04 * WIN_HEIGHT)))

## ----------------------------------------------------------------------- ##
#   Text display function
## ----------------------------------------------------------------------- ##
def disp_text(surface, font, text, color, center):
    text_rend = font.render(text, True, color)
    text_rect = text_rend.get_rect()
    text_rect.center = center
    surface.blit(text_rend, text_rect)

## ----------------------------------------------------------------------- ##
#   Draw a rectangle with a border and a shadow
## ----------------------------------------------------------------------- ##
def draw_with_border_and_shadow(surface, pos, main_color, border_color, border, shadow_color, offset, shadow_border=0):
    new_pos = pos.copy()
    new_pos[0] -= offset
    new_pos[1] += offset
    pygame.draw.rect(surface, shadow_color, new_pos, shadow_border)
    pygame.draw.rect(surface, main_color, pos)
    pygame.draw.rect(surface, border_color, pos, border)




### ----- MAIN PROGRAM AND GAME LOOP ----- ###

setup_game_window()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
