#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""LOAN CALCULATOR stage 4

This is a basic calculator for loans.
It can calculate the per month payments for differential loans.
It can also count the monthly payments, principal,
and the loan repayment period for annuity loans.
It can not calculate interest rate.
It can be invoked from the command line or from another script.
Its positional arguments are:
    --type ['annuity' | 'diff'] --interest <float | int>
    [--principal <float | int>] [--payment <float | int>]
    [--periods <int>]
If invoked with missing or incorrect arguments it will print an error message and exit.
"""

# --------------------
# IMPORTS
# --------------------
import argparse
import math

# --------------------
# MESSAGES
# --------------------
MSG_INVALID_PARAMETERS = 'Incorrect parameters'
MSG_REPORT_ANNUITY_PAYMENT = 'Your annuity payment = {PAYMENT}!'
MSG_REPORT_DIFF_PAYMENT = 'Month {PERIOD}: payment is {PAYMENT}'
MSG_REPORT_OVERPAYMENT = 'Overpayment = {OVERPAYMENT}'
MSG_REPORT_PRINCIPAL = 'Your loan principal = {PRINCIPAL}!'
MSG_REPORT_PERIODS_MONTHS = 'It will take {MONTHS} months to repay this loan!'
MSG_REPORT_PERIODS_ONE_YEAR = 'It will take 1 year to repay this loan!'
MSG_REPORT_PERIODS_ROUND_YEARS = 'It will take {YEARS} years to repay this loan!'
MSG_REPORT_PERIODS = 'It will take {YEARS} years and {MONTHS} months to repay this loan!'

# --------------------
# CONSTANTS
# --------------------
LOAN_TYPE_ANNUITY_KEYWORDS = ['annuity']
LOAN_TYPE_DIFFERENTIATED_KEYWORDS = ['diff']
LOAN_TYPE_ANNUITY_ID = 1
LOAN_TYPE_DIFFERENTIATED_ID = 2
LOAN_TYPE_ERROR_ID = 3
# CALC_TYPE_KEYs format:
# loan_type, payment, principal, periods, interest
# [str, bool, bool, bool, bool]
CALC_TYPE_KEY_ANNUITY_PAYMENT = (
    LOAN_TYPE_ANNUITY_ID, False, True, True, True)
CALC_TYPE_KEY_ANNUITY_PRINCIPAL = (
    LOAN_TYPE_ANNUITY_ID, True, False, True, True)
CALC_TYPE_KEY_ANNUITY_PERIODS = (
    LOAN_TYPE_ANNUITY_ID, True, True, False, True)
CALC_TYPE_KEY_DIFF_PAYMENT = (
    LOAN_TYPE_DIFFERENTIATED_ID, False, True, True, True)
CALC_TYPE_ID_ANNUITY_PAYMENT = 1
CALC_TYPE_ID_ANNUITY_PRINCIPAL = 2
CALC_TYPE_ID_ANNUITY_PERIODS = 3
CALC_TYPE_ID_DIFF_PAYMENT = 4
CALC_TYPE_ID_ERROR = 5


# --------------------
# FUNCTIONS
# --------------------


def init_parser() -> argparse.ArgumentParser:
    """
    Define the input arguments.

    :return: argparse.ArgumentParser object with the necessary arguments declared.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--payment', type=float)
    parser.add_argument('--principal', type=float)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float)
    return parser


def infer_loan_type_id(loan_type: str):
    """
    Infer the ID of the loan type.

    Infer the ID of the loan type by matching it against
    the keywords listed in LOAN_TYPE_ANNUITY_KEYWORDS
    and LOAN_TYPE_DIFFERENTIATED_KEYWORDS.
    :param loan_type: A string value which suggests the type of the loan.
    :return: The ID code of the inferred loan type
    """
    if loan_type in LOAN_TYPE_ANNUITY_KEYWORDS:
        return LOAN_TYPE_ANNUITY_ID
    elif loan_type in LOAN_TYPE_DIFFERENTIATED_KEYWORDS:
        return LOAN_TYPE_DIFFERENTIATED_ID
    else:
        return LOAN_TYPE_ERROR_ID


