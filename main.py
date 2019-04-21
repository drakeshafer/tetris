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
DARK_GRAY = (76, 76, 76)
M_DARK_GRAY = (111, 111, 111)
GRAY = (165, 165, 165)
LIGHT_GRAY = (200, 200, 200)
V_LIGHT_GRAY = (229, 229, 229)
WHITE = (255, 255, 255)
# -- Colors -- #
PINK = (208, 45, 130)
BLUE = (45, 130, 208)
ELEC_BLUE = (45, 205, 208)
GREEN = (130, 208, 45)

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
win.fill(M_DARK_GRAY)



### ----- THE FUNCTIONS GO HERE ---- ###

## ----------------------------------------------------------------------- ##
#   Setup the game window
## ----------------------------------------------------------------------- ##
def setup_game_window():
    # -- Main board window -- #
    draw_with_border_and_shadow(win, PLAY_RECT, BLACK, V_LIGHT_GRAY, 5, ELEC_BLUE, 5, 7)
    # -- Title -- #
    disp_text(win, title_font, 'TETRIS', BLUE, (CENTER_X - 5, PLAY_RECT[1] / 2 + 5))
    disp_text(win, title_font, 'TETRIS', WHITE, (CENTER_X, PLAY_RECT[1] / 2))
    # -- Pieces window -- #
    draw_with_border_and_shadow(win, PIECES_RECT, BLACK, V_LIGHT_GRAY, 5, PINK, 5, 7)
    # -- Pieces Label -- #
    disp_text(win, label_font, 'PIECES', PINK, (PLAY_RECT[0] / 2 - 3, PIECES_RECT[1] * 5 / 6 + 3))
    disp_text(win, label_font, 'PIECES', WHITE, (PLAY_RECT[0] / 2, PIECES_RECT[1] * 5 / 6))


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
