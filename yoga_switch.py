#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Witch code of Copyright (C) 2014 Mark Lee / https://github.com/malept/yoga-modeswitch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
from itertools import chain
from functools import partial
import subprocess
import time
import sys, os, time

#Identify your Touchpad & Keyboard with "xinput list" in Terminal
TOUCHPAD = "ETPS/2 Elantech Touchpad"
KEYBOARD = "AT Translated Set 2 keyboard"




def run(*args):
    return subprocess.call(list(args))

xinput = partial(run, 'xinput')
xinput_disable = partial(run, 'xinput', 'disable')
xrandr = partial(run, 'xrandr')

TS_MATRIX = {
    'normal': [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]],
    'right': [[0, 1, 0],
              [-1, 0, 1],
              [0, 0, 1]],
    'left': [[0, -1, 1],
             [1, 0, 0],
             [0, 0, 1]],
    'inverted': [[-1, 0, 1],
                 [0, -1, 1],
                 [0, 0, 1]],
}

def switch_mode(touchMode):
    if touchMode:
        xinput('disable', TOUCHPAD)
        xinput('disable', KEYBOARD)
    else:
        xinput('enable', TOUCHPAD)
        xinput('enable', KEYBOARD)

def switch_orientation(orientation):
        xrandr('--orientation', orientation)

def switchTo(mode):
    if mode == "tablet":
        switch_mode(True)
        switch_orientation("normal")
    elif mode == "normal":
        switch_mode(False)
        switch_orientation("normal")
    elif mode == "stand":
        switch_mode(True)
        switch_orientation("inverted")


if len(sys.argv) == 2:
    switchTo(sys.argv[1])
else:
    f = open(os.path.join(os.path.dirname(__file__), 'current_mode'), "r+");
    current = f.read();
    f.seek(0)

    if(current == "" or current == "normal"):
        switchTo("stand")
        text = "stand"
    elif (current == "stand"):
        switchTo("tablet")
        text = "tablet"
    else:
        switchTo("normal")
        text = "normal"

    print("current: " + text)
    f.write(text)
    f.truncate()
    f.close()