def is_present(param_: int | float | None, zero_ok: bool = False) -> bool:
    """
    Check if a parameter is present.

    A parameter is considered present if:
      zero_ok is True and the parameters value is positive or zero.
      zero_ok is False and the parameters value is positive (but not zero).
      The parameters value is not None.
    :param zero_ok: True if the parameters value can be zero, False otherwise.
    :param param_: The parameter to be checked.
    :return: True if the parameter is considered present and False otherwise.
    """
    if param_ is None:
        return False
    elif zero_ok and (param_ >= 0):
        return True
    elif not zero_ok and (param_ > 0):
        return True
    else:
        return False


def gen_calc_type_key(
        loan_type: str, payment: float, principal: float, periods: int, interest: float
) -> tuple:
    """
    Generate a tuple which represents which parameters are present.

    For each parameter except the loan type insert into the list True
    if it is considered present in the input and False otherwise.
    The parameters: payment, principal and periods are considered present
    if their value is not none and is positive.
    The parameter interest is considered present if it's value
    is not none and is positive or zero.
    For the loan_type parameter insert into the list the appropriate
    loan type id.
    :param loan_type: The type of the loan (annuity or differentiated).
    :param payment: The payment for each repayment period.
    :param principal: The loan principal.
    :param periods: The number of periods(months)
                    in which the loan is to be repaid.
    :param interest: The annual interest rate of the loan.
    :return: A list with the format [str, bool, bool, bool, bool] matching
              the state of loan_type, payment, principal, periods, interest
              in that order.
    """
    return (
        infer_loan_type_id(loan_type),
        is_present(payment),
        is_present(principal),
        is_present(periods),
        is_present(interest, zero_ok=True)
    )


def infer_calc_type_id(
        loan_type: str, payment: float, principal: float, periods: int, interest: float
) -> int:
    """
    Infer the type of the calculation to be performed.

    Use the given parameters to infer the missing parameter that
    is to be calculated.
    Input validation is carried out as an implicit side effect of
    the input parameters not fitting any type of calculation.
    :param loan_type: The type of the loan (annuity or differentiated).
    :param payment: The payment for each repayment period.
    :param principal: The loan principal.
    :param periods: The number of periods(months)
                    in which the loan is to be repaid.
    :param interest: The annual interest rate of the loan.
    :return: The ID code of the calculation to be performed.
    """
    calc_type_key = gen_calc_type_key(
        loan_type, payment, principal, periods, interest)
    if calc_type_key == CALC_TYPE_KEY_ANNUITY_PAYMENT:
        return CALC_TYPE_ID_ANNUITY_PAYMENT
    elif calc_type_key == CALC_TYPE_KEY_ANNUITY_PERIODS:
        return CALC_TYPE_ID_ANNUITY_PERIODS
    elif calc_type_key == CALC_TYPE_KEY_ANNUITY_PRINCIPAL:
        return CALC_TYPE_ID_ANNUITY_PRINCIPAL
    elif calc_type_key == CALC_TYPE_KEY_DIFF_PAYMENT:
        return CALC_TYPE_ID_DIFF_PAYMENT
    else:
        return CALC_TYPE_ID_ERROR


def calc_nominal_interest(annual_interest: float) -> float:
    """
    Calculate nominal(monthly) interest from annual(yearly) interest.

    :param annual_interest: A float representing the annual interest rate.
    :return: A float representing the nominal interest rate.
    """
    return annual_interest / (12 * 100)


def output_diff_payments(principal: float, periods: int, interest: float):
    """
    Calculate and print the differential loan's payments per period and overpayment.

    :param principal: The loan principal.
    :param periods: The number of periods(months)
                    in which the loan is to be repaid.
    :param interest: The nominal interest rate of the loan.
    :return: None.
    """
    # Calculate the annuity loan's payment per period and overpayment.
    payments, overpayment = calc_diff_payment(principal, periods, interest)
    # Print the monthly annuity payment, and it's overpayment.
    print_diff_payment(payments, overpayment)


