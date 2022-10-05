#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summary

Description
"""


# --------------------
# Imports
# --------------------
# Standard library modules:

# Third party modules:

# Local scripts and modules:
# --------------------


def run_honest_calculator():
    import honest_calculator.run
    honest_calculator.run.run()


def run_loan_calculator():
    import loan_calculator.run
    loan_calculator.run.run()


def run():
    # run_honest_calculator()
    run_loan_calculator()
    pass


if __name__ == "__main__":
    run()
