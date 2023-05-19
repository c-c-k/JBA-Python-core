#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Object -> Advanced  -> OOP
Topic name: Abstract classes
Question name: Deposits
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    from abc import ABC, abstractmethod
    
    class Account(ABC):
        def __init__(self, starting_sum, interest=None):
            self.sum = starting_sum
            self.interest = interest
    
        @abstractmethod
        def add_money(self, amount):
            ...
    
        def add_interest(self):
            ...
    
    # create SavingsAccount and Deposit

    class SavingsAccount(Account):
        def add_money(self, amount):
            if amount < 10:
                print('Cannot add to SavingsAccount: amount too low.')
            else:
                self.sum += amount

    class Deposit(Account):
        def add_money(self, amount):
            if amount < 50:
                print('Cannot add to Deposit: amount too low.')
            else:
                self.sum += amount

        def add_interest(self):
            self.sum = round(self.sum + self.sum * self.interest, 2)
    # -=- ANSWER CODE END -=-
    new_savings = SavingsAccount(50)
    new_savings.add_money(5)  # prints the following message:
    # Cannot add to SavingsAccount: amount too low.
    new_savings.add_money(30)
    new_savings.add_interest()
    print(new_savings.sum)
    # 80

    new_deposit = Deposit(60, 0.078)
    new_deposit.add_money(30)  # prints the following message:
    # Cannot add to Deposit: amount too low.
    new_deposit.add_money(70)
    new_deposit.add_interest()
    print(new_deposit.sum)
    # 140.14


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