def calc_diff_payment(principal: float, periods: int, interest: float):
    """
    Calculate the differential loan's payments per period and overpayment.

    differentiated payment per period =
                (loan principal / total number of repayment periods)
                + nominal interest rate * (
                    loan principal - (
                        loan principal
                        * (current repayment period - 1)
                        / total number of repayment periods
                    )
                )
    :param principal: The loan principal.
    :param periods: The number of periods(months)
                    in which the loan is to be repaid.
    :param interest: The nominal interest rate of the loan.
    :return: None.
    """
    # Calculate the differential loan's payments.
    payments = []
    for period in range(periods):
        payment = math.ceil(
                (principal / periods)
                + interest
                * (
                        principal
                        - (principal * period / periods)
                )
        )
        payments.append(payment)
    # Calculate the loan's overpayment.
    overpayment = sum(payments) - principal
    return payments, math.ceil(overpayment)


def print_diff_payment(payments: list, overpayment: float):
    """
    Print the differential loan's payments per period and overpayment.

    :param payments: The list of differentiated payment.
    :param overpayment: A float representing the overpayment for the loan.
    :return: None.
    """
    # Print the monthly annuity payments, and the loan's total overpayment.
    for period in range(len(payments)):
        print(MSG_REPORT_DIFF_PAYMENT.format(
            PERIOD=period, PAYMENT=payments[period]))
    print()
    print(MSG_REPORT_OVERPAYMENT.format(OVERPAYMENT=overpayment))


def output_annuity_payment(principal: float, periods: int, interest: float):
    """
    Calculate and print the annuity loan's payment per period and overpayment.

    :param principal: The loan principal.
    :param periods: The number of periods(months)
                    in which the loan is to be repaid.
    :param interest: The nominal interest rate of the loan.
    :return: None.
    """
    # Calculate the annuity loan's payment per period and overpayment.
    payment, overpayment = calc_annuity_payment(principal, periods, interest)
    # Print the monthly annuity payment, and it's overpayment.
    print_annuity_payment(payment, overpayment)


def calc_annuity_payment(principal: float, periods: int, interest: float):
    """
    Calculate the annuity loan's payment per period and overpayment.

    annuity payment =
                  loan principal
                  * (nominal interest * (1 + nominal interest)^number of payments)
                  / ((1 + nominal interest)^number of payments - 1)
    :param principal: The loan principal.
    :param periods: The number of periods(months)
                    in which the loan is to be repaid.
    :param interest: The nominal interest rate of the loan.
    :return: None.
    """
    # Calculate the annuity loan's payment per period.
    payment = math.ceil(
            principal
            * (interest * math.pow((1 + interest), periods))
            / (math.pow((1 + interest), periods) - 1)
    )
    # Calculate the loan's overpayment.
    overpayment = payment * periods - principal
    return payment, math.ceil(overpayment)


def print_annuity_payment(payment: float, overpayment: float):
    """
    Print the annuity loan's principal and overpayment.

    Take note to convert the periods to months and years.
    :param payment: The payment for each repayment period.
    :param overpayment: A float representing the overpayment for the loan.
    :return: None.
    """
    # Print the monthly annuity payment, and it's overpayment.
    print(MSG_REPORT_ANNUITY_PAYMENT.format(PAYMENT=payment))
    print(MSG_REPORT_OVERPAYMENT.format(OVERPAYMENT=overpayment))


def output_annuity_principal(payment: float, periods: int, interest: float):
    """
    Calculate and print the annuity loan's principal and overpayment.

    :param payment: The payment for each repayment period.
    :param periods: The number of periods(months)
                    in which the loan is to be repaid.
    :param interest: The nominal interest rate of the loan.
    :return: None.
    """
    # Calculate the loan's principal and overpayment.
    principal, overpayment = calc_annuity_principal(payment, periods, interest)
    # Print the loan's principal and overpayment.
    print_annuity_principal(principal, overpayment)


def calc_annuity_principal(payment: float, periods: int, interest: float):
    """
    Calculate the annuity loans principal and overpayment.

    loan principal =
                  annuity payment
                  / (
                      (nominal interest * (1 + nominal interest)^number of payments)
                      / ((1 + nominal interest)^number of payments - 1)
                  )
    :param payment: The payment for each repayment period.
    :param periods: The number of periods(months)
                    in which the loan is to be repaid.
    :param interest: The nominal interest rate of the loan.
    :return: None.
    """
    # Calculate the loan's principal.
    principal = math.floor(
            payment
            / (
                    (interest * math.pow((1 + interest), periods))
                    / (math.pow((1 + interest), periods) - 1)
            )
    )
    # Calculate the loan's overpayment.
    overpayment = payment * periods - principal
    return principal, math.ceil(overpayment)


