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
MSG_GREET = (
    'What do you want to calculate?\n'
    'type "n" for number of monthly payments,\n'
    'type "a" for annuity monthly payment amount,\n'
    'type "p" for loan principal:\n'
)
MSG_ENTER_PRINCIPAL = 'Enter the loan principal:\n'
MSG_ENTER_PAYMENT = 'Enter the monthly payment:\n'
MSG_ENTER_PERIODS = 'Enter the number of periods:\n'
MSG_ENTER_INTEREST = 'Enter the loan interest:\n'
MSG_REPORT_PERIODS_MONTHS = 'It will take {MONTHS} months to repay this loan!'
MSG_REPORT_PERIODS_ONE_YEAR = 'It will take 1 year to repay this loan!'
MSG_REPORT_PERIODS = 'It will take {YEARS} years and {MONTHS} months to repay this loan!'
MSG_REPORT_PAYMENT = 'Your monthly payment = {PAYMENT}!'
MSG_REPORT_PRINCIPAL = 'Your loan principal = {PRINCIPAL}!'
CHOICE_MONTHS = 'n'
CHOICE_PAYMENT = 'a'
CHOICE_PRINCIPAL = 'p'

# --------------------
# START OF PROGRAM
# --------------------

# Choose wherever the calculation is for:
#   * the number of monthly payments 'n'
#   * the annuity monthly payment 'a'
#   * the loan principal 'p'
calc_choice = input(MSG_GREET)

# Handle number of monthly payments choice.
if calc_choice == CHOICE_MONTHS:
    # Read loan principal, monthly annuity payment and loan interest  .
    principal = float(input(MSG_ENTER_PRINCIPAL))
    payment = float(input(MSG_ENTER_PAYMENT))
    interest = float(input(MSG_ENTER_INTEREST))
    # Calculate the nominal interest.
    # nominal interest = interest% / (12 months * 100%)
    interest = interest / (12 * 100)
    # calculate the number of payments(months).
    # number of payments =
    #                      log _(nominal interest + 1)_ (
    #                           annuity payment
    #                           / (annuity payment - nominal interest * loan principal)
    #                       )
    months = math.ceil(math.log(
        (payment / (payment - interest * principal)),
        (interest + 1)
    ))
    # Convert months to years and months.
    years = months // 12
    months = months % 12
    # Print the repayment period.
    # Take special care to account for a period of a year or less.
    if years < 1:
        print(MSG_REPORT_PERIODS_MONTHS.format(MONTHS=months))
    elif years == 1:
        print(MSG_REPORT_PERIODS_ONE_YEAR)
    else:  # years > 1
        print(MSG_REPORT_PERIODS.format(YEARS=years, MONTHS=months))
# Handle the annuity monthly payment choice.
elif calc_choice == CHOICE_PAYMENT:
    # Read loan principal, number of periods(months) to repay and the loan interest  .
    principal = float(input(MSG_ENTER_PRINCIPAL))
    months = int(input(MSG_ENTER_PERIODS))
    interest = float(input(MSG_ENTER_INTEREST))
    # Calculate the nominal interest.
    # nominal interest = interest% / (12 months * 100%)
    interest = interest / (12 * 100)
    # Calculate the monthly annuity repayment.
    # annuity payment =
    #               loan principal
    #               * (nominal interest * (1 + nominal interest)^number of payments)
    #               / ((1 + nominal interest)^number of payments - 1)
    payment = math.ceil(
        principal
        * (interest * math.pow((1 + interest), months))
        / (math.pow((1 + interest), months) - 1)
    )
    # Print the monthly annuity payment
    print(MSG_REPORT_PAYMENT.format(PAYMENT=payment))
# Handle the loan principal choice.
else:  # calc_choice == CHOICE_PRINCIPAL
    # Read monthly annuity payment, number of periods(months) to repay and loan interest.
    payment = float(input(MSG_ENTER_PAYMENT))
    months = int(input(MSG_ENTER_PERIODS))
    interest = float(input(MSG_ENTER_INTEREST))
    # Calculate the nominal interest.
    # nominal interest = interest% / (12 months * 100%)
    interest = interest / (12 * 100)
    # Calculate the loan principal.
    # loan principal =
    #               annuity payment
    #               / (
    #                   (nominal interest * (1 + nominal interest)^number of payments)
    #                   / ((1 + nominal interest)^number of payments - 1)
    #               )
    principal = math.floor(
            payment
            / (
                (interest * math.pow((1 + interest), months))
                / (math.pow((1 + interest), months) - 1)

            )
    )
    # Print the loan principal.
    print(MSG_REPORT_PRINCIPAL.format(PRINCIPAL=principal))
