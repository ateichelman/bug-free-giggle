import libtcodpy as tcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

font_path = 'data/fonts/arial10x10.png'
font_flags = tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD # May need to adjust.
tcod.console_set_custom_font(font_path, font_flags)

# Initializing window
window_title = 'Python 3 libtcod tutorial'
fullscreen = False
tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)

while not tcod.console_is_window_closed():
    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(0, 1, 1, '@', tcod.BKGND_NONE)
    tcod.console_flush()

# TODO: Moving around