def print_annuity_principal(principal: float, overpayment: float):
    """
    Print the annuity loan's principal and overpayment.

    Take note to convert the periods to months and years.
    :param principal: The loan principal.
    :param overpayment: A float representing the overpayment for the loan.
    :return: None.
    """
    # Print the time it will take to repay the loan, and it's overpayment.
    print(MSG_REPORT_PRINCIPAL.format(PRINCIPAL=principal))
    print(MSG_REPORT_OVERPAYMENT.format(OVERPAYMENT=overpayment))


def output_annuity_periods(payment: float, principal: float, interest: float):
    """
    Calculate and print the time it will take to repay the annuity loan.

    :param payment: The payment for each repayment period.
    :param principal: The loan principal.
    :param interest: The nominal interest rate of the loan.
    :return: None.
    """
    # Calculate the time it will take to repay the loan, and it's overpayment.
    periods, overpayment = calc_annuity_periods(payment, principal, interest)
    # Print the time it will take to repay the loan, and it's overpayment.
    print_annuity_periods(periods, overpayment)


def calc_annuity_periods(payment: float, principal: float, interest: float):
    """
    Calculate the time it will take to repay the annuity loan.

     number of periods =
                          log _(nominal interest + 1)_ (
                               annuity payment
                               / (annuity payment - nominal interest * loan principal)
                           )
    :param payment: The payment for each repayment period.
    :param principal: The loan principal.
    :param interest: The nominal interest rate of the loan.
    :return: None.
    """
    # calculate the number of periods.
    periods = math.ceil(math.log(
        (payment / (payment - interest * principal)),
        (interest + 1)
    ))
    # Calculate the loan's overpayment.
    overpayment = payment * periods - principal
    return periods, math.ceil(overpayment)


def print_annuity_periods(periods: int, overpayment: float):
    """
    Print the time it will take to repay the annuity loan.

    Take note to convert the periods to months and years.
    :param periods: The number of periods(months)
                    in which the loan is to be repaid.
    :param overpayment: A float representing the overpayment for the loan.
    :return: None.
    """
    # Convert periods to years and months.
    years = periods // 12
    months = periods % 12
    # Print the time it will take to repay the loan.
    if years < 1:
        print(MSG_REPORT_PERIODS_MONTHS.format(MONTHS=months))
    elif years == 1:
        print(MSG_REPORT_PERIODS_ONE_YEAR)
    elif months == 0:
        print(MSG_REPORT_PERIODS_ROUND_YEARS.format(YEARS=years))
    else:
        print(MSG_REPORT_PERIODS.format(YEARS=years, MONTHS=months))
    print(MSG_REPORT_OVERPAYMENT.format(OVERPAYMENT=overpayment))


def run():
    # Initialise and setup command line arguments parser.
    parser = init_parser()

    # Parse the command line arguments and assign them to parameters.
    parameters = parser.parse_args()
    loan_type = parameters.type
    payment = parameters.payment
    principal = parameters.principal
    periods = parameters.periods
    interest = parameters.interest

    # Infer the ID for the type of desired calculation.
    calc_type_id = infer_calc_type_id(
        loan_type, payment, principal, periods, interest)

    # print error message and exit if arguments were invalid.
    if calc_type_id == CALC_TYPE_ID_ERROR:
        print(MSG_INVALID_PARAMETERS)
        exit()

    # Calculate the nominal interest rate.
    interest = calc_nominal_interest(interest)

    # Calculate and output the missing loan information.
    if calc_type_id == CALC_TYPE_ID_ANNUITY_PRINCIPAL:
        output_annuity_principal(payment, periods, interest)
    elif calc_type_id == CALC_TYPE_ID_ANNUITY_PAYMENT:
        output_annuity_payment(principal, periods, interest)
    elif calc_type_id == CALC_TYPE_ID_ANNUITY_PERIODS:
        output_annuity_periods(payment, principal, interest)
    elif calc_type_id == CALC_TYPE_ID_DIFF_PAYMENT:
        output_diff_payments(principal, periods, interest)


# --------------------
# start of program
# --------------------
if __name__ == "__main__":
    run()
