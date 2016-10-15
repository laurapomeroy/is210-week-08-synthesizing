#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculate lifetime compound interest of a loan"""

import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = int(raw_input('What is the amount of your principal? '))
YEARS = int(raw_input('For how many years is this loan being borrowed? '))
PRE = raw_input('Are you pre-qualified for this loan? ').lower()
RATE = 0

if PRINCIPAL <= 199999:
    if YEARS <= 15:
        if PRE == 'y' or PRE == 'yes':
            RATE = decimal.Decimal('0.0363')
        else:
            RATE = decimal.Decimal('0.0465')
    elif 16 <= YEARS <= 20:
        if PRE == 'y' or PRE == 'yes':
            RATE = decimal.Decimal('0.0404')
        else:
            RATE = decimal.Decimal('0.0498')
    else:
        if PRE == 'y' or PRE == 'yes':
            RATE = decimal.Decimal('0.0577')
        else:
            RATE = decimal.Decimal('0.0639')
elif 200000 <= PRINCIPAL <= 999999:
    if YEARS <= 15:
        if PRE == 'y' or PRE == 'yes':
            RATE = decimal.Decimal('0.0302')
        else:
            RATE = decimal.Decimal('.0398')
    if 16 <= YEARS <= 20:
        if PRE == 'y' or PRE == 'yes':
            RATE = decimal.Decimal('.0327')
        else:
            RATE = decimal.Decimal('.0408')
    elif 21 <= YEARS <= 30:
        if PRE == 'y' or PRE == 'yes':
            RATE = decimal.Decimal('.0466')
        else:
            RATE is None
    else:
        RATE is None
elif PRINCIPAL >= 1000000:
    if YEARS <= 15:
        if PRE == 'y' or PRE == 'yes':
            RATE = decimal.Decimal('.0205')
        elif 16 <= YEARS <= 20:
            RATE = decimal.Decimal('.0262')
        else:
            RATE is None
else:
    RATE is None

if RATE is None:
    ACCUMULATED = None
else:
    ACCUMULATED = round(PRINCIPAL * (1 + (RATE / 12)) ** (12 * YEARS))

DASHEDLINE = '-' * 60
PRE = PRE.capitalize()

if ACCUMULATED is None:
    REPORT = ('Loan Report for: {}\n'
              '{}\n'
              'Principal: ${:>10,}\n'
              'Duration: {:>9}yrs\n'
              'Prequalified?: {:>7}\n'
              '\n'
              'Total: N/A')
    print REPORT.format(NAME, DASHEDLINE, PRINCIPAL, YEARS, PRE)

else:

    REPORT = ('Loan Report for: {}\n'
              '{}\n'
              'Principal: ${:>10,}\n'
              'Duration: {:>9}yrs\n'
              'Prequalified?: {:>7}\n'
              '\n'
              'Total: ${:>14,}')

    print REPORT.format(NAME, DASHEDLINE, PRINCIPAL, YEARS, PRE, ACCUMULATED)
