#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple alarm clock with snooze function"""


DAY = raw_input('What day is it? ').strip().lower()[:3]
TIME = int(raw_input('What is the time (4-digit number without a colon)? '))

SNOOZE = True if DAY is 'sat' or DAY is 'sun' or TIME < 600 else False

if not SNOOZE:
    print 'Beep! '*5
