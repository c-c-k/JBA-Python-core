#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""loan_calculator

Description
"""

# --------------------
# IMPORTS
# --------------------
import math

# --------------------
# MESSAGES
# --------------------
MSG_ENTER_PRINCIPLE = 'Enter the loan principal:'
MSG_CHOOSE_CALC_1 = 'What do you want to calculate?'
MSG_CHOOSE_CALC_2 = 'type "m" for number of monthly payments,'
MSG_CHOOSE_CALC_3 = 'type "p" for the monthly payment:'
CHOICE_MONTHS = 'm'
CHOICE_PAYMENT = 'p'
MSG_ENTER_PAYMENT = 'Enter the monthly payment:'
MSG_ENTER_MONTHS = 'Enter the number of months:'
MSG_REPORT_MONTHS_1 = 'It will take'
MSG_REPORT_MONTHS_2 = 'months to repay the loan'
MSG_REPORT_MONTHS_SINGLE = 'It will take 1 month to repay the loan'
MSG_REPORT_PAYMENT_1 = 'Your monthly payment = '
MSG_REPORT_PAYMENT_2 = ' and the last payment = '
MSG_REPORT_PAYMENT_3 = '.'

# --------------------
# START OF PROGRAM
# --------------------

# Read loan principal.
print(MSG_ENTER_PRINCIPLE)
principal = float(input())

# Choose wherever the calculation is for the number of months
# or for the monthly payment.
print(MSG_CHOOSE_CALC_1)
print(MSG_CHOOSE_CALC_2)
print(MSG_CHOOSE_CALC_3)
calc_choice = input()

# Handle number of months choice.
if calc_choice == CHOICE_MONTHS:
    # Read monthly payment.
    print(MSG_ENTER_PAYMENT)
    payment = float(input())
    # Calculate the number of months to repay the loan.
    months = math.ceil(principal / payment)
    # Print the number of months.
    # Take special care of the message in case of a single month payment.
    if months > 1:
        print(' '.join([MSG_REPORT_MONTHS_1, str(months), MSG_REPORT_MONTHS_2]))
    else:
        print(MSG_REPORT_MONTHS_SINGLE)
# Handle monthly payment choice.
else:
    # Read the number of months to repay the loan
    print(MSG_ENTER_MONTHS)
    months = int(input())
    # Calculate monthly payment and the monthly payment for the last month.
    payment = math.ceil(principal / months)
    last_payment = principal - payment * (months - 1)
    # Print the monthly payment, add the last monthly payment if relevant.
    if last_payment == payment:
        print(''.join([MSG_REPORT_PAYMENT_1, str(payment)]))
    else:
        print(''.join([
            MSG_REPORT_PAYMENT_1, str(payment),
            MSG_REPORT_PAYMENT_2, str(last_payment),
            MSG_REPORT_PAYMENT_3
        ]))
