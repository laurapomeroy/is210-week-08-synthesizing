#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Deciding on paint colors"""

BASECOL = 'Which base color, '
ACCENTCOL = 'Which accent color, '
HIGHLIGHTCOL = 'Which hightlight color, '

BASE = raw_input(BASECOL + '"Seattle Gray" or "Manatee?" ')

if BASE == 'Seattle Gray':
    ACCENT = raw_input(BASECOL + '"Ceramic Glaze" or "Cumulus Nimbus"? ')
    HIGHLIGHT = raw_input(HIGHLIGHTCOL + '"Basically White" or "White"? ')
if BASE == 'Manatee':
    ACCENT = raw_input(ACCENTCOL + '"Platinum Mist" or "Spartan Sage"? ')
    HIGHLIGHT = raw_input(HIGHLIGHTCOL + '"Bone White" or "Just White"? ')

    print ('Your selected colors are, {}, {}, and {}.'.format(BASE, ACCENT,
                                                              HIGHLIGHT))
