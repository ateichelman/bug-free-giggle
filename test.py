# https://github.com/libtcod/python-tcod
# https://python-tcod.readthedocs.io/en/latest/
# https://github.com/libtcod/python-tcod/blob/master/examples/samples_tcod.py

import os

import copy
import math
import random
import time
import numpy as np
import tcod
import tcod.event

SAMPLE_SCREEN_WIDTH = 46
SAMPLE_SCREEN_HEIGHT = 20
SAMPLE_SCREEN_X = 20
SAMPLE_SCREEN_Y = 10
FONT = "data/fonts/consolas10x10_gs_tc.png"

root_console = None
sample_console = tcod.console.Console(
	SAMPLE_SCREEN_WIDTH, SAMPLE_SCREEN_HEIGHT, order="F"
)

class Sample(tcod.event.EventDispatch):
    def __init__ (self, name: str = ""):
        self.name = name

    def on_enter(self):
        pass

    def on_draw(self):
        pass

    def ev_keydown(self, event: tcod.event.KeyDown):
        global cur_sample
        if event.sym == tcod.event.K_DOWN:
            cur_sample = (cur_sample + 1) % len(SAMPLES)
            SAMPLES[cur_sample].on_enter()
            draw_samples_menu()
        elif event.sym == tcod.event.K_UP:
            cur_sample = (cur_sample - 1) % len(SAMPLES)
            SAMPLES[cur_sample].on_enter()
            draw_samples_menu()
        elif (
			event.sym == tcod.event.K_RETURN
			and event.mod & tcod.event.KMOD_LALT
		):
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
        elif event.sym == tcod.event.K_PRINTSCREEN or event.sym == ord("p"):
            print("screenshot")
            if event.mod & tcod.event.KMOD_LALT:
                tcod.console_save_apf(None, "samples.apf")
                print("apf")
            else:
                tcod.sys_save_screenshot()
                print("png")
        elif event.sym == tcod.event.K_ESCAPE:
            raise SystemExit()
        elif event.sym in RENDERER_KEYS:
            tcod.sys_set_renderer(RENDERER_KEYS[event.sym])
            draw_renderer_menu()

    def ev_quit(self, event: tcod.event.Quit):
        raise SystemExit()

    # TODO: Keep working through the tcod same, look up classes/functions as we encounter them.
